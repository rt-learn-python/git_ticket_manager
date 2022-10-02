'''
TODO:
'''

from selenium import webdriver
# from selenium.webdriver.chrome.options import Options

# import config
import logger


# Global
DRIVER = None
logger = logger.instance


def init(p_logger):
    '''
    TODO:
    '''
    global logger
    logger = p_logger


def start(headless=True):
    '''
    TODO:
    '''
    global DRIVER

    DRIVER = webdriver.Safari()
    DRIVER.implicitly_wait(30)
    logger.info('Selenium started')
