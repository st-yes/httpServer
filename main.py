import socket
import threading
import sys
import os

PORT = 4221
HOST = "127.0.0.1"

def extractPath(theString):
    return theString.split()

def extractRandomStr(lines, directory):
    firstLine = lines[0]
    listSplitBySpace = firstLine.split()
    method = listSplitBySpace[0]
    secondItem = listSplitBySpace[1]
    
    if method == 'GET':
        if (secondItem[:6] == "/echo/"):
            randStr = secondItem[6:]
            return randStr, 200, None
        elif (secondItem == "/user-agent"):
            userAgentLine = lines[2].split()
            return userAgentLine[1], 200, None 
        elif (secondItem[:7] == "/files/"):
            filename = secondItem[7:]
            filename = directory + '/' + filename
            if (os.path.isfile(filename) == True):
                with open(filename, "r") as fd:
                    body = fd.read()
                return body, 200, "application/octet-stream"
            else:
                return None, 404, None          
        elif secondItem == "/":
            return None, 200, None
        else:
            return None, 404, None
    elif method == 'POST':
        filename = secondItem[7:]
        filename = directory + '/' + filename
        body = lines[6]
        with open(filename, "w") as fd:
            fd.write(body)
        return None, 201, None
        


def getLines(data):
    return (data.split('\r\n'))

def createResponse(responseN, randStr, type="text/plain"):
    crln = "\r\n"
    if randStr != None:
        return (responseN + crln + "Content-Type: "+ type + crln + "Content-Length: " + str(len(randStr)) + crln + crln + randStr + crln)
    else:
        return (responseN + crln + crln)

def clientHandler(client_socket, directory):
    response200 = "HTTP/1.1 200 OK"
    response404 =  "HTTP/1.1 404 Not Found"
    response201 = "HTTP/1.1 201 Created"
    data = client_socket.recv(1024)
    if (data):
        print(data.decode('utf-8'))
        dataList = getLines(data.decode('utf-8'))
        randStr, httpCode, thetype = extractRandomStr(dataList, directory)
        if (httpCode == 200):
            responseN = response200
        elif (httpCode == 201):
            responseN = response201
        else:
            responseN = response404
        if (thetype != None):
            theResponse = createResponse(responseN, randStr, thetype)
        else:
            theResponse = createResponse(responseN, randStr)
        client_socket.send(theResponse.encode('utf-8'))
    client_socket.close()


def main():
    try:
        directory = sys.argv[2]
    except:
        directory = ""
    server_socket = socket.create_server((HOST, PORT))
    print("SOCKET LISTENING ON PORT: {}".format(PORT))
    while True:
        client_socket, client_address = server_socket.accept()
        print("accepted connection from {} {}".format(*client_address))
        client_handler = threading.Thread(target=clientHandler, args=(client_socket, directory))
        client_handler.start()


if __name__ == "__main__":
    main()
