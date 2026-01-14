#!/usr/bin/env python3

from concurrent.futures import ThreadPoolExecutor
import argparse
from termcolor import colored
import subprocess
import signal
import time
import sys


def def_handler(sig, frame):
    print(colored(f"\n[!] Saliendo del programa...\n", "red"))
    sys.exit(1)

signal.signal(signal.SIGINT, def_handler)

def get_arguments():
    parser = argparse.ArgumentParser(description="Herrmienta para descubrir hosts activos en una red ICMP")
    parser.add_argument("-t", "--target", required=True, dest="target", help="Host o rango de red a escanear")

    args = parser.parse_args()

    return args

def parse_target(target_str):
    direcciones = []
    target_str_splited = target_str.split('.') # 192.128.1.1-100
    first_three_octets = '.'.join(target_str_splited[:3]) # 192.128.1

    if len(target_str_splited) == 4:
        if "-" in target_str_splited[3]:
            range_numbers = target_str_splited[3].split('-')
            first_number = int(range_numbers[0])
            end_number = int(range_numbers[1])+1
            for i in range(first_number, end_number):
                direcciones.append(f"{first_three_octets}.{i}")
            return direcciones
        else:
            return [target_str]
    else:
        print(colored(f"\n[+] Has introducido mal el host", "red"))

def host_discovery(target):
    try:
        ping = subprocess.run(["ping", "-c", "1", target], timeout=1, stdout=subprocess.DEVNULL)

        if ping.returncode == 0:
            print(colored(f"\n[i] La IP {target} esta activa", "green"))
    except subprocess.TimeoutExpired:
        pass

def main():
    args = get_arguments()
    target_str = args.target
    targets = parse_target(target_str)
    print("\n[H] ---HOST ACTIVOS EN LA RED---\n")
    max_threads = 100
    #manejadores de contexto
    with ThreadPoolExecutor(max_workers=max_threads) as executor:
        executor.map(host_discovery, targets)

if __name__ == '__main__':
    main()
