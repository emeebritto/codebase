# from googletrans import Translator
# import fileinput
# import requests
# import base64
# import os
# import json
# import re


# create a twitter thread about "deepfake in politics field" in portuguese

# # Import the Selenium WebDriver
# from selenium import webdriver

# # Create a new instance of the WebDriver
# driver = webdriver.Firefox()
# print("f")
# # Use the WebDriver to visit a web page
# driver.get("http://www.neblika.com")

# # Get the HTML of the page
# html = driver.page_source

# # Print the HTML to the console
# print(html)


#Y1q8uw2a%y0q4uw1a#r9

# ====================================================================
# ====================================================================

# import torch
# import torch.nn as nn
# import numpy as np


# model = nn.Linear(4, 4) # predict logits for 5 classes
# model.train()
# # x = torch.tensor([[1., 2.]])
# # y = torch.tensor([[3., 4.]]) # get classA and classC as active

# word_to_ix = {
# 	"house": 0,
# 	"horse": 1,
# 	"the": 2,
# 	"girl": 3,
# 	"is": 4,
# 	"run": 5,
# 	"running": 6,
# 	"the": 7,
# 	"man": 8,
# 	"yet": 9,
# 	"your": 10,
# 	"beautiful": 11,
# 	"paulo": 12,
# 	"at": 13,

# 	"home": 14
# }

# dataset = [
#   [torch.tensor([7., 3., 4., 6.]), torch.tensor([0., 1., 0., 0.])],
#   [torch.tensor([8., 4., 6., 9.]), torch.tensor([1., 0., 0., 0.])],
#   [torch.tensor([3., 4., 6., 9.]), torch.tensor([1., 0., 0., 0.])],
#   [torch.tensor([10., 0., 4., 11.]), torch.tensor([0., 1., 0., 0.])]
# ]

# # print(dir(nn))
# criterion = nn.BCEWithLogitsLoss()
# optimizer = torch.optim.SGD(model.parameters(), lr=1e-1, weight_decay=1e-4)

# for epoch in range(30):
#   for data in dataset:
#     x = data[0]
#     y = data[1].to(dtype=torch.float)
#     optimizer.zero_grad()
#     # print("x", x)
#     # print("y", y)
#     output = model(x)
#     # print("output", output)
#     loss = criterion(output, y)
#     loss.backward()
#     optimizer.step()
#   print('Loss: {:.3f}'.format(loss.item()))

# model.eval()
# pred = data[0][0]
# output = model(torch.tensor([[12.,4.,6.,9.]]))
# print("output", output)
# output = torch.sigmoid(output)
# print("output", output)


# output = output.detach().cpu()
# print("output", output)
# sorted_indices = np.argsort(output)
# print("sorted_indices", sorted_indices)
# probs = torch.softmax(output, dim=0)
# print("probs", probs)


# =====================================================================
# TESTING GRADIO SPACE LOAD ===========================================

# import gradio as gr

# # io1 = gr.Interface.load("spaces/keras-io/question_answering")
# io1 = gr.Interface.load("spaces/emee/nexa", api_key="")
# def question_answering(value):
#   result = io1(value)
#   return result

# print(question_answering("what is the cat color ?"))

# =====================================================================
# TESTING SUBPROCESS ==================================================

# import subprocess
# def get_output(command):
#   print(command.split())
#   p = subprocess.Popen(command.split(), stdout=subprocess.PIPE)
#   out, err = p.communicate()
#   return out

# print(get_output("curl https://framely.vercel.app"))

# =====================================================================
# WALLPAPER CHANGER ===================================================


# pip install PyWallpaper
# from PyWallpaper import change_wallpaper
# image_path = "/home/emerson-britto/Desktop/whale-in-black-screen-hw0vglscjvlu6lr5.jpg"
# change_wallpaper(image_path)

# =====================================================================
# USING ULTRAMSG API ==================================================


# import requests
# url = "https://api.ultramsg.com/instance23218/messages/chat"
# payload = "token=z3a71cbl8dzf1evh&to=558184081096&body=test message;priority=1&referenceId="
# headers = {'content-type': 'application/x-www-form-urlencoded'}
# response = requests.request("POST", url, data=payload, headers=headers)
# print(response.text)


# =====================================================================
# USING PYWHATKIT =====================================================


# import pywhatkit

# pywhatkit.sendwhatmsg_instantly("+5573991973084", "Hello from pywhatkit")
# print("Successfully Sent!")


# =====================================================================
# SEARCH ON GOOGLE ====================================================


