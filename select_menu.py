from screen import *
import projects


def print_menu():
    println('Select ticket branch:')
    printhr()
    projects.print_with_tickets_and_branches()
    print('n - Create a new branch')

    if last_menu != 'c' and last_menu is not None:
        print('c - Print current ticket')

    if last_menu != 'l':
        print('l - List project and tickets')

    if last_menu != 's':
        print('s - Select branch')

    if last_menu != 'p':
        print('n - New branch')

    println('q - Quit')
    printhr()
