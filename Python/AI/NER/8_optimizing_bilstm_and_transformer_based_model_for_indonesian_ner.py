# -*- coding: utf-8 -*-
"""8 - Optimizing BiLSTM and Transformer-based model for Indonesian NER

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1IimPtjt56ktPiRS7X_QUDAN2f_4xD9Ho

# Optimization with learning rate finder and early stopping

In [Part 7](https://colab.research.google.com/drive/1lq-5Qua6Oo60LjLMJfC1n5UNLJzezOJO?usp=sharing), I trained and compared the BiLSTM and Transformer-based model for Indonesian NER with exactly the same hyperparameters. However, different types of architecture possess different optimal hyperparameters. In this final part, I try to optimize [the most important one](https://arxiv.org/pdf/1506.01186.pdf): learning rate. 

To find a good approximation for LR, I use the [LR Finder for pytorch](https://github.com/davidtvs/pytorch-lr-finder). In essence, the method sweep over a potential range, perform a training sequence for each learning rate value, and note how well the model improved according to a preset metric. Finally, we can take the learning with which the model shows the best improvement. Bear in mind that this approach is not definitive by any means, it is just a helper.

Other than the hyperparameters, every architecture may require different number of epochs for training. To accommodate this variability, I adopt two techniques: reducing LR dynamically and early stopping. The former means we monitor the progress of the validation F1 score, if it does not improve after some epochs, we reduce the learning rate by a factor. Meanwhile, the latter deals with stopping the training when there is still no noticable improvement even after reducing the learning rate.
"""

from google.colab import drive
drive.mount("/content/gdrive")

import warnings
warnings.simplefilter(action='ignore', category=FutureWarning)

!pip install torchtext==0.6.0
!pip install pytorch-crf

import math
import time
import gensim
import torch
import torchcrf
import matplotlib.pyplot as plt
from torch import nn
from torch.optim import Adam
from torch.optim.lr_scheduler import ReduceLROnPlateau
from torchtext.data import Field, NestedField, BucketIterator
from torchtext.datasets import SequenceTaggingDataset
from torchtext.vocab import Vocab
from collections import Counter
from spacy.lang.id import Indonesian
from sklearn.metrics import f1_score, classification_report

"""To simplify the notebook, I put the LR Finder implementation as an external python script. You can check the content [here](https://github.com/yoseflaw/nerindo/blob/master/nerindo/lr_finder.py). The primary classes used are `LRFinder` and `ExponentialLR`."""

import sys
DRIVE_ROOT = "/content/gdrive/My Drive/Colab Notebooks/Nerindo"
if DRIVE_ROOT not in sys.path:
    sys.path.append(DRIVE_ROOT)
from lr_finder import LRFinder

available_gpu = torch.cuda.is_available()
if available_gpu:
    print(f"GPU is available: {torch.cuda.get_device_name(0)}")
    use_device = torch.device("cuda")
else:
    use_device = torch.device("cpu")

"""# Corpus

Nothing changes for corpus.
"""

class Corpus(object):

    def __init__(self, input_folder, min_word_freq, batch_size, wv_file=None):
        # list all the fields
        self.word_field = Field(lower=True)  # [sent len, batch_size]
        self.tag_field = Field(unk_token=None)  # [sent len, batch_size]
        # Character-level input
        self.char_nesting_field = Field(tokenize=list)
        self.char_field = NestedField(self.char_nesting_field)  # [batch_size, sent len, max len char]
        # create dataset using built-in parser from torchtext
        self.train_dataset, self.val_dataset, self.test_dataset = SequenceTaggingDataset.splits(
            path=input_folder,
            train="train.tsv",
            validation="val.tsv",
            test="test.tsv",
            fields=(
                (("word", "char"), (self.word_field, self.char_field)),
                ("tag", self.tag_field)
            )
        )
        # convert fields to vocabulary list
        if wv_file:
            self.wv_model = gensim.models.word2vec.Word2Vec.load(wv_file)
            self.embedding_dim = self.wv_model.vector_size
            word_freq = {word: self.wv_model.wv.vocab[word].count for word in self.wv_model.wv.vocab}
            word_counter = Counter(word_freq)
            self.word_field.vocab = Vocab(word_counter, min_freq=min_word_freq)
            vectors = []
            for word, idx in self.word_field.vocab.stoi.items():
                if word in self.wv_model.wv.vocab.keys():
                    vectors.append(torch.as_tensor(self.wv_model.wv[word].tolist()))
                else:
                    vectors.append(torch.zeros(self.embedding_dim))
            self.word_field.vocab.set_vectors(
                stoi=self.word_field.vocab.stoi,
                vectors=vectors,
                dim=self.embedding_dim
            )
        else:
            self.word_field.build_vocab(self.train_dataset.word, min_freq=min_word_freq)
        # build vocab for tag and characters
        self.char_field.build_vocab(self.train_dataset.char)
        self.tag_field.build_vocab(self.train_dataset.tag)
        # create iterator for batch input
        self.train_iter, self.val_iter, self.test_iter = BucketIterator.splits(
            datasets=(self.train_dataset, self.val_dataset, self.test_dataset),
            batch_size=batch_size
        )
        # prepare padding index to be ignored during model training/evaluation
        self.word_pad_idx = self.word_field.vocab.stoi[self.word_field.pad_token]
        self.char_pad_idx = self.char_field.vocab.stoi[self.char_field.pad_token]
        self.tag_pad_idx = self.tag_field.vocab.stoi[self.tag_field.pad_token]