# from googlesearch import search
# print([*search("what is a apple?")])
# from googlesearch import search
# import requests
# from bs4 import BeautifulSoup

# def google_scrape(url):
#   thepage = requests.get(url).content
#   soup = BeautifulSoup(thepage, "html.parser")
#   print(soup.text)
#   print(dir(soup))
#   return soup.title.text

# query = 'what is a apple?'
# for url in search(query, 1):
#   a = google_scrape(url)
#   print(a)
#   print(url)
#   print(" ")


# ====================================================================
# FROM BINARY TO STRING VAR ==========================================


# file_target = "m.mp3"
# print(os.path.getsize(file_target))
# with open(file_target, "rb") as img_file:
#   my_string = base64.b64encode(img_file.read()).decode('utf-8')


# ====================================================================
# USING GRADIO =======================================================


# import gradio as gr

# def greet(uInput):
#   return "Hello " + uInput + "!", None, None, None

# demo = gr.Interface(fn=greet, inputs="text", outputs=["text", "image", "video", "audio"])

# demo.launch()


# ===================================================================
# TESTING LEXICA API ================================================


# session_token = "eyJhbGciOiJkaXIiLCJlbmMiOiJBMjU2R0NNIn0..FY11BxLiO4wmePcR.XpmdQddOhBfzwWDMqWCsXWXIZG0tvF7XWje-DkgR60yLnYHtw1Hq5j1dX7MKfOoEycd_dfL-ksornJqlAe_uniktUAucL35VBe9WE74NhElw37hohmJnYb4_9kTvcMmQce1liJVwBgowwh1QCjR58yilq_z8RNkeORThgsEt7HOqWCDU-RKnT10vCR3d559rzgwYklqIgObw_apNHLsk7FE6iFWMB7PLc7I8Nk789u2msKjtC2VxW_Jz7dXDQevADji3Co7OYaQK90ntSw.TU75VhuhNSCKYtsU8Zb2kQ"
# csrf_token = "49a50e269cb9495bf181506bbe16ec43c8c978f5eab696ec5a796d557208c99a%7C9d6f1d8d3b5fec3b12534aca5019bd9691a2ec993c23489d027a9e30f15157f3"


# result = requests.post("https://lexica.art/api/trpc/generator.generate?batch=1", headers={
#   "Host": "lexica.art",
#   "User-Agent": "Mozilla/5.0 (X11; Linux x86_64; rv:106.0) Gecko/20100101 Firefox/106.0",
#   "Accept": "*/*",
#   "Accept-Language": "en-US,en;q=0.5",
#   "Accept-Encoding": "gzip, deflate, br",
#   "Referer": "https://lexica.art/",
#   "content-type": "application/json",
#   "Content-Length": "173",
#   "Origin": "https://lexica.art",
#   "DNT": "1",
#   "Alt-Used": "lexica.art",
#   "Connection": "keep-alive",
#   "Cookie": f"__Host-next-auth.csrf-token={csrf_token}; __Secure-next-auth.callback-url=https://lexica.art/; __Secure-next-auth.session-token={session_token}",
#   "Sec-Fetch-Dest": "empty",
#   "Sec-Fetch-Mode": "cors",
#   "Sec-Fetch-Site": "same-origin",
#   "Sec-GPC": "1",
#   "Pragma": "no-cache",
#   "Cache-Control": "no-cache",
#   "TE": "trailers"
# }, data=json.dumps({
#   "0":{
#     "json":{
#       "prompt":"a girl",
#       "negative_prompt":"",
#       "guidance_scale":10,
#       "width":512,
#       "height":512,
#       "image_strength":30,
#       "randomizeSeed":True,
#       "init_image":"",
#       "seed":60073012
#     }
#   }

# }))
# matches = re.findall(r"<form id=\"challenge-form\" action=\"(.+)\" method=\"POST\"", str(result.content))
# api_path = matches[0]
# print("matches", matches[0])
# print("")
# print("")
# matches = re.findall(r"<input type=\"hidden\" name=\"md\" value=\"(.+)\">\\n            <input type=\"hidden\" name=\"r\"", str(result.content))
# md = matches[0]
# print("md", matches[0])
# print("")
# print("")
# matches = re.findall(r"<input type=\"hidden\" name=\"r\" value=\"(.+)\">\\n        </form>\\n    </div>", str(result.content))
# r = matches[0]
# print("r", matches[0])
# print("")
# print("")
# print(result.headers)
# print("")
# print("")
# print(result.content)
# # with open("res.html", "w") as file:
# #   file.write(str(result.content))
# print("")
# print("")
# # data = result.json()
# # print(data)

