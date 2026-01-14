#!/usr/bin/env python3

import socket

def start_udp_client():
    host = '127.0.0.1'
    port = 1235

    #UDP
    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
        message = "Hola, aqui estamos tensinggg".encode("utf-8")
        s.sendto(message, (host,port))

start_udp_client()
