# Overview

We can work with multiple projects, each project can have multiple tickets, with only one active at a time.  Each ticket can have multiple branches.


## Development


### Virtual environments


#### Set Up virtual environment

```
$ virtualenv venv
```


#### Activate virtual environment

```
$ source venv/bin/activate
```


#### Leave the virtual environment

```
$ deactivate
```



### Dependencies

```
$ pip install pyyaml selenium python-dotenv coverage
```


## Limitations

Supports a single branch per ticket only, to avoid the complexity.
If I need multiple branch, I can manually create it and manually update the tickets.yml.


## Issues

1. Initially designed to have a menu in the console but it is making it complicated.  Changed approach to use small functions.
- PyInstall was considered...


## Edge case, card where you need to modify multiple repositories.