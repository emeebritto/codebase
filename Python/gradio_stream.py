import gradio as gr
from flask import Flask, Response, stream_with_context
from time import sleep


def main(text):
	def generate():
		for i in range(5):
			sleep(1)
			yield f"Data chunk {i}\n"

	text = "";
	for val in generate():
		text += val
		yield text

nx = gr.Interface(fn=main, inputs="text", outputs="text")
nx.queue()
nx.launch()
