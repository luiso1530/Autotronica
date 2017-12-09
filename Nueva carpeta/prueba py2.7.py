import demjson

data = [ { 'a' : 1, 'b' : 2, 'c' : 3, 'd' : 4, 'e' : 5 } ]
data= demjson.encode(data)
print data
##
##import httplib
##conn = httplib.HTTPSConnection('www.api.ocpp.conectaev.com')
##conn.connect()
##request = conn.putrequest('POST', '/api/snippet/')
##headers = {}
##headers['Content-Type'] = 'application/json'
##for k in headers:
##    conn.putheader(k, headers[k])
##conn.endheaders()
##conn.request("GET", "/")
##r1 = conn.getresponse()
##print r1.status, r1.reason
##data1 = r1.read()
##conn.request("GET", "/")
##r2 = conn.getresponse()
##print r2.status, r2.reason
##data2 = r2.read()
##conn.send(data)
##r3 = conn.getresponse()
##print r3.status, r3.reason
##conn.close()

import httplib
import base64
import ssl

conn = httplib.HTTPSConnection('www.api.ocpp.conectaev.com') 
conn._context.check_hostname = False 
conn._context.verify_mode = ssl.CERT_NONE

headers = {}
headers['Authorization'] = \
    "Basic %s" % base64.standard_b64encode("admin:ibm")
req = conn.request('GET', ' ', headers=headers)
res = conn.getresponse()
conn.connect()
conn.send(data)

print res.read()

conn.close()
