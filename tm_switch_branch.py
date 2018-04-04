#!/usr/bin/env python3

# Create a another branch for an existing ticket or to create a new branch
# altogether if it does not exist yet.  You must be in the correct project
# folder because this script will read that.

import sys
import tickets
import config

import logger


# Globals
logger = logger.instance


def main():
    config.load()

    if len(sys.argv) > 1:
        ticket_id = sys.argv[1]
    else:
        ticket_id = input('Enter ticket ID: ')

    if tickets.exists(ticket_id):
        tickets.switch_branch(ticket_id)
    else:
        tickets.create_default_branch(ticket_id)


main()
