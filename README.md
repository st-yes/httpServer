### Project description
a minimal http server to understand how does the http protocol work

### functionalities
handled methods:
- GET (ongoing)
- POST (ongoing)
- DELETE (Not yet)

- support multiple clients (concurrent connections)

###  brief about the HTTP Protocol
HTTP is the protocol that browsers use to retrieve and push information to servers.  
In its essence,  HTTP is text that follows a certain pattern and request-response rules:  
i.e: in a request coming from the browser(client), on the first line you specify which resource you want, then it follows the headers, and then you have a blank line that separates the headers from the body of the message (if any).

#### example of an http request
POST / HTTP/1.1 --> **first line**
content-length: 14 --> **start of headers**
accept-encoding: gzip, deflate, br
Accept: */*
User-Agent: Thunder Client (https://www.thunderclient.com)
Content-Type: application/json
Host: localhost:4221
Connection: close --> **end of headers**
                  --> **line consisting of "\r\n"**
this is a body    --> body of request

<img src= "https://www.aisangam.com/blog/wp-content/uploads/2019/10/HTTPRequestMessageFormat.png" width=500>
