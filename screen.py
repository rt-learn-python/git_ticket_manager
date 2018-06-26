import platform
import os


def println(text=''):
    print(text, end='\n')


def printhr():
    print('-' * 80)


def clear():
    if platform.system() == 'Darwin':
        os.system("clear")
        os.system(r"printf '\e[3J'")
