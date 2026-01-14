#!/usr/bin/env python3

import scapy.all as scapy
import argparse



def get_arguments():
    parser = argparse.ArgumentParser(description="ARP Scanner")
    parser.add_argument("-t","--target", required=True, help="Host / IP Range to Scan")

    args = parser.parse_args()

    return args.target


def scan(ip):
    #scapy.arping(ip)
    #Peticion ARP capa 3.5
    arp_p = scapy.ARP(pdst=ip)
    #Broadcast Ethernet capa 2
    broadcast_packet = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
    #Fusionar capas
    arp_p = broadcast_packet / arp_p

    answered, unanswered = scapy.srp(arp_p, timeout=1, verbose=False)

    #response = answered.summary()

    for sent, received in answered:
        print(received.psrc, received.hwsrc)

def main():
    target = get_arguments()
    scan(target)

if __name__ == '__main__':
    main()
