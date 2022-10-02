'''
TODO:
'''

from selenium import webdriver
from selenium.webdriver.chrome.options import Options

import config
import logger


# Global
DRIVER = None
LOGGER = logger.instance


def init(p_logger):
    '''
    TODO
    '''
    global LOGGER
    LOGGER = p_logger


def start(headless=True):
    '''
    TODO
    '''
    global DRIVER

    if not headless:
        DRIVER = webdriver.Chrome()
    elif config.headless:
        chrome_options = Options()
        chrome_options.add_argument("--headless")
        chrome_options.binary_location = config.chrome_bin
        DRIVER = webdriver.Chrome(
            executable_path=config.chrome_driver_bin,
            chrome_options=chrome_options
        )
    else:
        DRIVER = webdriver.Chrome()

    DRIVER.implicitly_wait(10)
    LOGGER.info('Selenium started')
