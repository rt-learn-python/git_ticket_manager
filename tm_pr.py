#!/usr/bin/env python3

"""
TODO
"""

import pyperclip

import projects
import tickets
import git_wrapper as git


def main():
    """
    # input(
    #     'PR comment will be available from the clipboard, press <return> '
    #     'to continue')
    """

    ticket = tickets.current()

    title = f"{ticket['id']}: {ticket['description']}"
    pyperclip.copy(title)
    git.pull_request(projects.current_merge_branch(), ticket["id"], title, browse=True)


main()
