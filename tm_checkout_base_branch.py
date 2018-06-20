#!/usr/bin/env python3

import projects
import git_wrapper as git


def main():
    git.checkout(projects.current_base_branch())


main()
