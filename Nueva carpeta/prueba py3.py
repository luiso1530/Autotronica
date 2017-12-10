import requests
import demjson
import json

data = [ { 'a' : 1, 'b' : 2, 'c' : 3, 'd' : 4, 'e' : 5 } ]
envio= demjson.encode(data)
print( data)
m=requests.post('https://www.api.ocpp.conectaev.com',data=envio)
with open("json/Authorize.json")as file:        #funcion encargada de enviar 
    data = json.load(file)       #el idTag para autorizar el 
    idTag=123456
    data["idTag"]=idTag                          #uso del punto de recarga
    print (data["idTag"])  #prueba                 #retorna la respuesta del servidor
    print ("...............AUTHORIZE....................")
    send=demjson.encode(data)
m=requests.post('https://www.api.ocpp.conectaev.com',data=send)
