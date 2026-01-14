#!/usr/bin/env python3
import netfilterqueue

def process_packet(packet):
    packet.accept()

queue = netfilterqueue.NetfilterQueue()
queue.bind(0, process_packet)
queue.run()
