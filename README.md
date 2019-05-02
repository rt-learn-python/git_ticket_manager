# Overview

We can work with multiple projects, each project can have multiple tickets, with
 only one active at a time.  Each ticket can have multiple branches.


## Prerequisites

1. Python 3
2. Jira Access

## Setting Up as User

1. Clone or fork this repo
- cd to the project folder
- Run `pip3 install -r requirements.txt`




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

