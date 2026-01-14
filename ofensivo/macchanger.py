#!/usr/bin/env python3

import argparse
import re
import subprocess
from termcolor import colored


def get_arguments():
    parser = argparse.ArgumentParser(description="Herramienta para cambiar la direccion de MAC de una interfaz de red")
    parser.add_argument("-i", "--interface", required=True, dest="interface", help="Nombre de la interfaz de red")
    parser.add_argument("-m", "--mac", required=True, dest="mac_addres", help="Nueva direccion MAC para la interfaz de red")

    return parser.parse_args()

def is_valid_input(interface, mac_address):
    is_valid_interface = re.match(r'^(en(p\d+s\d+|s\d+)|eth\d+)$', interface)
    is_valid_mac_addres= re.match(r'^([A-Fa-f0-9]{2}[:]){5}[A-Fa-f0-9]{2}$', mac_address)
    print(is_valid_interface)
    return is_valid_interface and is_valid_mac_addres

def change_mac_addres(interface, mac_address):

    if is_valid_input(interface, mac_address):
        subprocess.run(["ifconfig", interface, "down"])
        subprocess.run(["ifconfig", interface, "hw", "ether", mac_address])
        subprocess.run(["ifconfig", interface, "up"])
        print(colored("\n[+] La MAC ha sido cambiada correctamente", "green"))
    else:
        print(colored("\n[!] La MAC no ha sido cambiada", "red"))


def main():

    args = get_arguments()

    print(colored(f"\n[+] La interfaz -> {args.interface}", "yellow"))
    print(colored(f"\n[+] La mascara de red -> {args.mac_addres}", "yellow"))
    change_mac_addres(args.interface, args.mac_addres)
if __name__ == '__main__':
    main()
