#!/usr/bin/env python3

# Create a another branch for an existing ticket or to create a new branch
# altogether if it does not exist yet.  You must be in the correct project
# folder because this script will read that.

import sys
import projects
import tickets
import config
import re
import logger


# Globals
logger = logger.instance


def main():
    config.load()

    if len(sys.argv) > 1:
        ticket_id = sys.argv[1]
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
        tickets.create(ticket_id)

    tickets.switch_ticket(ticket_id, do_create)


main()
