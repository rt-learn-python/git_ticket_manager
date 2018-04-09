import subprocess
from screen import *
import config
import tickets
import logger


# Globals
logger = logger.instance


config.load()


def detect_current_branch():
    result = subprocess.run(['git', 'branch'], stdout=subprocess.PIPE)
    # print(result)
    # print(filter(None, result.stdout.decode('utf-8').split('\n')))
    # print(result.stdout.decode('utf-8').split('\n'))
    lines = result.stdout.decode('utf-8').split('\n')
    return [x[2:].strip() for x in lines if x.strip().startswith('*')][0]


def current_ticket_id():
    return current()['current_ticket_id']


def ticket_with_branch(branch):
    project_tickets = current()['tickets']
    for ticket, ticket_detail in project_tickets.items():
        if branch in ticket_detail['branches']:
            ticket_detail['id'] = ticket
            return ticket_detail


def ticket_at_index(choice):
    project_tickets = current()['tickets']
    counter = 1
    for ticket, ticket_detail in project_tickets.items():
        if counter == choice:
            return ticket
        counter += 1


def print_tickets_for_select():
    project_tickets = current()['tickets']
    counter = 1
    for ticket, ticket_detail in project_tickets.items():
        print('{} {}: {}'.format(
            counter, ticket, ticket_detail['description']))
        counter += 1


def current():
    '''
    Returns the current project detail
    '''
    return config.main['projects'][current_name()]


def merge_branch():
    '''
    Returns the current project merge branch
    '''
    return current()['branches']['merge']


def current_name():
    '''
    Assumes you are in the project root and returns the current folder name.
    '''
    return os.path.basename(os.getcwd())


def current_base_branch():
    '''
    Return the curret base branch of the project owner of the current ticket.
    '''
    config.load()
    current_ticket_id = config.main['current_ticket_id']
    projects = config.main['projects']
    for project, project_detail in projects.items():
        project_tickets = project_detail['tickets']
        if project_tickets and current_ticket_id in project_tickets:
            branches = project_detail['branches']
            return branches['base']
    return None


def print_with_tickets_and_branches():
    '''
    Used for selecting ticket and branch
    '''
    projects = config.main['projects']

    for project in projects:
        print('{} {}'.format(index, name))


def list():
    '''
    Return list of projects.
    '''
    return config.main['projects']


def new():
    '''
    Add a new project.  This will be expected in ~/projects
    '''
    project_name = input('Enter project folder name: ')
    branch_base = input('Enter the base branch: (defaults to master)')
    branch_merge = input('Enter the merge branch: (defaults to master) ')

    confirm = input('Are the values you entered correct [yN]? ')
    if confirm.lower() == 'y':
        create_project(project_name, branch_base, branch_merge)


def list_with_tickets():
    '''
    List projects with tickets for viewing only.
    '''
    project_list = config.main['projects']
    for project in project_list:
        print(project['project'])
        tickets.list_with_branches(project)
    else:
        printhr()


def print_tickets(project_detail):
    '''
    print tickets of the given project dict.
    '''
    tickets = project_detail['tickets']
    if tickets:
        for id, ticket_detail in tickets.items():
            print('\t{}: {}'.format(id, ticket_detail['description']))
    else:
        print('\tNo ticket for this project.')


def create_project(project_name, branch_base, branch_merge):
    config.main['projects'][project_name] = {
        'branches': {
            'base': branch_base or 'master',
            'merge': branch_merge or 'master'
        },
        'path': '~/projects/{}'.format(project_name),
        'tickets': None
    }
    config.save()
