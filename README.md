# Overview

Simplifies git workflow by formatting jira description as the default branch name,
commit title, and pull-request title.

## Prerequisites

1. Python 3
2. Jira Access

## Setting Up as User

1. Clone or fork this repo
2. cd to the project folder
3. Run `pip3 install -r requirements.txt`
4. Create the .env file from .env.template

## Usage

    1. Switch branch new or old. If not existing, it will create a branch named
    feature/JIRA-001-description-here based on the jira description.

```shell
tm_checkout_branch <ticket_id>
```

    2. Commit changes. You need to stage some changes first manually, then this will
    prompt you for optional commit description.  Commit title will be the jira
    description.

```shell
tm_commit.py
```

    3. Push changes. This will push your branch and set the current upstream to
    this branch so will let you use just `git push` for any subsequent commits.

```shell
tm_push.py
```

    3. Create pull request. Jira description will be stored in the clipboard
    which you can then use as title for this PR.

```shell
tm_pr.py
```

## Development

To install this project on a new machine, pull dependencies by running: (NOTE
that this will install these libraries globally)

```bash
pip3 install -r requirements.txt
```

### Virtual environments

#### Set Up virtual environment

```bash
virtualenv venv
```

#### Activate virtual environment

```bash
source venv/bin/activate
```

#### Leave the virtual environment

```bash
deactivate
```

## Limitations

Supports a single branch per ticket only, to avoid the complexity.
If I need multiple branch, I can manually create it and manually update the tickets.yml.

## Issues

1. PyInstall was considered...