#@title
corpus = Corpus(
    input_folder=f"{DRIVE_ROOT}/input",
    min_word_freq=3,
    batch_size=64,
    wv_file=f"{DRIVE_ROOT}/pretrain/embeddings/id_ft.bin"
)
print(f"Train set: {len(corpus.train_dataset)} sentences")
print(f"Val set: {len(corpus.val_dataset)} sentences")
print(f"Test set: {len(corpus.test_dataset)} sentences")

"""# Model

Nothing changes for model.
"""

class Embeddings(nn.Module):

    def __init__(self,
                 word_input_dim,
                 word_emb_dim,
                 word_emb_pretrained,
                 word_emb_dropout,
                 word_emb_froze,
                 use_char_emb,
                 char_input_dim,
                 char_emb_dim,
                 char_emb_dropout,
                 char_cnn_filter_num,
                 char_cnn_kernel_size,
                 char_cnn_dropout,
                 word_pad_idx,
                 char_pad_idx,
                 device
                 ):
        super().__init__()
        self.device = device
        self.word_pad_idx = word_pad_idx
        self.char_pad_idx = char_pad_idx
        # Word Embedding
        # initialize embedding with pretrained weights if given
        if word_emb_pretrained is not None:
            self.word_emb = nn.Embedding.from_pretrained(
                embeddings=torch.as_tensor(word_emb_pretrained),
                padding_idx=self.word_pad_idx,
                freeze=word_emb_froze
            )
        else:
            self.word_emb = nn.Embedding(
                num_embeddings=word_input_dim,
                embedding_dim=word_emb_dim,
                padding_idx=self.word_pad_idx
            )
            self.word_emb.weight.data[self.word_pad_idx] = torch.zeros(word_emb_dim)
        self.word_emb_dropout = nn.Dropout(word_emb_dropout)
        self.output_dim = word_emb_dim
        # Char Embedding
        self.use_char_emb = use_char_emb
        if self.use_char_emb:
            self.char_emb_dim = char_emb_dim
            self.char_emb = nn.Embedding(
                num_embeddings=char_input_dim,
                embedding_dim=char_emb_dim,
                padding_idx=char_pad_idx
            )
            # initialize embedding for char padding as zero
            self.char_emb.weight.data[self.char_pad_idx] = torch.zeros(self.char_emb_dim)
            self.char_emb_dropout = nn.Dropout(char_emb_dropout)
            # Char CNN
            self.char_cnn = nn.Conv1d(
                in_channels=char_emb_dim,
                out_channels=char_emb_dim * char_cnn_filter_num,
                kernel_size=char_cnn_kernel_size,
                groups=char_emb_dim  # different 1d conv for each embedding dim
            )
            self.char_cnn_dropout = nn.Dropout(char_cnn_dropout)
            self.output_dim += char_emb_dim * char_cnn_filter_num

    def forward(self, words, chars):
        # words = [sentence length, batch size]
        # chars = [batch size, sentence length, word length)
        # tags = [sentence length, batch size]
        # embedding_out = [sentence length, batch size, embedding dim]
        embedding_out = self.word_emb_dropout(self.word_emb(words))
        if not self.use_char_emb: return embedding_out
        # character cnn layer forward
        # reference: https://github.com/achernodub/targer/blob/master/src/layers/layer_char_cnn.py
        # char_emb_out = [batch size, sentence length, word length, char emb dim]
        char_emb_out = self.char_emb_dropout(self.char_emb(chars))
        batch_size, sent_len, word_len, char_emb_dim = char_emb_out.shape
        char_cnn_max_out = torch.zeros(batch_size, sent_len, self.char_cnn.out_channels, device=self.device)
        for sent_i in range(sent_len):
            # sent_char_emb = [batch size, word length, char emb dim]
            sent_char_emb = char_emb_out[:, sent_i, :, :]
            # sent_char_emb_p = [batch size, char emb dim, word length]
            sent_char_emb_p = sent_char_emb.permute(0, 2, 1)
            # char_cnn_sent_out = [batch size, out channels * char emb dim, word length - kernel size + 1]
            char_cnn_sent_out = self.char_cnn(sent_char_emb_p)
            char_cnn_max_out[:, sent_i, :], _ = torch.max(char_cnn_sent_out, dim=2)
        char_cnn = self.char_cnn_dropout(char_cnn_max_out)
        # concat word and char embedding
        # char_cnn_p = [sentence length, batch size, char emb dim * num filter]
        char_cnn_p = char_cnn.permute(1, 0, 2)
        word_features = torch.cat((embedding_out, char_cnn_p), dim=2)
        return word_features


