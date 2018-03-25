import config
import logger


driver = None
logger = logger.instance


def login(web_driver):
    global driver
    driver = web_driver

    enter_username()
    enter_password()
    submit_login()


def enter_username():
    username = config.username
    username_element = driver.find_element_by_id('login-form-username')
    username_element.clear()
    username_element.send_keys(username)


def enter_password():
    password = config.password
    password_element = driver.find_element_by_id('login-form-password')
    password_element.clear()
    password_element.send_keys(password)


def submit_login():
    submit_element = driver.find_element_by_id('login-form-submit')
    submit_element.click()


def print_summary(ticket_id):
    '''
    Print the description and the calculated branch.
    '''
    desc_element = driver.find_element_by_id('summary-val')
    logger.info(translate_to_branch(ticket_id, desc_element.text))
    logger.info('{}: {}'.format(ticket_id, desc_element.text))


def translate_to_branch(id, description):
    return 'feature/{}-{}'.format(
        id,
        description.replace(' - ', '-')
        .replace(' ', '-')
        .replace("'", ''))

