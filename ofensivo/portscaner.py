#!/usr/bin/env python3

import socket
import argparse
from termcolor import colored
import sys
import pdb

def get_arguments():
    parser = argparse.ArgumentParser(description="Fast TCP Port Scanner")
    parser.add_argument("-t", "--target", dest="target", help="Victim target to scan(Ex: -t 192.168.1.189)")
    parser.add_argument("-p", "--port", dest="port", help="Port range to scan(Ex: -p 1-100)")
    options = parser.parse_args()

    if options.target is None or options.port is None:
        parser.print_help()
        print(colored("\n[!] No se ha proporcionado el target", "red"))
        sys.exit(1)
    return options.target, options.port


def create_socket():
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(1)
    return sock

def port_scanner(port, host, sock):
    try:
        result = sock.connect_ex((host, port))
        if result == 0:
            print(colored(f"\n[+] El puerto {port}, esta abierto", 'green'))
        sock.close()
    except (socket.timeout, ConnectionRefusedError):
        sock.close()

def main():

    target, port = get_arguments()

    if '-' in port:
        ports = port.split('-')
        start_port = int(ports[0])
        end_port = int(ports[1])+1

        for port in range(start_port, end_port):
            #pdb.set_trace()
            sock = create_socket()
            port_scanner(port,target,sock)

    elif ',' in port:
        ports = port.split(',')
        for port in ports:
            sock = create_socket()
            port_scanner(int(port), target, sock)

    else:
       socket = create_socket()
       port_scanner(int(port), target, socket)

if __name__ == '__main__':
    main()
