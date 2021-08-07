#!/usr/bin/env python3

# Integrates with external session. plist file is expected at
# env.SESSION_FILEPATH. Will set the current project to BSS when checking out
# from a mobile-bss folder.
#
# Create a another branch for an existing ticket or to create a new branch
# altogether if it does not exist yet.  You must be in the correct project
# folder because this script will read that.

import sys
import projects
import tickets
import config
import re
import logger

# Used modify external session's current project.
import os
import subprocess


# Globals
logger = logger.instance


def main():
    config.load()

    session_filepath = config.session_plist + '.plist'
    if 'bss' in os.getcwd():
        try:
            subprocess.call([
                'plutil', '-replace', 'Current Project', '-string',
                'Mobile BSS', session_filepath])

            subprocess.call([
                'plutil', '-replace', 'Current Project Key', '-string', 'bss',
                session_filepath])

        except Exception:
            pass

    ticket_desc = None
    if len(sys.argv) > 1:
        ticket_id = sys.argv[1].upper()

        subprocess.call([
            'plutil', '-replace', 'Current Ticket', '-string',
            ticket_id, session_filepath])

        if len(sys.argv) > 2:
            ticket_desc = sys.argv[2]
    else:
        projects.print_tickets_for_select()
        choice = input('Enter ticket line number or ticket ID: ')
        pattern = re.compile(r"\d+")

        if pattern.match(choice):
            ticket_id = projects.ticket_at(choice)
        else:
            ticket_id = choice

    tickets.set_current_ticket(ticket_id)

    do_create = not projects.ticket_exists(ticket_id)
    if do_create:
        tickets.create(ticket_id, ticket_desc)

    tickets.switch_ticket(ticket_id, do_create)


main()
