# WARNING: Safari don't seem to wait for element before trying to interact with
# it. We are left with manual sleep for now.
import time
import logger


driver = None
logger = logger.instance


def login(web_driver):
    global driver
    driver = web_driver

    time.sleep(1)
    submit_login()
    time.sleep(6)


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
