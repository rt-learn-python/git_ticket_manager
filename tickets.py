"""
TODO:
"""

import os
import subprocess

from datetime import datetime

import projects
import config
import logger

import git_wrapper as git

# import web
# import jira_web
import util

# Safari is very unreliable to automate.
# import web_safari as web
# import jira_web_safari as jira_web


import screen


# Requires that configuration file have already been loaded by the main script.

logger = logger.instance


def create(ticket_id, given_desc=None):
    """
    TODO:
    """
    if given_desc is None:
        logger.info("create default branch")

        subprocess.call(
            ["osascript", config.as_filepath + "/Read JIRA Summary.applescript"]
        )

        desc_raw = subprocess.check_output(
            ["defaults", "read", config.session_plist, "New Ticket Description"]
        )
        desc = desc_raw.decode("utf-8").rstrip()

    else:
        desc = given_desc

    branch = util.translate_to_branch(ticket_id, desc)
    add(ticket_id, desc, branch)
    config.save()


def delete_ticket(ticket_id):
    """
    Delete the ticket_id from the config.
    """
    logger.info("Deleting ticket...")
    logger.info("Ticket ID: %s", ticket_id)
    logger.debug("Current Folder: %s", os.getcwd())

    config.load()

    projects_node = config.main["projects"]
    project_name = os.path.basename(os.getcwd())

    logger.debug("Project name: %s", project_name)

    project_detail = projects_node.get(project_name)
    if project_detail:
        tickets = project_detail["tickets"]
        result = tickets.pop(ticket_id, None)
        if result:
            config.save()
            logger.info("Ticket deleted.")


def switch_ticket(_ticket_id, p_create=False):
    """
    TODO:
    """
    if p_create:
        git.checkout(projects.current_base_branch())
        git.pull()

    git.checkout(current()["branch"], p_create)


def exists(ticket_id):
    """
    TODO:
    """
    project_list = projects.current()
    for project, project_detail in project_list.items():
        logger.debug(project)
        project_tickets = project_detail["tickets"]
        if project_tickets:
            for ticket, _ticket_detail in project_tickets.items():
                if ticket == ticket_id:
                    return True
    return False


def add(ticket_id, desc, branch):
    """
    Creates a new ticket and sets as the current.
    """
    logger.info("Creating new ticket...")
    logger.info("Ticket ID: %s", ticket_id)
    logger.info("Description: %s", desc)
    logger.info("Branch: %s", branch)
    logger.debug("Current Folder: %s", os.getcwd())

    config.load()

    new_ticket = {"id": ticket_id, "description": desc, "branch": branch}

    projects_node = config.main["projects"]
    project_name = os.path.basename(os.getcwd())

    logger.debug("Project name: %s", project_name)

    if projects_node.get(project_name):
        _create_additional_ticket(project_name, new_ticket)
    else:
        _create_first_ticket(project_name, new_ticket)

    set_current_ticket(ticket_id)
    logger.info("New ticket created.")


def set_current_ticket(ticket_id):
    """
    TODO:
    """
    project_detail = projects.current()
    project_detail["current_ticket_id"] = ticket_id
    config.save()


def _create_first_ticket(project_name, new_ticket):
    """
    Create a first ticket for unregistered project.
    """
    logger.info("Creating new project...")
    branch_base = input("Enter the base branch name: ")
    branch_merge = input("Enter the merge branch name: ")
    ticket_id = new_ticket["id"]
    del new_ticket["id"]

    config.main["projects"][project_name] = {
        "branches": {
            "base": branch_base,
            "merge": branch_merge,
            "tickets": {ticket_id: new_ticket},
        }
    }


def _create_additional_ticket(project_name, new_ticket):
    """
    Create a ticket for a previously registered project.
    """
    ticket_id = new_ticket["id"]
    logger.info("Adding %s to %s", ticket_id, project_name)
    project_detail = config.main["projects"][project_name]
    if "tickets" not in project_detail:
        project_detail["tickets"] = {}
    tickets = project_detail["tickets"]
    new_ticket["date_created"] = datetime.now()
    del new_ticket["id"]
    if tickets is None:
        tickets = {}
    tickets[ticket_id] = new_ticket
    logger.debug(tickets[ticket_id])


def print_for_select(project):
    """
    Print projects with numbered tickets for selection.
    """
    if project["tickets"]:
        for ticket in project["tickets"]:
            print(f"{project['project']} - {ticket['ticket']}: {ticket['description']}")


# def print_list():
#     global tickets_for_select
#     tickets_for_select.clear()

#     projects = config.main['projects']

#     index = 0
#     for _name, detail in projects.items():
#         tickets = detail['tickets']
#         if tickets:
#             for id, ticket_detail in tickets.items():
#                 index += 1
#                 tickets_for_select[str(index)] = id
#                 print('{}  {}: {}'.format(
#                     index, id, ticket_detail['description']))


def show_current():
    """
    TODO:
    """
    project_detail = config.project_detail(projects.current_name())
    if project_detail:
        print("Current Ticket:")
        screen.printhr()

        current_ticket = current()

        print(
            f"{project_detail['current_ticket_id']}: \
            {current_ticket['description']}\nBranch: {current_ticket['branch']}"
        )

        screen.printhr()
    else:
        print("Current directory is not registered.")


def current():
    """
    Return the current ticket detail based on the currently set
    current_ticket_id.
    """
    project_detail = projects.current()
    current_ticket_id = project_detail["current_ticket_id"]
    project_tickets = project_detail["tickets"]
    if project_tickets and current_ticket_id in project_tickets:
        ticket = project_tickets[current_ticket_id]
        ticket["id"] = current_ticket_id
        return ticket
    return None