class LSTMAttn(nn.Module):

    def __init__(self,
                 input_dim,
                 lstm_hidden_dim,
                 lstm_layers,
                 lstm_dropout,
                 word_pad_idx,
                 attn_heads=None,
                 attn_dropout=None
                 ):
        super().__init__()
        self.word_pad_idx = word_pad_idx
        self.lstm = nn.LSTM(
            input_size=input_dim,
            hidden_size=lstm_hidden_dim,
            num_layers=lstm_layers,
            bidirectional=True,
            dropout=lstm_dropout if lstm_layers > 1 else 0
        )
        self.attn_heads = attn_heads
        if self.attn_heads:
            self.attn = nn.MultiheadAttention(
                embed_dim=lstm_hidden_dim * 2,
                num_heads=attn_heads,
                dropout=attn_dropout
            )

    def forward(self, words, word_features):
        lstm_out, _ = self.lstm(word_features)
        if not self.attn_heads: return lstm_out
        # create masking for paddings
        key_padding_mask = torch.as_tensor(words == self.word_pad_idx).permute(1, 0)
        attn_out, _ = self.attn(lstm_out, lstm_out, lstm_out, key_padding_mask=key_padding_mask)
        return attn_out


class CRF(nn.Module):

    def __init__(self,
                 input_dim,
                 fc_dropout,
                 word_pad_idx,
                 tag_names,
                 ):
        super().__init__()
        self.word_pad_idx = word_pad_idx
        # Fully-connected
        self.fc_dropout = nn.Dropout(fc_dropout)
        self.fc = nn.Linear(input_dim, len(tag_names))
        # CRF
        self.crf = torchcrf.CRF(num_tags=len(tag_names))
        self.init_crf_transitions(tag_names)

    def forward(self, words, word_features, tags):
        # fc_out = [sentence length, batch size, output dim]
        fc_out = self.fc(self.fc_dropout(word_features))
        crf_mask = words != self.word_pad_idx
        crf_out = self.crf.decode(fc_out, mask=crf_mask)
        crf_loss = -self.crf(fc_out, tags=tags, mask=crf_mask) if tags is not None else None
        return crf_out, crf_loss

    def init_crf_transitions(self, tag_names, imp_value=-100):
        num_tags = len(tag_names)
        for i in range(num_tags):
            tag_name = tag_names[i]
            # I and L and <pad> impossible as a start
            if tag_name[0] in ("I", "L") or tag_name == "<pad>":
                torch.nn.init.constant_(self.crf.start_transitions[i], imp_value)
            # B and I impossible as an end
            if tag_name[0] in ("B", "I"):
                torch.nn.init.constant_(self.crf.end_transitions[i], imp_value)
        # init impossible transitions between positions
        tag_is = {}
        for tag_position in ("B", "I", "O", "U", "L"):
            tag_is[tag_position] = [i for i, tag in enumerate(tag_names) if tag[0] == tag_position]
        tag_is["P"] = [i for i, tag in enumerate(tag_names) if tag == "tag"]
        impossible_transitions_position = {
            "B": "BOUP",
            "I": "BOUP",
            "O": "IL",
            "U": "IL"
        }
        for from_tag, to_tag_list in impossible_transitions_position.items():
            to_tags = list(to_tag_list)
            for from_tag_i in tag_is[from_tag]:
                for to_tag in to_tags:
                    for to_tag_i in tag_is[to_tag]:
                        torch.nn.init.constant_(
                            self.crf.transitions[from_tag_i, to_tag_i], imp_value
                        )
        # init impossible B and I transitions to different entity types
        impossible_transitions_tags = {
            "B": "IL",
            "I": "IL"
        }
        for from_tag, to_tag_list in impossible_transitions_tags.items():
            to_tags = list(to_tag_list)
            for from_tag_i in tag_is[from_tag]:
                for to_tag in to_tags:
                    for to_tag_i in tag_is[to_tag]:
                        if tag_names[from_tag_i].split("-")[1] != tag_names[to_tag_i].split("-")[1]:
                            torch.nn.init.constant_(
                                self.crf.transitions[from_tag_i, to_tag_i], imp_value
                            )


