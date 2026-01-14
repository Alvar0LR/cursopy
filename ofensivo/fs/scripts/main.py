#!/usr/bin/env python3

import sys
import signal
from forwardshell import ForwardShell
from termcolor import colored

def def_handler(sig, frame):
    print(colored(f"\n[+]Saliendo...", "red"))
    my_forwardshell.remove_data()
    sys.exit(1)

signal.signal(signal.SIGINT, def_handler)

if __name__ == '__main__':

    my_forwardshell = ForwardShell()
    my_forwardshell.run()
