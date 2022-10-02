#!/usr/bin/env python3

"""
# Push the existing branch to remote repository setting the default upstream
"""

import tickets
import config
import logger
import git_wrapper as git

# Global
logger = logger.instance


def main():
    """
    TODO:
    """
    config.load()

    current_branch = tickets.current()["branch"]
    git.push(current_branch)


main()