class PositionalEncoding(nn.Module):

    def __init__(self, d_model, dropout=0.1, max_len=500):
        super(PositionalEncoding, self).__init__()
        self.dropout = nn.Dropout(p=dropout)
        pe = torch.zeros(max_len, d_model)
        position = torch.arange(0, max_len, dtype=torch.float).unsqueeze(1)
        div_term = torch.exp(torch.arange(0, d_model, 2).float() * (-math.log(10000.0) / d_model))
        pe[:, 0::2] = torch.sin(position * div_term)
        pe[:, 1::2] = torch.cos(position * div_term)
        pe = pe.unsqueeze(0).transpose(0, 1)
        self.register_buffer('pe', pe)

    def forward(self, x):
        x = x + self.pe[:x.size(0), :]
        return self.dropout(x)


class Transformer(nn.Module):

    def __init__(self,
                 input_dim,
                 attn_heads,
                 attn_dropout,
                 trf_layers,
                 fc_hidden,
                 word_pad_idx
                 ):
        super().__init__()
        self.word_pad_idx = word_pad_idx
        self.position_encoder = PositionalEncoding(
            d_model=input_dim
        )
        layers = nn.TransformerEncoderLayer(
            d_model=input_dim,
            nhead=attn_heads,
            activation="relu",
            dropout=attn_dropout
        )
        self.trf = nn.TransformerEncoder(
            encoder_layer=layers,
            num_layers=trf_layers
        )
        # 2-layers fully-connected with GELU activation in-between
        self.fc = nn.Linear(
            in_features=input_dim,
            out_features=fc_hidden
        )
        self.fc_gelu = nn.GELU()
        self.fc_norm = nn.LayerNorm(fc_hidden)
        self.output_dim = fc_hidden

    def forward(self, words, word_features):
        # Transformer
        key_padding_mask = torch.as_tensor(words == self.word_pad_idx).permute(1, 0)
        # pos_out = [sentence length, batch size, embedding dim + char emb dim * num filter]
        pos_out = self.position_encoder(word_features)
        # enc_out = [sentence length, batch size, embedding dim + char emb dim * num filter]
        trf_out = self.trf(pos_out, src_key_padding_mask=key_padding_mask)
        # fc_out = [sentence length, batch size, fc hidden]
        fc_out = self.fc_norm(self.fc_gelu(self.fc(trf_out)))
        return fc_out


class NERModel(nn.Module):

    def __init__(self,
                 word_input_dim,
                 word_pad_idx,
                 char_pad_idx,
                 tag_names,
                 device,
                 model_arch="bilstm",
                 word_emb_dim=300,
                 word_emb_pretrained=None,
                 word_emb_dropout=0.5,
                 word_emb_froze=False,
                 use_char_emb=False,
                 char_input_dim=None,
                 char_emb_dim=None,
                 char_emb_dropout=None,
                 char_cnn_filter_num=None,
                 char_cnn_kernel_size=None,
                 char_cnn_dropout=None,
                 lstm_hidden_dim=64,
                 lstm_layers=2,
                 lstm_dropout=0.1,
                 attn_heads=None,
                 attn_dropout=None,
                 trf_layers=None,
                 fc_hidden=None,
                 fc_dropout=0.25
                 ):
        super().__init__()
        # Embeddings
        self.embeddings = Embeddings(
            word_input_dim=word_input_dim,
            word_emb_dim=word_emb_dim,
            word_emb_pretrained=word_emb_pretrained,
            word_emb_dropout=word_emb_dropout,
            word_emb_froze=word_emb_froze,
            use_char_emb=use_char_emb,
            char_input_dim=char_input_dim,
            char_emb_dim=char_emb_dim,
            char_emb_dropout=char_emb_dropout,
            char_cnn_filter_num=char_cnn_filter_num,
            char_cnn_kernel_size=char_cnn_kernel_size,
            char_cnn_dropout=char_cnn_dropout,
            word_pad_idx=word_pad_idx,
            char_pad_idx=char_pad_idx,
            device=device
        )
        if model_arch.lower() == "bilstm":
            # LSTM-Attention
            self.encoder = LSTMAttn(
                 input_dim=self.embeddings.output_dim,
                 lstm_hidden_dim=lstm_hidden_dim,
                 lstm_layers=lstm_layers,
                 lstm_dropout=lstm_dropout,
                 word_pad_idx=word_pad_idx,
                 attn_heads=attn_heads,
                 attn_dropout=attn_dropout
            )
            encoder_output_dim = lstm_hidden_dim * 2
        elif model_arch.lower() == "transformer":
            # Transformer
            self.encoder = Transformer(
                input_dim=self.embeddings.output_dim,
                attn_heads=attn_heads,
                attn_dropout=attn_dropout,
                trf_layers=trf_layers,
                fc_hidden=fc_hidden,
                word_pad_idx=word_pad_idx
            )
            encoder_output_dim = self.encoder.output_dim
        else:
            raise ValueError("param `model_arch` must be either 'bilstm' or 'transformer'")
        # CRF
        self.crf = CRF(
            input_dim=encoder_output_dim,
            fc_dropout=fc_dropout,
            word_pad_idx=word_pad_idx,
            tag_names=tag_names
        )

    def forward(self, words, chars, tags=None):
        word_features = self.embeddings(words, chars)
        # lstm_out = [sentence length, batch size, hidden dim * 2]
        encoder_out = self.encoder(words, word_features)
        # fc_out = [sentence length, batch size, output dim]
        crf_out, crf_loss = self.crf(words, encoder_out, tags)
        return crf_out, crf_loss

    def save_state(self, path):
        torch.save(self.state_dict(), path)

    def load_state(self, path):
        self.load_state_dict(torch.load(path))

    def count_parameters(self):
        return sum(p.numel() for p in self.parameters() if p.requires_grad)

