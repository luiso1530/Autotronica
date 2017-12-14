import requests
import demjson
import envioOCPP as env

buff=[]

#env.setdir('https://www.api.ocpp.conectaev.com')
buff=env.buffering({ 'a' : 1, 'b' : 2, 'c' : 3, 'd' : 4, 'e' : 7 })
buff=env.buffering({ 'a' : 8, 'b' : 9, 'c' : 10, 'd' : 11, 'e' : 12 })
env.SBuffering(buff,'https://www.api.ocpp.conectaev.com')


