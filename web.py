from selenium import webdriver
from selenium.webdriver.chrome.options import Options

import config
import logger


# Globals
driver = None
logger = logger.instance


def init(p_logger):
    global logger
    logger = p_logger


def start():
    global driver

    chrome_options = Options()
    chrome_options.add_argument("--headless")
    chrome_options.binary_location = config.chrome_bin

    driver = webdriver.Chrome()

    # driver = webdriver.Chrome(
    #     executable_path=config.chrome_driver_bin,
    #     chrome_options=chrome_options)

    driver.implicitly_wait(10)
    logger.info('Selenium started')
