import os
import sys
import yaml

from dotenv import load_dotenv
import logger

logger = logger.instance


main = None
home_folder = os.environ['HOME']
CONFIG_FILE = '{}/tickets.yml'.format(home_folder)
username = None
password = None
chrome_driver_bin = None
chrome_bin = None

load_dotenv()

headless = os.getenv('HEADLESS') == 'true'


def init_web_env():
    '''
    Initialize environment variables in preparation for web interaction.
    '''
    global username
    global password
    global chrome_driver_bin
    global chrome_bin

    username = os.getenv('JIRA_USERNAME')
    password = os.getenv('JIRA_PASSWORD')

    if not password:
        global logger
        logger.error(
            'Jira password was not found in the environment variables.')
        sys.exit(1)

    chrome_driver_bin = os.getenv('CHROME_DRIVER_BIN')
    chrome_bin = os.getenv('CHROME_BIN')


def load():
    global CONFIG_FILE
    global main

    with open(CONFIG_FILE) as file:
        main = yaml.load(file)['main']

    # pprint(tickets['main'])


def save():
    global main
    with open(CONFIG_FILE, 'w') as outfile:
        yaml.dump({'main': main}, outfile, default_flow_style=False)
