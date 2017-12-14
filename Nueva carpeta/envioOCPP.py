import requests
import demjson

buff=[]

def envio(data,HTTPdir):
	envio= demjson.encode(data)
	m=requests.post(HTTPdir,data=envio)
	print("enviado")

def buffering(new):
	buff.append(new)
	print(buff)
	return buff

def SBuffering(send,HTTPfdir):
	envio(send,HTTPfdir)
	buff=[]
	print("buffer vaciado")