# print(md)
# print("")
# print("")
# print(r)

# result = requests.post(f"https://lexica.art{api_path}", headers={
#   "Host": "lexica.art",
#   "User-Agent": "Mozilla/5.0 (X11; Linux x86_64; rv:106.0) Gecko/20100101 Firefox/106.0",
#   "Accept": "*/*",
#   "Accept-Language": "en-US,en;q=0.5",
#   "Accept-Encoding": "gzip, deflate, br",
#   "Referer": "https://lexica.art/",
#   "content-type": "application/x-www-form-urlencoded",
#   "Content-Length": "173",
#   "Origin": "https://lexica.art",
#   "DNT": "1",
#   "Alt-Used": "lexica.art",
#   "Connection": "keep-alive",
#   "Cookie": f"__Host-next-auth.csrf-token={csrf_token}; __Secure-next-auth.callback-url=https://lexica.art/; __Secure-next-auth.session-token={md}",
#   "Sec-Fetch-Dest": "empty",
#   "Sec-Fetch-Mode": "cors",
#   "Sec-Fetch-Site": "same-origin",
#   "Sec-GPC": "1",
#   "Pragma": "no-cache",
#   "Cache-Control": "no-cache",
#   "TE": "trailers"
# }, data={
#   "md": md,
#   "r": r
# })

# print("")
# print(result.headers)
# print("")
# print("")
# print(result.content)


# =================================================================
# USING SOCKETIO ==================================================


# import socketio

# sio = socketio.Client()
# sio.connect("wss://stabilityai-stable-diffusion.hf.space", namespaces=["/queue/join"])


# =================================================================
# USING STABLE-DIFFUSION PIPELINE =================================


# from torch import autocast
# from diffusers import StableDiffusionPipeline

# pipe = StableDiffusionPipeline.from_pretrained(
#   "CompVis/stable-diffusion-v1-4", 
#   use_auth_token=True
# ).to("cuda")

# prompt = "a photo of an astronaut riding a horse on mars"
# with autocast("cuda"):
#     image = pipe(prompt)["sample"][0]  
		
# image.save("astronaut_rides_horse.png")


# ================================================================
# TESTING MOUSE TRACKER ==========================================


# import pyautogui, sys
# print('Press Ctrl-C to quit.')
# try:
#     while True:
#         x, y = pyautogui.position()
#         positionStr = 'X: ' + str(x).rjust(4) + ' Y: ' + str(y).rjust(4)
#         print(positionStr, end='')
#         print('\b' * len(positionStr), end='', flush=True)
# except KeyboardInterrupt:
#     print('\n')


# ===============================================================
# TESTING TRANSLATER SYSTEM + API ===============================


# last_request = ""
# text = ""
# while True:
#   translator = Translator()
#   uInput = input("you: ")
#   if not "rg" in uInput:
#     from_lang = 'pt'
#     to_lang = 'en'

#     text_to_translate = translator.translate(uInput, src=from_lang, dest=to_lang)
#     text = text_to_translate.text
#     last_request = text
#   else:
#     text = last_request

#   print("processing..")

#   data = requests.post("https://stabilityai-stable-diffusion.hf.space/api/predict/", headers={
#     "Host": "stabilityai-stable-diffusion.hf.space",
#     "User-Agent": "Mozilla/5.0 (X11; Linux x86_64; rv:106.0) Gecko/20100101 Firefox/106.0",
#     "Accept": "*/*",
#     "Accept-Language": "en-US,en;q=0.5",
#     "Accept-Encoding": "gzip, deflate, br",
#     "Referer": "https://stabilityai-stable-diffusion.hf.space/?__theme=light",
#     "Content-Type": "application/json",
#     "Content-Length": "53",
#     "Origin": "https://stabilityai-stable-diffusion.hf.space",
#     "DNT": "1",
#     "Connection": "keep-alive",
#     "Cookie": "session-space-cookie=e0d3de91a2173ae9a132d9fb287b13cb",
#     "Sec-Fetch-Dest": "empty",
#     "Sec-Fetch-Mode": "cors",
#     "Sec-Fetch-Site": "same-origin",
#     "Sec-GPC": "1",
#     "TE": "trailers"
#   }, data=json.dumps({
#     "fn_index":2,
#     "data":[text],
#     "advanced": {
#       "width": 450,
#       "height": 800,
#       "seed": 45,
#     },
#     "session_hash":"f0512fjdy27"
#   }))