"""# Trainer

In the training sequence (`train()`) you can see the implementation of LR reduction and early stopping. For reducing LR, I use the pytorch built-in implementation `ReduceLROnPlateau`, while the early stopping is simply executed with a counter based on the F1 score. Note that the new score has to be at least 1% relatively better than the previous best score to be considered as a significant improvement.
"""

class Trainer(object):

    def __init__(self, model, data, optimizer, device, checkpoint_path=None):
        self.device = device
        self.model = model.to(self.device)
        self.data = data
        self.optimizer = optimizer
        self.checkpoint_path = checkpoint_path

    @staticmethod
    def epoch_time(start_time, end_time):
        elapsed_time = end_time - start_time
        elapsed_mins = int(elapsed_time / 60)
        elapsed_secs = int(elapsed_time - (elapsed_mins * 60))
        return elapsed_mins, elapsed_secs

    def f1_positive(self, preds, y, full_report=False):
        index_o = self.data.tag_field.vocab.stoi["O"]
        # take all labels except padding and "O"
        positive_labels = [i for i in range(len(self.data.tag_field.vocab.itos))
                           if i not in (self.data.tag_pad_idx, index_o)]
        # make the prediction one dimensional to follow sklearn f1 score input param
        flatten_preds = [pred for sent_pred in preds for pred in sent_pred]
        # remove prediction for padding and "O"
        positive_preds = [pred for pred in flatten_preds
                          if pred not in (self.data.tag_pad_idx, index_o)]
        # make the true tags one dimensional to follow sklearn f1 score input param
        flatten_y = [tag for sent_tag in y for tag in sent_tag]
        if full_report:
            # take all names except padding and "O"
            positive_names = [self.data.tag_field.vocab.itos[i]
                              for i in range(len(self.data.tag_field.vocab.itos))
                              if i not in (self.data.tag_pad_idx, index_o)]
            print(classification_report(
                y_true=flatten_y,
                y_pred=flatten_preds,
                labels=positive_labels,
                target_names=positive_names
            ))
        # average "micro" means we take weighted average of the class f1 score
        # weighted based on the number of support
        return f1_score(
            y_true=flatten_y,
            y_pred=flatten_preds,
            labels=positive_labels,
            average="micro"
        ) if len(positive_preds) > 0 else 0

    def epoch(self):
        epoch_loss = 0
        true_tags_epoch = []
        pred_tags_epoch = []
        self.model.train()
        for batch in self.data.train_iter:
            # words = [sent len, batch size]
            words = batch.word.to(self.device)
            # chars = [batch size, sent len, char len]
            chars = batch.char.to(self.device)
            # tags = [sent len, batch size]
            true_tags = batch.tag.to(self.device)
            self.optimizer.zero_grad()
            pred_tags_list, batch_loss = self.model(words, chars, true_tags)
            pred_tags_epoch += pred_tags_list
            # to calculate the loss and f1, we flatten true tags
            true_tags_epoch += [
                [tag for tag in sent_tag if tag != self.data.tag_pad_idx]
                for sent_tag in true_tags.permute(1, 0).tolist()
            ]
            batch_loss.backward()
            self.optimizer.step()
            epoch_loss += batch_loss.item()
        epoch_score = self.f1_positive(pred_tags_epoch, true_tags_epoch)
        return epoch_loss / len(self.data.train_iter), epoch_score

    def evaluate(self, iterator, full_report=False):
        epoch_loss = 0
        true_tags_epoch = []
        pred_tags_epoch = []
        self.model.eval()
        with torch.no_grad():
            # similar to epoch() but model is in evaluation mode and no backprop
            for batch in iterator:
                words = batch.word.to(self.device)
                chars = batch.char.to(self.device)
                true_tags = batch.tag.to(self.device)
                pred_tags, batch_loss = self.model(words, chars, true_tags)
                pred_tags_epoch += pred_tags
                true_tags_epoch += [
                    [tag for tag in sent_tag if tag != self.data.tag_pad_idx]
                    for sent_tag in true_tags.permute(1, 0).tolist()
                ]
                epoch_loss += batch_loss.item()
        epoch_score = self.f1_positive(pred_tags_epoch, true_tags_epoch, full_report)
        return epoch_loss / len(iterator), epoch_score

    ### BEGIN MODIFIED SECTION: LEARNING RATE ###
    def train(self, max_epochs, no_improvement=None):
        history = {
            "num_params": self.model.count_parameters(),
            "train_loss": [],
            "train_f1": [],
            "val_loss": [],
            "val_f1": [],
        }
        elapsed_train_time = 0
        best_val_f1 = 0
        best_epoch = None
        # scheduler object from pytorch
        # reduce learning rate by a factor of 0.3 if there is no performance
        # improvement after 3 epochs
        lr_scheduler = ReduceLROnPlateau(
            optimizer=self.optimizer,
            patience=3,
            factor=0.3,
            mode="max",
            verbose=True
        )
        epoch = 1
        n_stagnant = 0  # preparation for early stopping
        stop = False
        while not stop:
            start_time = time.time()
            train_loss, train_f1 = self.epoch()
            end_time = time.time()
            elapsed_train_time += end_time - start_time
            history["train_loss"].append(train_loss)
            history["train_f1"].append(train_f1)
            val_loss, val_f1 = self.evaluate(self.data.val_iter)
            lr_scheduler.step(val_f1)  # inform the scheduler
            # take the current model if it is at least 1% better than the previous best F1
            if self.checkpoint_path and val_f1 > (1.01 * best_val_f1):
                print(f"Epoch {epoch:5d}: found better Val F1: {val_f1:.4f} (Train F1: {train_f1:.4f}), saving model...")
                self.model.save_state(self.checkpoint_path)
                best_val_f1 = val_f1
                best_epoch = epoch
                n_stagnant = 0
            else:
                n_stagnant += 1
            history["val_loss"].append(val_loss)
            history["val_f1"].append(val_f1)
            if epoch >= max_epochs:
                print(f"Reach maximum number of epoch: {epoch}, stop training.")
                stop = True
            elif no_improvement is not None and n_stagnant >= no_improvement:
                print(f"No improvement after {n_stagnant} epochs, stop training.")
                stop = True
            else:
                epoch += 1
        if self.checkpoint_path and best_val_f1 > 0:
            self.model.load_state(self.checkpoint_path)
        test_loss, test_f1 = self.evaluate(self.data.test_iter)
        history["best_val_f1"] = best_val_f1
        history["best_epoch"] = best_epoch
        history["test_loss"] = test_loss
        history["test_f1"] = test_f1
        history["elapsed_train_time"] = elapsed_train_time
        return history
    ### END MODIFIED SECTION ###

    def infer(self, sentence, true_tags=None):
        self.model.eval()
        # tokenize sentence
        nlp = Indonesian()
        tokens = [token.text for token in nlp(sentence)]
        max_word_len = max([len(token) for token in tokens])
        # transform to indices based on corpus vocab
        numericalized_tokens = [self.data.word_field.vocab.stoi[token.lower()] for token in tokens]
        numericalized_chars = []
        char_pad_id = self.data.char_pad_idx
        for token in tokens:
            numericalized_chars.append(
                [self.data.char_field.vocab.stoi[char] for char in token]
                + [char_pad_id for _ in range(max_word_len - len(token))]
            )
        # find unknown words
        unk_idx = self.data.word_field.vocab.stoi[self.data.word_field.unk_token]
        unks = [t for t, n in zip(tokens, numericalized_tokens) if n == unk_idx]
        # begin prediction
        token_tensor = torch.as_tensor(numericalized_tokens)
        token_tensor = token_tensor.unsqueeze(-1).to(self.device)
        char_tensor = torch.as_tensor(numericalized_chars)
        char_tensor = char_tensor.unsqueeze(0).to(self.device)
        predictions, _ = self.model(token_tensor, char_tensor)
        # convert results to tags
        predicted_tags = [self.data.tag_field.vocab.itos[t] for t in predictions[0]]
        # print inferred tags
        max_len_token = max([len(token) for token in tokens] + [len('word')])
        max_len_tag = max([len(tag) for tag in predicted_tags] + [len('pred')])
        print(
            f"{'word'.ljust(max_len_token)}\t{'unk'.ljust(max_len_token)}\t{'pred tag'.ljust(max_len_tag)}"
            + ("\ttrue tag" if true_tags else "")
        )
        for i, token in enumerate(tokens):
            is_unk = "✓" if token in unks else ""
            print(
                f"{token.ljust(max_len_token)}\t{is_unk.ljust(max_len_token)}\t{predicted_tags[i].ljust(max_len_tag)}"
                + (f"\t{true_tags[i]}" if true_tags else "")
            )
        return tokens, predicted_tags, unks

