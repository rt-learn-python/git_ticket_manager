import projects
import config
from screen import *
import sys
import logger


from subprocess import call
import web
import jira_web


# Requires that configuration file have already been loaded by the main script.

logger = logger.instance


def switch_branch(ticket_id):
    prompt_create_branch(ticket_id)


def prompt_create_branch(ticket_id):
    new_branch = input('Do you want to create a new branch [Ny]? ') or 'n'
    if new_branch.lower() == 'y':
        create_another_branch(ticket_id)
    else:
        if is_multi_branch(ticket_id):
            prompt_for_branch(ticket_id)
        else:
            set_current_ticket(ticket_id, 1)
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
    add(ticket_id, desc, branch)


def switch_to_lone_branch(ticket_id):
    call(['git', 'checkout', current()['branches'][0]])


def exists(ticket_id):
    projects = config.main['projects']
    for project, project_detail in projects.items():
        logger.debug(project)
        if project_detail['tickets']:
            for ticket, ticket_detail in project_detail['tickets'].items():
                if ticket == ticket_id:
                    return True
    return False


def is_multi_branch(ticket_id):
    pass


def list_with_branches(project):
    tickets = project['tickets']
    if tickets:
        for ticket in tickets:
            print('\t{}: {}'.format(
                ticket['ticket'],
                ticket['description']
            ))
            branches = ticket['branches']
            for branch in branches:
                print('\t\t{}'.format(branch['branch']))

    else:
        print('\tNo ticket.')


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

    branch_index = 1
    if projects.get(project_name):
        branch_index = _create_additional_ticket(project_name, new_ticket)
    else:
        _create_first_ticket(project_name, new_ticket)

    set_current_ticket(ticket_id, branch_index or 1)

    config.save()
    logger.info("New ticket created.")


def set_current_ticket(ticket_id, branch_index):
    config.main['current_branch_index'] = branch_index
    config.main['current_ticket_id'] = ticket_id


def _create_first_ticket(project_name, new_ticket):
    '''
    Create a first ticket for unregistered project.
    '''
    logger.info('Creating new project...')
    branch_base = input('Enter the base branch name: ')
    branch_merge = input('Enter the merge branch name: ')
    new_ticket['branches'] = [new_ticket['branch']]
    ticket_id = new_ticket['id']
    del new_ticket['id']
    del new_ticket['branch']

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
    new_ticket['branches'] = [new_ticket['branch']]
    del new_ticket['id']
    del new_ticket['branch']
    tickets[ticket_id] = new_ticket


def _create_additional_branch(ticket_id, branch):
    '''
    Create a another branch for an existing ticket.
    '''
    pass


def choose_branch():
    '''
    Select a ticket branch:
    '''
    projects.print_with_tickets_and_branches()
    sys.exit()

    while True:
        print_for_select()
        print('q. quit')
        chosen = input('Enter # of preferred ticket: ')
        if chosen == 'q':
            do_loop = False
        elif chosen in tickets_for_select.keys():
            config['main']['current_ticket_id'] = tickets_for_select[chosen]
            do_loop = False
            tickets.show_current()


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
    print('Current Ticket:')
    printhr()
    print('{}: {}\nBranch: {}'
          .format(
              config.main['current_ticket_id'],
              current()['description'],
              current_branch_name()
          ))
    printhr()


def current():
    '''
    Return the curret ticket detail based or the currently set
    current_ticket_id.
    '''
    current_ticket_id = config.main['current_ticket_id']
    projects = config.main['projects']
    for project, project_detail in projects.items():
        project_tickets = project_detail['tickets']
        if project_tickets and current_ticket_id in project_tickets:
            return project_tickets[current_ticket_id]
    return None


def current_branch_name():
    '''
    Retrieve current branch name from config.
    '''
    current_branch_index = config.main['current_branch_index'] or 1
    ticket = current()
    branches = ticket['branches']
    for i in range(0, len(branches)):
        if i == current_branch_index - 1:
            return branches[i]
