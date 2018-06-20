
from subprocess import call


def checkout(branch, create=False):
    command = ['git', 'checkout']
    if create:
        command.append('-b')
    command.append(branch)
    call(command)


def pull_request(branch, browse=False):
    command = ['hub', 'pull-request', '-b', branch]
    if browse:
        command.append('-o')
    call(command)


def pull():
    call(['git', 'pull'])
