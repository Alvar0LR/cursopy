#!/usr/bin/env python3

import argparse
import socket

def get_arguments():
    parser = argparse.ArgumentParser(description="=== TCP PORT CHECKER ===")
    parser.add_argument("-t", "--ip", required=True, help="IP to scan")
    parser.add_argument("-p", "--port", required=True, help="port to scan")

    args = parser.parse_args() # hasta aqui creo los parametros necesarios

    if args.ip is None or args.port is None:
        parser.print_help()
        print(f"\n[!] Inserte los parametros <ip> y <port> para completar el scan")
        # si no veo que el usuario ha introducido los parametros le aviso mandandole el mensaje de ayuda
    return args.ip, args.port
    # devuelvo los dos parametros creados

def create_socket():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(1)
    return s

def port_scanner(port, ip, sock):
    try:
        result_conection = sock.connect_ex((ip, port))
        if result_conection == 0: # si el resultado de la conexion es 0 es que estan abiertos
            print(f"\n[+] PORT {port} - OPEN")
        else:
            print(f"\n[-] PORT {port} - CLOSE") # si es distinto es que estan closed
        sock.close()
    except (socket.timeout, ConnectionRefusedError):
        sock.close()

def main():

    ip, port = get_arguments() # recojo los parametros

    if '-' in port: # si encuentro guion es que quiere un range desde el puerto indicado hasta el puerto que quiere encontrar 
        puertos = port.split('-') # si encuentro el giuon creo una lista con los dos numeros 
        n1 = int(puertos[0])
        n2 = int(puertos[1])+1
        # creo los limitantes del rango con los dos numeros
        for port in range(n1, n2):
            socket = create_socket()
            port_scanner(port, ip, socket) # me creo el socket y el puerto y la ip las paso al metodo para que se evalue el escaneo
    else:
        socket = create_socket()
        port_scanner(int(port), ip, socket)

if __name__ == '__main__':
    main()
