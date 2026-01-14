#!/usr/bin/env python3

from mitmproxy import http
from mitmproxy import ctx

def request(packet):
    ctx.log.info(f"[+] URL: {packet.request.url}\n\n")


def response(packet):
    ctx.log.info(f"[+] Response: {packet.request.url}\n\n")