#   # # with open("text.txt", 'w') as file:
#   # #   file.write(data["data"][0][0].replace("data:image/jpeg;base64,", ""))

#   # # # newjpgtxt = open("text.txt","rb").read()
#   data = data.json()
#   # print(data["data"][0])
#   for idx, img in enumerate(data["data"][0]):
#     with open(f"out_{idx}.jpeg", 'wb') as file:
#       base = img.replace("data:image/jpeg;base64,", "")
#       file.write(base64.decodebytes(bytes(base, "utf-8")))

#   print("image was generated")


# =============================================================
# TESTING BASE64 DECODER ======================================


# for index, line in enumerate(fileinput.input('text.txt'), 1):
#   with open('image{0:02}.jpg'.format(index), 'wb') as jpg:
#     line = line.strip()
#     jpg.write(base64.b64decode(line))



# recovered = base64.decodebytes(bytes(data["data"][0][0], 'utf-8'))
# print(recovered)
# with open("image.jpeg", 'wb') as file:
#   file.write(recovered)


# ============================================================
# TESTING GRPC SYSTEM ========================================


# from pyease_grpc import Protobuf, RpcSession
# from pyease_grpc.rpc_uri import RpcUri

# protobuf = Protobuf.from_file('test.proto')
# session = RpcSession(protobuf)

# response = session.request(
#     RpcUri('https://grpc.stability.ai/gooseai.GenerationService/Generate', service='TimeService', method='GetCurrentTime'),
#     {},
#     {
#       "Host": "grpc.stability.ai",
#       "User-Agent": "Mozilla/5.0 (X11; Linux x86_64; rv:106.0) Gecko/20100101 Firefox/106.0",
#       "Accept": "*/*",
#       "Accept-Language": "en-US,en;q=0.5",
#       "Accept-Encoding": "gzip, deflate, br",
#       "Referer": "https://beta.dreamstudio.ai/",
#       "authorization": "Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6IjlhUWoxMnpIUXdkN0VwY1h1dVhMeCJ9.eyJpc3MiOiJodHRwczovL3N0YWJpbGl0eWFpLnVzLmF1dGgwLmNvbS8iLCJzdWIiOiJhdXRoMHw2MzYzNTlkYWFkMzcwNzBhOGQ3NWI5MmYiLCJhdWQiOlsiaHR0cHM6Ly9zdGFiaWxpdHlhaS51cy5hdXRoMC5jb20vYXBpL3YyLyIsImh0dHBzOi8vc3RhYmlsaXR5YWkudXMuYXV0aDAuY29tL3VzZXJpbmZvIl0sImlhdCI6MTY2NzQ1NjEyMywiZXhwIjoxNjY3NTQyNTIzLCJhenAiOiJLdllaSktTaG1Vb09qWHBjbFFsS1lVeHVjQVZlc2xITiIsInNjb3BlIjoib3BlbmlkIHByb2ZpbGUgZW1haWwifQ.EsvDt4EIN_QtNNyCCzHowAld8MHQ-WtM7ekj3L1Rhwwit1Basmd1_XaLlkgyTO3e7s7t60jQOMafljDszugxGUWQPaFUxACgXMMG2sTQCtV8srhOmcwkHRe09j0tfEF6TsDkHJQyQWZ1n3aBT4v9Yk7p0Fou8v1B4Hv5xlj-SBWUBmPcZgVtgXWi3sZb1d6vZTC-Yjs6R2QpNPLlssMy9dRuxH0gnoenCqL8rn4raErFw28Uh_r-d6-6DBLDVqDyd0DPbMsQ_llDUWkPo_Q58rSA807z2Byha9IcuE5V_p3onUqhcD_dgkyDF6ai1ubYbvrk7dTJvmBU0bGXumOd8g",
#       "content-type": "application/grpc-web+proto",
#       "x-grpc-web": "1",
#       "Content-Length": "164",
#       "Origin": "https://beta.dreamstudio.ai",
#       "DNT": "1",
#       "Connection": "keep-alive",
#       "Sec-Fetch-Dest": "empty",
#       "Sec-Fetch-Mode": "cors",
#       "Sec-Fetch-Site": "cross-site",
#       "Sec-GPC": "1",
#       "Pragma": "no-cache",
#       "Cache-Control": "no-cache",
#       "TE": "trailers"
#     }
# )
# print(response)
# print(dir(response))
# response.raise_for_status()

# result = response.single
# print(result['currentTime'])


# ============================================================
# ============================================================