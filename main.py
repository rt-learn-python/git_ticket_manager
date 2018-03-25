#!/usr/bin/env python3

# from pprint import pprint
import sys

import config
import main_menu
from screen import *
import tickets
import projects


def main():
    clear()
    config.load()
    tickets.show_current()

    while True:
        main_menu.print_main()
        option = input('Choose an option: ')

        if option == 'q':
            sys.exit()

        if option == 'c':
            tickets.show_current()
        elif option == 'l':
            clear()
            projects.list_with_tickets()
        elif option == 's':
            tickets.choose_branch()
        elif option == 'n':
            tickets.new()
        elif option == 'p':
            projects.new()
        else:
            clear()

        main_menu.last(option)


main()
