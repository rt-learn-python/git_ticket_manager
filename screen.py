"""
TODO:
"""

import platform
import os


def println(text=""):
    """
    TODO:
    """
    print(text, end="\n")


def printhr():
    """
    TODO:
    """
    print("-" * 80)


def clear():
    """
    TODO:
    """
    if platform.system() == "Darwin":
        os.system("clear")
        os.system(r"printf '\e[3J'")
