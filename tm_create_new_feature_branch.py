#!/usr/bin/env python3

from subprocess import call
import re
import projects
import tickets

import git_wrapper as git

# TODO: Check if branch already present in .git/config, abort and notify if it
# is.


class color:
    PURPLE = '\033[95m'
    CYAN = '\033[96m'
    DARKCYAN = '\033[36m'
    BLUE = '\033[94m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    END = '\033[0m'


def main():
    print("{}IMPORTANT{}: Make sure you have no pending changes".format(
        color.BOLD, color.END))

    call(['git', 'status'])

    base_branch = projects.current_base_branch()
    print('\nBase branch: {}'.format(base_branch))
    feature_branch = tickets.current_branch_name()
    print('Feature branch: {}\n'.format(feature_branch))

    yN = input('Continue creating new branch [y/N]? ')

    pattern = re.compile("[yY]+")
    if pattern.match(yN):
        create_branch(base_branch, feature_branch)
    else:
        print('Aborted')


def create_branch(base, feature):
    print('Creating branch via git commands...')

    git.checkout(base)
    git.pull()
    git.checkout(feature, create=True)


main()
