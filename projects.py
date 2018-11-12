import subprocess
import config
import logger
import os


# Globals
logger = logger.instance


config.load()


def ticket_exists(ticket_id):
    print(current())
    if 'tickets' in current():
        tickets = current()['tickets']
        return tickets is not None and ticket_id in tickets
    return False


def detect_current_branch():
    result = subprocess.run(['git', 'branch'], stdout=subprocess.PIPE)
    lines = result.stdout.decode('utf-8').split('\n')
    return [x[2:].strip() for x in lines if x.strip().startswith('*')][0]


def switch_to_base():
    pass


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
    for _ticket, ticket_detail in project_tickets.items():
        if counter == choice:
            return ticket_detail
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
    projects = config.main['projects']
    if current_name() not in projects:
        create_project(current_name(), 'master', 'master')

    return projects[current_name()]


def current_merge_branch():
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
    Returns the current project merge branch
    '''
    return current()['branches']['base']


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

    confirm = input('Are the values you entered correct [y/N]? ')
    if confirm.lower() == 'y':
        create_project(project_name, branch_base, branch_merge)


def create_project(project_name, branch_base, branch_merge):
    config.main['projects'][project_name] = {
        'branches': {
            'base': branch_base or 'master',
            'merge': branch_merge or 'master'
        }
    }
    config.save()
