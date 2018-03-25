from screen import *


last_menu = None


def last(option):
    '''
    sets the most recent option.
    '''
    global last_menu
    last_menu = option


def last_is(option):
    pass


def print_main():
    global last_menu

    println('Main Menu:')
    printhr()

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
