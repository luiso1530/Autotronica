#funciones cargador
import websocket #libreria externa para manejo de datos por web socket
import json      #libreria nativa de python para manejo de archivos json


def web_send(data):
    ws = websocket.WebSocket()              #funcion encargada de enviar datos 
    ws.connect("ws://demos.kaazing.com/echo")      #mediante websockets
    ws.send(data)
    result = ws.recv()
    print (result)#prueba
    print ("...................................")
    return result

def Authorize_req(idTag):
    with open("json/Authorize.json")as file:        #funcion encargada de enviar 
       data = json.load(file)                       #el idTag para autorizar el 
       data["idTag"]=idTag                          #uso del punto de recarga
       print data["idTag"]  #prueba                 #retorna la respuesta del servidor
       print ("...............AUTHORIZE....................")
       send=json.dumps(data)
       web_send(send)
    
def StartTransaction_req(connectorId, idTag, meterStart, timestamp, reservationId):
    with open("json/StartTransaction.json")as file:
        data = json.load(file)
        data["connectorId"]=connectorId
        data["idTag"]=idTag
        data["meterStart"]=meterStart
        data["timestamp"]=timestamp
        data["reservationId"]=reservationId
        print(data["connectorId"],data["idTag"],data["meterStart"],data["timestamp"],data["reservationId"])
        print ("............STARTTRANSACTION.......................")
        send=json.dumps(data)
        web_send(send)
        return data

#se encarga de informar al servidor que la carga inicio asi como los parametros requeridos
