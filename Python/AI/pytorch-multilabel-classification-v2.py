#Import suppporting libraries
import tarfile
import urllib.request as urllib2
import os
from os import listdir
from os.path import isfile, join
import re
#Import deep learning libraries
import torch
import torch.nn as nn
import torch.nn.functional as F
from torch.utils.data import Dataset, DataLoader
import torchvision
from torchvision import datasets, transforms, models
import torchvision.models as models
#Import data analytics libraries
import matplotlib.pyplot as plt
import matplotlib.image as img
import numpy as np
import scipy.io
import pandas as pd
import seaborn as sns
#Import image visualization libraries
from PIL import *
from PIL import ImageFile
from PIL import Image
#System settings
ImageFile.LOAD_TRUNCATED_IMAGES = True
os.environ['WANDB_CONSOLE'] = 'off'
#Coloring for print outputs
class color:
	RED = '\033[91m'
	BOLD = '\033[1m'
	END = '\033[0m'

def getting_data(url,path):
	data = urllib2.urlopen(url)
	tar_package = tarfile.open(fileobj=data, mode='r:gz')
	tar_package.extractall(path)
	tar_package.close()
	return print("Data extracted and saved.")

# getting_data("http://ai.stanford.edu/~jkrause/car196/car_ims.tgz","/content/carimages")

def getting_metadata(url,filename):
	'''
	Downloading a metadata file from a specific url and save it to the disc.
	'''
	labels = urllib2.urlopen(url)
	file = open(filename, 'wb')
	file.write(labels.read())
	file.close()
	return print("Metadata downloaded and saved.")

# getting_metadata("http://ai.stanford.edu/~jkrause/car196/cars_annos.mat","car_metadata.mat")

class MetaParsing():
	'''
	Class for parsing image and meta-data for the Stanford car dataset to create a custom dataset.
	path: The filepah to the metadata in .mat format.
	*args: Accepts dictionaries with self-created labels which will be extracted from the metadata (e.g. {0: 'Audi', 1: 'BMW', 3: 'Other').
	year: Can be defined to create two classes (<=year and later).
	'''
	def __init__(self,path,*args,year=None):
		self.mat = scipy.io.loadmat(path)
		self.year = year
		self.args = args
		self.annotations = np.transpose(self.mat['annotations'])
		#Extracting the file name for each sample
		self.file_names = [annotation[0][0][0].split("/")[-1] for annotation in self.annotations]
		#Extracting the index of the label for each sample
		self.label_indices = [annotation[0][5][0][0] for annotation in self.annotations]
		#Extracting the car names as strings
		self.car_names = [x[0] for x in self.mat['class_names'][0]]
		#Create a list with car names instead of label indices for each sample
		self.translated_car_names = [self.car_names[x-1] for x in self.label_indices]
	def brand_types(self,base_dict, x):
		y = list(base_dict.keys())[-1]
		for k,v in base_dict.items():
			if v in x: y=k
		return y
	def parsing(self):
		result = []
		for arg in self.args:
			temp_list = [self.brand_types(arg,x) for x in self.translated_car_names]
			result.append(temp_list)
		if self.year != None:
			years_list = [0 if int(x.split(" ")[-1]) <= self.year else 1 for x in self.translated_car_names]
			result.append(years_list)
		brands = [x.split(" ")[0] for x in self.translated_car_names]
		return result, self.file_names, self.translated_car_names

brand_dict = {0: 'Audi', 1: 'BMW', 2: 'Chevrolet', 3: 'Dodge', 4: 'Ford', 5: 'Other'}
vehicle_types_dict = {0: 'Convertible', 1: 'Coupe', 2: 'SUV', 3: 'Van', 4: 'Other'}

results, file_names, translated_car_names = MetaParsing("/content/car_metadata.mat",brand_dict,vehicle_types_dict,year=2009).parsing()
# len(results)

def count_classes(base_dict, base_list):
	for i in range(len(list(base_dict.keys()))):
		print("{}: {}".format(base_dict[i], str(base_list.count(i))))

# count_classes(brand_dict,results[0])
# count_classes(vehicle_types_dict,results[1])

translation_dict = dict(zip(file_names,list(zip(results[0],results[1],results[2]))))

class CarDataset(Dataset):
	
	def __init__(self,car_path,transform,translation_dict):
		self.path = car_path
		self.folder = [x for x in listdir(car_path)]
		self.transform = transform
		self.translation_dict = translation_dict

	def __len__(self):
		return len(self.folder)

	def __getitem__(self,idx):
		img_loc = os.path.join(self.path, self.folder[idx])
		image = Image.open(img_loc).convert('RGB')
		single_img = self.transform(image)

		label1 = translation_dict[self.folder[idx]][0]
		label2 = translation_dict[self.folder[idx]][1]
		label3 = translation_dict[self.folder[idx]][2]

		sample = {'image':single_img, 'labels': {'label_brand':label1, 'label_vehicle_type':label2, 'label_epoch':label3}}
		return sample

#Pre-processing transformations
data_transforms = transforms.Compose([
	transforms.Resize((224,224)),
	transforms.ToTensor(),
	transforms.Normalize((0.5,0.5,0.5), (0.5,0.5,0.5))
])

#Getting the data
cardata = CarDataset("/content/carimages/car_ims", transform=data_transforms,translation_dict=translation_dict)

#Split the data in training and testing
train_len = int(cardata.__len__()*0.8)
test_len = int(cardata.__len__()*0.2)
train_set, val_set = torch.utils.data.random_split(cardata, [train_len, test_len])