"""Now, we can execute LR Finder for each of the architecture config. The plot shown for each model represents the loss at every learning rate value. The rule of thumb is to take the value on which the loss has been steadily decreasing and not yet reach the minimum."""

# configurations building block
base = {
    "word_input_dim": len(corpus.word_field.vocab),
    "char_pad_idx": corpus.char_pad_idx,
    "word_pad_idx": corpus.word_pad_idx,
    "tag_names": corpus.tag_field.vocab.itos,
    "device": use_device
}
w2v = {
    "word_emb_pretrained": corpus.word_field.vocab.vectors if corpus.wv_model else None
}
cnn = {
    "use_char_emb": True,
    "char_input_dim": len(corpus.char_field.vocab),
    "char_emb_dim": 37,
    "char_emb_dropout": 0.25,
    "char_cnn_filter_num": 4,
    "char_cnn_kernel_size": 3,
    "char_cnn_dropout": 0.25
}
attn = {
    "attn_heads": 16,
    "attn_dropout": 0.25
}
transformer = {
    "model_arch": "transformer",
    "trf_layers": 2,
    "fc_hidden": 256,
}
configs = {
    "bilstm": base,
    "bilstm+w2v": {**base, **w2v},
    "bilstm+w2v+cnn": {**base, **w2v, **cnn},
    "bilstm+w2v+cnn+attn": {**base, **w2v, **cnn, **attn},
    "transformer+w2v+cnn": {**base, **transformer, **w2v, **cnn, **attn}
}
search_space = {
    "bilstm": (1e-5, 10),
    "bilstm+w2v": (1e-5, 10),
    "bilstm+w2v+cnn": (1e-5, 2),
    "bilstm+w2v+cnn+attn": (1e-5, 0.2),
    "transformer+w2v+cnn": (1e-6, 0.2)
}
for model_name in configs:
    print(f"Begin LR Finder for model: {model_name}")
    model = NERModel(**configs[model_name])
    start_lr, end_lr = search_space[model_name]
    lr_finder = LRFinder(model, Adam(model.parameters(), lr=start_lr, weight_decay=1e-2), device=use_device)
    lr_finder.range_test(corpus.train_iter, corpus.val_iter, end_lr=end_lr, num_iter=55, step_mode="exp", diverge_th=3, disable_progress_bar=True)
    lr_finder.plot(skip_start=10, skip_end=0, suggest_lr=False)

