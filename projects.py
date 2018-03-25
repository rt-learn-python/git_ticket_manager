from screen import *
import config
import tickets


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