#Create the dataloader for each dataset
train_loader = DataLoader(
	train_set,
	batch_size=16,
	shuffle=True,
	num_workers=4,
	drop_last=True
)
test_loader = DataLoader(
	val_set,
	batch_size=16,
	shuffle=False,
	num_workers=4,
	drop_last=True
)

sample = next(iter(train_loader))
print("Keys in our sample batch: {}".format(sample.keys()))
print("Size for the images in our sample batch: {}".format(sample['image'].shape))
print("Size for the target in our sample batch: {}".format(sample['labels']['label_brand'].shape))
print("Targets for each batch in our sample: {}".format(sample['labels']['label_brand']))

# resnet = models.resnet34(pretrained=True)
# list(resnet.children())[-3:]
# model_wo_fc = nn.Sequential(*(list(resnet.children())[:-1]))
# output_sample = model_wo_fc(sample['image'])
# print(output_sample.shape)
# print(torch.flatten(output_sample, 1).shape)

# output_sample_flatten = torch.flatten(output_sample, 1)
# brand = nn.Sequential(
# 	nn.Dropout(p=0.2),
# 	nn.Linear(in_features=512, out_features=6)
# )

# brand(output_sample_flatten).shape

class MultilabelClassifier(nn.Module):
	def __init__(self, n_brand, n_vehicle_type, n_epoch):
		super().__init__()
		self.resnet = models.resnet34(pretrained=True)
		self.model_wo_fc = nn.Sequential(*(list(self.resnet.children())[:-1]))

		self.brand = nn.Sequential(
			nn.Dropout(p=0.2),
			nn.Linear(in_features=512, out_features=n_brand)
		)
		self.vehicle_type = nn.Sequential(
			nn.Dropout(p=0.2),
			nn.Linear(in_features=512, out_features=n_vehicle_type)
		)
		self.epoch = nn.Sequential(
			nn.Dropout(p=0.2),
			nn.Linear(in_features=512, out_features=n_epoch)
		)

	def forward(self, x):
		x = self.model_wo_fc(x)
		x = torch.flatten(x, 1)

		return {
			'brand': self.brand(x),
			'vehicle_type': self.vehicle_type(x),
			'epoch': self.epoch(x)
		}

device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
model = MultilabelClassifier(6,5,2).to(device)

def criterion(loss_func,outputs,pictures):
	losses = 0
	for i, key in enumerate(outputs):
		losses += loss_func(outputs[key], pictures['labels'][f'label_{key}'].to(device))
	return losses

def training(model,device,lr_rate,epochs,train_loader):
	num_epochs = epochs
	losses = []
	checkpoint_losses = []

	optimizer = torch.optim.Adam(model.parameters(), lr=lr_rate)
	n_total_steps = len(train_loader)

	loss_func = nn.CrossEntropyLoss()

	for epoch in range(num_epochs):
		for i, pictures in enumerate(train_loader):
			images = pictures['image'].to(device)
			pictures = pictures

			outputs = model(images)

			loss = criterion(loss_func,outputs, pictures)
			losses.append(loss.item())

			optimizer.zero_grad()
			loss.backward()
			optimizer.step()

			if (i+1) % (int(n_total_steps/1)) == 0:
				checkpoint_loss = torch.tensor(losses).mean().item()
				checkpoint_losses.append(checkpoint_loss)
				print (f'Epoch [{epoch+1}/{num_epochs}], Step [{i+1}/{n_total_steps}], Loss: {checkpoint_loss:.4f}')
	return checkpoint_losses

checkpoint_losses = training(model,device,0.0001,10,train_loader)


def validation(model, dataloader, *args):

	all_predictions = torch.tensor([]).to(device)
	all_true_labels = torch.tensor([]).to(device)

	with torch.no_grad():
		n_correct = []
		n_class_correct = []
		n_class_samples = []
		n_samples = 0

		for arg in args:
			n_correct.append(len(arg))
			n_class_correct.append([0 for i in range(len(arg))])
			n_class_samples.append([0 for i in range(len(arg))])

		for pictures in dataloader:
			images = pictures['image'].to(device)
			outputs = model(images)
			labels = [pictures['labels'][picture].to(device) for picture in pictures['labels']]

			for i,out in enumerate(outputs):
				_, predicted = torch.max(outputs[out],1)
				n_correct[i] += (predicted == labels[i]).sum().item()

				if i == 0:
					n_samples += labels[i].size(0)

				for k in range(16):
					label = labels[i][k]
					pred = predicted[k]
					if (label == pred):
						n_class_correct[i][label] += 1
					n_class_samples[i][label] += 1
					
	return n_correct,n_samples,n_class_correct,n_class_samples

def class_acc(n_correct,n_samples,n_class_correct,n_class_samples,class_list):
		for i in range(len(class_list)):
			print("-------------------------------------------------")
			acc = 100.0 * n_correct[i] / n_samples
			print(color.BOLD + color.RED + f'Overall class performance: {round(acc,1)} %' + color.END)
			for k in range(len(class_list[i])):
					acc = 100.0 * n_class_correct[i][k] / n_class_samples[i][k]
					print(f'Accuracy of {class_list[i][k]}: {round(acc,1)} %')
		print("-------------------------------------------------")

classes_brand = list(brand_dict.values())
classes_vehicle_type = list(vehicle_types_dict.values())
classes_epoch = ['2009 and earlier','2010 and later']
class_list = [classes_brand,classes_vehicle_type,classes_epoch]

n_correct,n_samples,n_class_correct,n_class_samples = validation(model,test_loader,classes_brand,classes_vehicle_type,classes_epoch)

class_acc(n_correct,n_samples,n_class_correct,n_class_samples,class_list)