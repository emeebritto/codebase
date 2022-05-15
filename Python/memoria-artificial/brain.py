from chatterbot import ChatBot
# from chatterbot.trainers import ChatterBotCorpusTrainer
from chatterbot.trainers import ListTrainer
from gtts import gTTS
import playsound
import os

chatbot = ChatBot('ubi')
# Create a new trainer for the chatbot
# trainer = ChatterBotCorpusTrainer(chatbot)

trainer = ListTrainer(chatbot)

# Train the chatbot based on the portuguese corpus
# trainer.train("chatterbot.corpus.portuguese")

trainer.train([
    "Oi",
    "Oi",
    "Tudo bem?",
    "Estou bem",
    "Você é real?",
    "Nunca me senti tão viva"
])


def falar(texto):
    sintese = gTTS(texto, lang='pt', slow=False)
    arq = os.path.join(os.getcwd(), 'fala.mp3')
    sintese.save(arq)
    playsound.playsound(arq)

while True:
    request = input("Você: ")
    response = chatbot.get_response(request)
    voz = str(response)
    falar(voz)
    print("Ubi: ", voz)


