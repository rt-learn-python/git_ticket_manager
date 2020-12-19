from selenium import webdriver
# from selenium.webdriver.chrome.options import Options

# import config
import logger


# Globals
driver = None
logger = logger.instance


def init(p_logger):
    global logger
    logger = p_logger


def start(headless=True):
    global driver

    driver = webdriver.Safari()
    driver.implicitly_wait(30)
    logger.info('Selenium started')
