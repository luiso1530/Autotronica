import requests
import demjson

data = [ { 'a' : 1, 'b' : 2, 'c' : 3, 'd' : 4, 'e' : 7 },{ 'a' : 1, 'b' : 2, 'c' : 3, 'd' : 4, 'e' : 8 } ]
envio= demjson.encode(data)
print( data)
print(envio)
m=requests.post('https://www.api.ocpp.conectaev.com',data=envio)
