#!/usr/bin/env python3

import scapy.all as scapy

def process(packet):
    if packet.haslayer(scapy.DNSQR):
        domain = packet[scapy.DNSQR].qname.decode()

        ex_keywords = ["google","bing","cloud","static", "secure", "fonts"]
        if (domain not in domains_seen) and (not any(keyword in domain for keyword in ex_keywords)):
            domains_seen.add(domain)
            print(f"[+] Dominio: {domain}")
def main():
    global domains_seen
    domains_seen = set()
    interface = "enp0s3"
    print(f"\n[+] Interceptando paquetes de la maquina vicitima:\n")
    scapy.sniff(iface=interface, filter="udp and port 53", prn=process, store=0)


if __name__ == '__main__':
    main()
