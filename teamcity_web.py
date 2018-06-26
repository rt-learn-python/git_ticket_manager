import config
import logger


driver = None
delete_at_night = None
logger = logger.instance


def login(web_driver):
    global driver
    driver = web_driver

    enter_username()
    enter_password()
    submit_login()


def enter_username():
    username = config.tc_username
    username_element = driver.find_element_by_id('username')
    username_element.clear()
    username_element.send_keys(username)


def enter_password():
    password = config.tc_password
    password_element = driver.find_element_by_id('password')
    password_element.clear()
    password_element.send_keys(password)


def submit_login():
    submit_element = driver.find_element_by_name('submitLogin')
    submit_element.click()


def collapse_dev_branch_section():
    section = driver.find_elements_by_xpath(
        '//*[@id="bt548-div"]/span[2]/a')
    if section:
        toggle = driver.find_element_by_id('blockHandleovr_project7')
        toggle.click()


def click_run_button():
    run_element = driver.find_elements_by_xpath(
        '//*[@id="bt543-div"]/table/tbody/tr/td[2]/span/button[1]')[0]
    run_element.click()


def set_code_base(app_version):
    version_element = driver.find_element_by_name('parameter_Codebase_Version')
    version_element.clear()
    version_element.send_keys(app_version)


def start_build_job():
    run_build_element = driver.find_element_by_id('runCustomBuildButton')
    run_build_element.click()


def selectR4Large():
    r4_large_option = driver.find_element_by_xpath(
        '//*[@id="parameter_Instance_Type"]/option[2]')
    r4_large_option.click()


def keep_stack_indefinitely():
    delete_element = driver.find_element_by_id(
        'parameter__STACK_ADD_TO_DELETE')
    if delete_element.is_selected:
        delete_element.click()


def toggle_kill_flexi_on():
    kill_flexi_element = driver.find_element_by_xpath(
        '//*[@id="parameter_TOGGLE_KILL_FLEXI"]')
    kill_flexi_element.click()
