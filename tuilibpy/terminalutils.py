# tuilibpy/terminalutils.py - Basic terminal utils
# (C) Copyright 2025 Ben Daws

import sys
import os

def ansi_clear_screen():
    sys.stdout.write("\033[2J")

def clear_screen():
    if os.name == 'nt':
        _ = os.system('cls')
    else:
        _ = os.system('clear')

def hide_cursor():
    print("\033[?25l", end="")

def show_cursor():
    print("\033[?25h", end="")