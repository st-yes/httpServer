
import os

def getContentOfFile(filename):
    with open(filename, "r") as fd:
        body = fd.read()
    return body

def extractBody(lines, directory):
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
                body = getContentOfFile(filename)
                return body, 200, "application/octet-stream"
            else:
                return None, 404, None          
        elif secondItem[0] == "/":
            if len (secondItem) == 1:
                filename = "./htdocs/" + "index.html"
                if (os.path.isfile(filename) == True):
                    body = getContentOfFile("./htdocs/" + "index.html")
                else:
                    return None, 404, None
                return body, 200, "text/html"
            else:
                filename = "./htdocs/" + secondItem[1:]
                if (os.path.isfile(filename) == True):
                    body = getContentOfFile(filename)
                else:
                    return None, 404, None
                if (filename[-4:] == '.css'):
                    return  body, 200, "text/css"
                else:
                    return  body, 200, "text/html"
        else:
            return None, 404, None
    elif method == 'POST':
        filename = secondItem[7:]
        filename = directory + '/' + filename
        body = lines[6]
        with open(filename, "w") as fd:
            fd.write(body)
        return None, 201, None
        


# def extractRandomStr(lines, directory):
#     firstLine = lines[0]
#     listSplitBySpace = firstLine.split()
#     method = listSplitBySpace[0]
#     secondItem = listSplitBySpace[1]
    
#     if method == 'GET':
#         if (secondItem[:6] == "/echo/"):
#             randStr = secondItem[6:]
#             return randStr, 200, None
#         elif (secondItem == "/user-agent"):
#             userAgentLine = lines[2].split()
#             return userAgentLine[1], 200, None 
#         elif (secondItem[:7] == "/files/"):
#             filename = secondItem[7:]
#             filename = directory + '/' + filename
#             if (os.path.isfile(filename) == True):
#                 with open(filename, "r") as fd:
#                     body = fd.read()
#                 return body, 200, "application/octet-stream"
#             else:
#                 return None, 404, None          
#         elif secondItem == "/":
#             return None, 200, None
#         else:
#             return None, 404, None
#     elif method == 'POST':
#         filename = secondItem[7:]
#         filename = directory + '/' + filename
#         body = lines[6]
#         with open(filename, "w") as fd:
#             fd.write(body)
#         return None, 201, None
        
