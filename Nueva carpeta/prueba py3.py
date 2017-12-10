import requests
import demjson

data = [ { 'a' : 1, 'b' : 2, 'c' : 3, 'd' : 4, 'e' : 5 } ]
envio= demjson.encode(data)
print( data)
m=requests.post('https://www.api.ocpp.conectaev.com',data=envio)
