#!/usr/bin/env python3
from socket import *
from threading import Thread
from struct import pack
import time

def server():
    server = socket(AF_INET, SOCK_STREAM)
    server.setsockopt(SOL_SOCKET, SO_LINGER, pack('ii', 1, 0))
    server.bind(('0.0.0.0', 7000))
    while True:
        try:
            server.connect(('127.0.0.1', 8000))
            break
        except:
            time.sleep(0.01)
            pass
    
    buffer = server.recv(1024)
    print(buffer)
    server.send(b'Server say hello')
Thread(target=server).start()

def client():
    client = socket(AF_INET, SOCK_STREAM)
    client.setsockopt(SOL_SOCKET, SO_LINGER, pack('ii', 1, 0))
    client.bind(('0.0.0.0', 8000))
    while True:
        try:
            client.connect(('127.0.0.1', 7000))
            break
        except:
            time.sleep(0.01)
            pass
    
    client.send(b'Client say hi')
    buffer = client.recv(1024)
    print(buffer)
Thread(target=client).start()
