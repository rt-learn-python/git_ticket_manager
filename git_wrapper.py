
from subprocess import call


def checkout(branch, create=False):
    command = ['git', 'checkout']
    if create:
        command.append('-b')
    command.append(branch)
    _call(command)


def pull_request(branch, browse=False):
    command = ['hub', 'pull-request', '-b', branch]
    if browse:
        command.append('-o')
    _call(command)


def pull():
    _call(['git', 'pull'])


def push(branch):
    _call(['git', 'push', '-u', 'origin', branch])


def _call(command):
    print('Running command: {}'.format(' '.join(command)))
    call(command)
