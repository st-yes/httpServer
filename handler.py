from parsing import *
import sys

CRLN = "\r\n"

def extractPath(theString):
    return theString.split()

def getLines(data):
    return (data.split('\r\n'))

def createResponse(responseN, randStr, type="text/plain"):
    if randStr != None:
        return (responseN + CRLN + "Content-Type: " + type + CRLN + "Content-Length: " + str(len(randStr)) + crln + crln + randStr + crln)
    else:
        return (responseN + CRLN + CRLN)

def createClassicResponse(responseN, body, type):
    return (responseN + CRLN + "Content-Type: " + type + CRLN + CRLN + body + CRLN)

def respFromStatusCode(code):
    if code == 200:
        response = "HTTP/1.1 200 OK"
    elif code == 404:
        response = "HTTP/1.1 404 Not Found"
    elif code == 201:
        response = "HTTP/1.1 201 Created"
    return response
        
    
def clientHandler(client_socket, directory):
    data = client_socket.recv(1024)
    if (data):
        print(data.decode('utf-8'))
        dataList = getLines(data.decode('utf-8'))
        body, httpCode, theType = extractBody(dataList, directory)
        responseN = respFromStatusCode(httpCode)
        if theType == "text/html" or theType == "text/css":
            theResponse = createClassicResponse(responseN, body, theType)
        else:
            theResponse = createResponse(responseN, body)
        client_socket.send(theResponse.encode('utf-8'))
    client_socket.close()