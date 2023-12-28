from time import sleep
import threading 
import socket
import logging

# obj 
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
addr = ('localhost', 9090)

try:
    server.bind(addr)
except AddressAlreadyInUse as err:
    server.close()
    logging.error("Port already use:")
server.listen(5)
