#!/usr/bin/env python3

from subprocess import call
import projects
import tickets
import pyperclip


def main():
    input(
        'PR comment will be available from the clipboard, press <return> '
        'to continue')

    ticket = tickets.current()

    pyperclip.copy('{}: {}'.format(ticket['id'], ticket['description']))
    call(['hub', 'pull-request', '-b', projects.merge_branch(), '-o'])


main()
