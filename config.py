import os
import sys
import yaml

from dotenv import load_dotenv

import logger


logger = logger.instance


main = None
home_folder = os.environ['HOME']
CONFIG_FILE = '{}/tickets.yml'.format(home_folder)

jira_url = None
jira_username = None
jira_password = None

chrome_driver_bin = None
chrome_bin = None

env_path = os.path.dirname(os.path.realpath(__file__)) + '/.env'
load_dotenv(dotenv_path=env_path)

headless = os.getenv('HEADLESS') == 'true'


def init_web_env():
    '''
    Initialize environment variables in preparation for web interaction.
    '''
    global jira_url
    global jira_username
    global jira_password
    global chrome_driver_bin
    global chrome_bin

    jira_url = os.getenv('JIRA_URL')
    jira_username = os.getenv('JIRA_USERNAME')
    jira_password = os.getenv('JIRA_PASSWORD')

    chrome_driver_bin = os.getenv('CHROME_DRIVER_BIN')
    chrome_bin = os.getenv('CHROME_BIN')


def check_jira_password_exists():
    if not jira_password:
        logger.error(
            'Jira password was not found in the environment variables.')
        sys.exit(1)


def project_detail(project_name):
    return main['projects'].get(project_name)


def load():
    global main

    try:
        with open(CONFIG_FILE) as file:
            main = yaml.safe_load(file)['main']
    except Exception as e:
        main = {
            'projects': {}
        }


def save():
    with open(CONFIG_FILE, 'w+') as outfile:
        yaml.dump({'main': main}, outfile, default_flow_style=False)
