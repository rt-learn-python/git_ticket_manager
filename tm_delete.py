#!/usr/bin/env python3

# Delete a ticket in tickets.yml. Used for testing, we want to reuse an existing
# ticket and simulate that it has never been checked out before.

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
        ticket_id = sys.argv[1].upper()

    else:
        projects.print_tickets_for_select()
        choice = input('Enter ticket line number or ticket ID: ')
        pattern = re.compile(r"\d+")

        if pattern.match(choice):
            ticket_id = projects.ticket_at(choice)
        else:
            ticket_id = choice

    tickets.delete_ticket(ticket_id)


main()