# New initial learning rate
lrs = {
    "bilstm": 1e-2,
    "bilstm+w2v": 1e-2,
    "bilstm+w2v+cnn": 3e-3,
    "bilstm+w2v+cnn+attn": 3e-3,
    "transformer+w2v+cnn": 4e-4
}
max_epochs = 50
no_improvement = 10
histories = {}
for model_name in configs:
    print(f"Start Training: {model_name}")
    model = NERModel(**configs[model_name])
    trainer = Trainer(
        model=model,
        data=corpus,
        optimizer=Adam(model.parameters(), lr=lrs[model_name], weight_decay=1e-2),  # add weight decay for Adam
        device=use_device,
        checkpoint_path=f"{DRIVE_ROOT}/models/{model_name}.pt"
    )
    histories[model_name] = trainer.train(max_epochs, no_improvement)
    print(f"Done Training: {model_name}")
    print()

for model_name in configs:
    print(f"Sample inferences for model: {model_name}")
    trainer.model = NERModel(**configs[model_name]).to(use_device)
    trainer.model.load_state(f"{DRIVE_ROOT}/models/{model_name}.pt")
    # https://regional.kompas.com/read/2020/07/12/15554711/diduga-terlibat-perselingkuhan-ketua-kpu-sumba-barat-diberhentikan
    sentence = "\"Menjatuhkan sanksi pemberhentian tetap kepada teradu Sophia Marlinda Djami selaku Ketua KPU Kabupaten Sumba Barat, sejak dibacakannya putusan ini\", ucap Alfitra dalam sidang putusan, Rabu (8/7/2020)."
    tags = ["O", "O", "O", "O", "O", "O", "O", "B-PERSON", "I-PERSON", "L-PERSON", "O", "O", "B-ORGANIZATION", "I-ORGANIZATION", "I-ORGANIZATION", "L-ORGANIZATION", "O", "O", "O", "O", "O", "O", "O", "O", "U-PERSON", "O", "O", "O", "O", "B-TIME", "I-TIME", "I-TIME", "I-TIME", "I-TIME", "I-TIME", "I_TIME", "L-TIME", "O"]
    words, infer_tags, unknown_tokens = trainer.infer(sentence=sentence, true_tags=tags)
    print()
    # https://regional.kompas.com/read/2020/07/15/16583081/banjir-bandang-di-masamba-19-korban-meninggal-23-hilang-15000-mengungsi
    sentence = "Sementara itu, Kepala Pelaksana BPBD Luwu Utara Muslim Muchtar mengatakan, terdapat 15.000 jiwa mengungsi akibat banjir bandang."
    tags = ["O", "O", "O", "O", "O", "B-ORGANIZATION", "I-ORGANIZATION", "L-ORGANIZATION", "B-PERSON", "L-PERSON", "O", "O", "O", "U-QUANTITY", "O", "O", "O", "O", "O", "O"]
    words, infer_tags, unknown_tokens = trainer.infer(sentence=sentence, true_tags=tags)
    print()

