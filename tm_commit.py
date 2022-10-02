#!/usr/bin/env python3

"""
TODO
"""


import subprocess
import sys
import re

import projects
import tickets
import config

import logger


logger = logger.instance


def main():
    """
    TODO:
    """
    subprocess.call(["git", "status"])

    yn_response = input("Continue committing staged file(s) [y/N]? ") or "n"

    ticket_id = projects.current_ticket_id()
    print(f"Ticket ID: {ticket_id}")

    pattern = re.compile("[yY]+")
    if pattern.match(yn_response):
        commit()
    else:
        print("Change/s not committed")


def commit():
    """
    TODO:
    """
    ticket_detail = tickets.current()
    jira_id = ticket_detail["id"]
    jira_desc = ticket_detail["description"]
    commit_title = f"{jira_id}: {jira_desc}"

    print(f"Commit title: {commit_title}")
    commit_description = input("Commit description: ")
    call_ret = subprocess.call(
        ["git", "commit", "-m", commit_title, "-m", commit_description]
    )

    if call_ret == 0:
        print("Commit completed.")
    else:
        print("Commit failed.")
        sys.exit(call_ret)


config.load()
main()
