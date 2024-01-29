# import config

"""
Wraps git shell commands with python procedures.
"""

from subprocess import call


def checkout(branch, create=False):
    """
    rtfc
    """
    command = ["git", "checkout"]
    if create:
        command.append("-b")
    # command.append(branch.replace("(", "\\(").replace(")", "\\)"))
    command.append(branch)
    _call(command)


def pull_request(branch, ticket_id, title, browse=False):
    """
    rtfc
    """

    # command = ['hub', 'pull-request', '-b', branch, '-r', config.reviewers,
    #            '-l', 'WIP',
    #            '-m', '''{}

    command = [
        "hub",
        "pull-request",
        "-b",
        branch,
        # "-l",
        # "WIP",
        "-d",
        "",
        "-m",
        f"""{title}

[JIRA](https://jira.amaysim.net/browse/{ticket_id})""",
    ]

    if browse:
        command.append("-o")

    _call(command)


def pull():
    """
    Runs git pull command
    """

    _call(["git", "pull"])


def push(branch):
    """
    Runs git push command
    """

    _call(["git", "push", "-u", "origin", branch])


def _call(command):
    print(f"Running command: {' '.join(command)}")
    call(command)
