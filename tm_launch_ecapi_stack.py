#!/usr/bin/env python3

import os
import json
import sys

import web
import jira_web
import config

import tickets

# Globals
driver = None
delete_at_night = None


def main():
    config.load()

    if len(sys.argv) > 1:
        ticket_id = sys.argv[1]
    else:
        ticket_id = input('Enter ticket ID: ')

    tickets.switch_branch(ticket_id)
    confirm_current_project()

    global delete_at_night
    delete_at_night = input('Delete stack at night [Yn]? ): ')

    config.init_web_env()
    web.start(False)
    global driver
    driver = web.driver

    driver.get('https://automation.amaysim.net/')

    click_run_button()
    set_code_base()
    configure_keep_stack()
    selectR4Large()
    toggle_shark_on()
    start_build_job()


def confirm_current_project():
    tickets.show_current()
    answer = input('Proceed [Yn]? ')
    if answer.lower() == 'n':
        print('Aborted.')
        sys.exit(1)


def click_run_button():
    run_element = driver.find_elements_by_xpath(
        '//*[@id="bt543-div"]/table/tbody/tr/td[2]/span/button[1]')[0]
    run_element.click()


def set_code_base():
    version_element = driver.find_element_by_name('parameter_Codebase_Version')
    version_element.clear()
    app_version = calc_app_version()
    print('App Version: {}'.format(app_version))
    version_element.send_keys(app_version)


def start_build_job():
    run_build_element = driver.find_element_by_id('runCustomBuildButton')
    run_build_element.click()


def calc_app_version():
    project_path = os.environ.get('PROJECT_FOLDER')
    feature_id = os.environ.get('CURRENT_TICKET_ID')
    meta = json.load(open('{}/meta.json'.format(project_path)))

    return "{}-{}-SNAPSHOT".format(
        meta['version'],
        feature_id)


def selectR4Large():
    r4_large_option = driver.find_element_by_xpath(
        '//*[@id="parameter_Instance_Type"]/option[2]')
    r4_large_option.click()


def configure_keep_stack():
    '''Ask user to delete stack at night. Defaults Yes.'''
    if delete_at_night.lower() == 'n':
        delete_element = driver.find_element_by_id(
            'parameter__STACK_ADD_TO_DELETE')
        if delete_element.is_selected:
            delete_element.click()


def toggle_shark_on():
    shark_element = driver.find_element_by_xpath(
        '//*[@id="parameter_TOGGLE_SHARK"]/option[2]')
    shark_element.click()


main()
