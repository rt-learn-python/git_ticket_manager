import os
import sys
import yaml

from dotenv import load_dotenv

import logger


logger = logger.instance


main = None
home_folder = os.environ['HOME']
CONFIG_FILE = '{}/tickets.yml'.format(home_folder)

jira_username = None
jira_password = None
tc_username = None
tc_password = None

chrome_driver_bin = None
chrome_bin = None

env_path = os.path.dirname(os.path.realpath(__file__)) + '/.env'
load_dotenv(dotenv_path=env_path)

headless = os.getenv('HEADLESS') == 'true'


def init_web_env():
    '''
    Initialize environment variables in preparation for web interaction.
    '''
    global jira_username
    global jira_password
    global tc_username
    global tc_password
    global chrome_driver_bin
    global chrome_bin

    jira_username = os.getenv('JIRA_USERNAME')
    tc_username = os.getenv('TC_USERNAME')
    jira_password = os.getenv('JIRA_PASSWORD')
    tc_password = os.getenv('TC_PASSWORD')

    if not jira_password:
        global logger
        logger.error(
            'Jira password was not found in the environment variables.')
        sys.exit(1)

    chrome_driver_bin = os.getenv('CHROME_DRIVER_BIN')
    chrome_bin = os.getenv('CHROME_BIN')


def project_detail(project_name):
    return main['projects'].get(project_name)


def load():
    global main

    with open(CONFIG_FILE) as file:
        main = yaml.load(file)['main']

    # pprint(tickets['main'])


def save():
    with open(CONFIG_FILE, 'w') as outfile:
        yaml.dump({'main': main}, outfile, default_flow_style=False)
