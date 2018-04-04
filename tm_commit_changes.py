#!/usr/bin/env python3


from subprocess import call
import sys
import re

import tickets
import config


def main():
    call(['git', 'status'])
    yN = input('Continue committing staged file(s) [yN]? ') or 'n'

    ticket_id = config.main['current_ticket_id']
    print('Ticket ID: {}'.format(ticket_id))

    pattern = re.compile("[yY]+")
    if pattern.match(yN):
        commit(ticket_id)
    else:
        print('Change/s not committed')


def commit(ticket_id):
    commit_title = tickets.current()['description']
    print('Commit title: {}'.format(commit_title))
    commit_description = input('Commit description: ')
    call_ret = call(
        ['git', 'commit', '-m', commit_title, '-m', commit_description])

    if call_ret == 0:
        print('Commit completed.')
    else:
        print('Commit failed.')
        sys.exit(call_ret)


config.load()
main()
