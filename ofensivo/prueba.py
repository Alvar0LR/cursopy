#!/usr/bin/env python3

import argparse
import socket
import subprocess
import sys

# -----------------------------
# Argumentos
# -----------------------------
def get_arguments():
    parser = argparse.ArgumentParser(description="Network Utility Tool")
    parser.add_argument("-t", "--target", required=True, help="IP o dominio objetivo")
    return parser.parse_args()

# -----------------------------
# Validar si es IP (lógica pura)
# -----------------------------
def is_ip(target):
    parts = target.split(".")

    # Una IP debe tener exactamente 4 partes
    if len(parts) != 4:
        return False

    for part in parts:
        # Cada parte debe ser numérica
        if not part.isdigit():
            return False

        number = int(part)

        # Cada octeto debe estar entre 0 y 255
        if number < 0 or number > 255:
            return False

    return True

# -----------------------------
# Resolver dominio
# -----------------------------
def resolve_domain(domain):
    try:
        ip = socket.gethostbyname(domain)
        print(f"[DNS] {domain} → {ip}")
        return ip
    except socket.gaierror:
        print("[DNS] No se pudo resolver el dominio")
        return None

# -----------------------------
# Ping (sin atajos)
# -----------------------------
def ping_host(ip):
    try:
        result = subprocess.run(
            ["ping", "-c", "1", "-W", "1", ip],
            stdout=subprocess.DEVNULL,
            stderr=subprocess.DEVNULL
        )

        if result.returncode == 0:
            print("[PING] Host activo")
            return True
        else:
            print("[PING] Host no responde")
            return False

    except Exception:
        print("[PING] Error ejecutando ping")
        return False

# -----------------------------
# Escaneo de puertos (lógico)
# -----------------------------
def scan_ports(ip):
    ports = [21, 22, 80, 443]

    for port in ports:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1)

        result = sock.connect_ex((ip, port))

        if result == 0:
            print(f"[PORT] {port} abierto")

        sock.close()

# -----------------------------
# Main
# -----------------------------
def main():
    args = get_arguments()
    target = args.target

    # Decisión explícita
    if is_ip(target):
        ip = target
    else:
        ip = resolve_domain(target)
        if ip is None:
            print("[ERROR] Target inválido")
            sys.exit(1)

    # Conectividad
    ping_host(ip)

    # Puertos
    scan_ports(ip)

    #resolve domain
    resolve_domain(ip)

if __name__ == "__main__":
    main()
