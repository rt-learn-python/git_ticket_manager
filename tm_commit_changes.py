#!/usr/bin/env python3


import subprocess
import sys
import re

import projects
import tickets
import config


def main():
    subprocess.call(['git', 'status'])

    yN = input('Continue committing staged file(s) [yN]? ') or 'n'

    ticket_id = projects.current_ticket_id()
    print('Ticket ID: {}'.format(ticket_id))

    pattern = re.compile("[yY]+")
    if pattern.match(yN):
        commit()
    else:
        print('Change/s not committed')


def commit():
    branch_name = projects.detect_current_branch()
    ticket_detail = projects.ticket_with_branch(branch_name)

    commit_title = '{}: {}'.format(
        ticket_detail['id'],
        ticket_detail['description'])

    print('Commit title: {}'.format(commit_title))
    commit_description = input('Commit description: ')
    call_ret = subprocess.call(
        ['git', 'commit', '-m', commit_title, '-m', commit_description])

    if call_ret == 0:
        print('Commit completed.')
    else:
        print('Commit failed.')
        sys.exit(call_ret)


config.load()
main()

