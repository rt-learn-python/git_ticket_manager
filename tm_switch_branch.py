#!/usr/bin/env python3

# Create a another branch for an existing ticket or to create a new branch
# altogether if it does not exist yet.  You must be in the correct project
# folder because this script will read that.

import tickets
import config

import logger

import web
import jira_web


# Globals
logger = logger.instance


def main():
    config.load()

    ticket_id = input('Enter ticket ID: ')

    if tickets.exists(ticket_id):
        switch_branch(ticket_id)
    else:
        create_default_branch(ticket_id)


def switch_branch(ticket_id):
    prompt_create_branch(ticket_id)


def prompt_create_branch(ticket_id):
    new_branch = input('Do you want to create a new branch [Ny]?') or 'n'
    if new_branch.lower() == 'y':
        create_another_branch(ticket_id)
    else:
        if tickets.is_multi_branch(ticket_id):
            prompt_for_branch(ticket_id)
        else:
            switch_to_lone_branch(ticket_id)


def create_default_branch(ticket_id):
    logger.info('create default branch')
    config.init_web_env()
    web.start()
    driver = web.driver
    driver.get('https://jira.amaysim.net/browse/{}'.format(ticket_id))
    logger.info('Page loaded.')
    jira_web.login(web.driver)
    logger.info('Logged in to jira')
    branch, desc = jira_web.extract_info(ticket_id)
    tickets.add(ticket_id, desc, branch)


main()
