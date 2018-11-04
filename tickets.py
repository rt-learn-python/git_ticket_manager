import projects
import config
import logger
from datetime import datetime

import git_wrapper as git
import web
import jira_web
import os

import screen


# Requires that configuration file have already been loaded by the main script.

logger = logger.instance


def create(ticket_id):
    logger.info('create default branch')
    config.init_web_env()
    config.check_jira_password_exists()
    web.start()
    driver = web.driver
    driver.get('https://jira.amaysim.net/browse/{}'.format(ticket_id))
    logger.info('Page loaded.')
    jira_web.login(web.driver)
    logger.info('Logged in to jira')
    branch, desc = jira_web.extract_info(ticket_id)
    add(ticket_id, desc, branch)
    config.save()


def switch_ticket(ticket_id, create=False):
    if create:
        git.checkout(projects.current_base_branch())
        git.pull()
    git.checkout(current()['branch'], create)


def exists(ticket_id):
    project_list = projects.current()
    for project, project_detail in project_list.items():
        logger.debug(project)
        if project_detail['tickets']:
            for ticket, ticket_detail in project_detail['tickets'].items():
                if ticket == ticket_id:
                    return True
    return False


def add(ticket_id, desc, branch):
    '''
    Creates a new ticket and sets as the current.
    '''
    logger.info('Creating new ticket...')
    logger.info('Ticket ID: {}'.format(ticket_id))
    logger.info('Description: {}'.format(desc))
    logger.info('Branch: {}'.format(branch))
    logger.debug('Current Folder: {}'.format(os.getcwd()))

    config.load()

    new_ticket = {
        'id': ticket_id,
        'description': desc,
        'branch': branch
    }

    projects = config.main['projects']
    project_name = os.path.basename(os.getcwd())

    logger.debug("Project name: {}".format(project_name))

    if projects.get(project_name):
        _create_additional_ticket(project_name, new_ticket)
    else:
        _create_first_ticket(project_name, new_ticket)

    set_current_ticket(ticket_id)
    logger.info("New ticket created.")


def set_current_ticket(ticket_id):
    project_detail = projects.current()
    project_detail['current_ticket_id'] = ticket_id
    config.save()


def _create_first_ticket(project_name, new_ticket):
    '''
    Create a first ticket for unregistered project.
    '''
    logger.info('Creating new project...')
    branch_base = input('Enter the base branch name: ')
    branch_merge = input('Enter the merge branch name: ')
    ticket_id = new_ticket['id']
    del new_ticket['id']

    print(ticket_id)
    print(new_ticket)

    config.main['projects'][project_name] = {
        'branches': {
            'base': branch_base,
            'merge': branch_merge,
            'tickets': {
                ticket_id: new_ticket
            }
        }
    }


def _create_additional_ticket(project_name, new_ticket):
    '''
    Create a ticket for a previously registered project.
    '''
    ticket_id = new_ticket['id']
    logger.info('Adding {} to {}'.format(ticket_id, project_name))
    project_detail = config.main['projects'][project_name]
    tickets = project_detail['tickets']
    new_ticket['date_created'] = datetime.now()
    del new_ticket['id']
    tickets[ticket_id] = new_ticket
    logger.debug(tickets[ticket_id])


def print_for_select(project):
    '''
    Print projects with numbered tickets for selection.
    '''
    if project['tickets']:
        for ticket in project['tickets']:
            print(
                "{} - {}: {}".format(
                    project['project'],
                    ticket['ticket'],
                    ticket['description']))


def print_list():
    global tickets_for_select
    tickets_for_select.clear()

    projects = config.main['projects']

    index = 0
    for _name, detail in projects.items():
        tickets = detail['tickets']
        if tickets:
            for id, ticket_detail in tickets.items():
                index += 1
                tickets_for_select[str(index)] = id
                print('{}  {}: {}'.format(
                    index, id, ticket_detail['description']))


def show_current():
    project_detail = config.project_detail(projects.current_name())
    if project_detail:
        print('Current Ticket:')
        screen.printhr()

        current_ticket = current()

        print('{}: {}\nBranch: {}'
              .format(
                  project_detail['current_ticket_id'],
                  current_ticket['description'],
                  current_ticket['branch']
              ))
        screen.printhr()
    else:
        print('Current directory is not registered.')


def current():
    '''
    Return the curret ticket detail based on the currently set
    current_ticket_id.
    '''
    project_detail = projects.current()
    current_ticket_id = project_detail['current_ticket_id']
    project_tickets = project_detail['tickets']
    if project_tickets and current_ticket_id in project_tickets:
        ticket = project_tickets[current_ticket_id]
        ticket['id'] = current_ticket_id
        return ticket
    return None