max_len_model_name = max([len(m) for m in histories])
print(f"{'MODEL NAME'.ljust(max_len_model_name)}\t{'NUM PARAMS'.ljust(10)}\tTRAINING TIME")
for model_name, history in histories.items():
    print(f"{model_name.ljust(max_len_model_name)}\t{history['num_params']:,}\t{int(history['elapsed_train_time']//60)}m {int(history['elapsed_train_time'] % 60)}s")

model_name = "bilstm"
val_loss1 = histories[model_name]["val_loss"]
val_loss2 = histories["bilstm+w2v"]["val_loss"]
fig, axs = plt.subplots(2, 1, figsize=(15, 12))
for model_name in histories:
    axs[0].plot(histories[model_name]["val_loss"], label=model_name)
    axs[1].plot(histories[model_name]["val_f1"], label=model_name)
_ = axs[0].set_title("Val Loss")
_ = axs[1].set_title("Val F1")
_ = axs[1].set_xlabel("epochs")
_ = axs[0].set_ylabel("loss")
_ = axs[1].set_ylabel("F1")
_ = axs[0].legend(loc="upper right")
_ = axs[1].legend(loc="lower right")

model_test_f1 = [(m, histories[m]["test_f1"]) for m in histories]
model_test_f1_sorted = sorted(model_test_f1, key=lambda m: m[1])
model_names = [m[0] for m in model_test_f1_sorted]
y_pos = list(range(len(model_names)))
f1_scores = [m[1] for m in model_test_f1_sorted]
fig, ax = plt.subplots()
_ = ax.barh(y_pos, f1_scores, align='center')
_ = ax.set_yticks(y_pos)
_ = ax.set_yticklabels(model_names)
_ = ax.set_title("Test F1")

"""# Squeezing the last bit

The improvement from the unoptimized models are not substantial based on the Test F1 scores. The BiLSTM models are still better then the transformer-based model. However, if you check the validation loss plot above, all models are showing an indication of overfitting except the transformer model because the loss start to increase again after it reaches the minimum value. In fact, if you compare the inference samples, it seems the transformer model provides automatic labels that make more sense than the BiLSTM ones.

I have to mention that this overfitting symptom should have been addressed with early stopping too. In a sense, the training should be stopped when the validation loss starts to climb again. I did not implement early stopping as such to keep consistency: the F1 score is the single primary metric for measuring the model performance. Taking multiple metrics into account for model comparison is a dilemma that is often overlooked.

There are various techniques to reduce overfitting: more rigorous regularization, reducing the model complexity, or simply collect more data. After all, I have only tried to optimize one hyperparameter and have not touched the model architectural hyperparameters. Can we get significantly better performance if we play around with other hyperparameters? Or is it better to label more text for training?

I leave those questions unanswered for now.
Thank you for reading up to this point!

Any comments are welcome. Find me on Twitter: [@yoseflaw](https://twitter.com/yoseflaw).
"""