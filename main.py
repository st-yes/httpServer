import socket
import threading
import sys
from handler import *

PORT = 4221
HOST = "127.0.0.1"

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