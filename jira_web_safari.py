# WARNING: Safari don't seem to wait for element before trying to interact with
# it. We are left with manual sleep for now.
# Also, the credentials at one point wasn't required to be inputed by the
# script, then now it is required.
import time
import logger
import config


driver = None
logger = logger.instance


def login(web_driver):
    global driver
    driver = web_driver

    enter_username()
    enter_password()

    time.sleep(1)
    submit_login()
    time.sleep(6)


def enter_username():
    username = config.jira_username
    username_element = driver.find_element_by_id("login-form-username")
    username_element.clear()
    username_element.send_keys(username)


def enter_password():
    password = config.jira_password
    password_element = driver.find_element_by_id("login-form-password")
    password_element.clear()
    password_element.send_keys(password)


def submit_login():
    submit_element = driver.find_element_by_id("login-form-submit")
    submit_element.click()


def extract_info(ticket_id):
    """
    Assumes you are on a ticket page and returns the calculated branch name
    and the formatted ticket description.
    """
    desc_element = driver.find_element_by_id("summary-val")
    logger.debug(desc_element.text[desc_element.text.index(" ") + 1:])

    translated = (
        _translate_to_branch(ticket_id, desc_element.text),
        desc_element.text)

    driver.quit()
    print(translated)

    return translated


# def print_summary(ticket_id):
#     '''
#     Print the description and the calculated branch.
#     '''
#     desc_element = driver.find_element_by_id('summary-val')
#     logger.info(translate_to_branch(ticket_id, desc_element.text))
#     logger.info('{}: {}'.format(ticket_id, desc_element.text))


def _translate_to_branch(id, description):
    return "feature/{}-{}".format(
        id,
        description.replace(" - ", "-")
        .replace(".", "_")
        .replace("/", "")
        .replace(": ", "-")
        .replace(" ", "-")
        .replace("'", "")
        .rstrip("_"),
    )
