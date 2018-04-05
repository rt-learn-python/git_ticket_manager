#!/usr/bin/env python3

import sys
import os
import json
import re
import web
import teamcity_web
import config

import tickets

# Globals
driver = None


def main():
    config.load()

    confirm_current_project()
    yN = input('Delete stack at night [Yn]? ): ')
    pattern = re.compile("[yY]+")

    config.init_web_env()
    web.start(False)
    global driver
    driver = web.driver

    driver.get('https://automation.amaysim.net/')
    teamcity_web.login(web.driver)

    teamcity_web.collapse_dev_branch_section()
    teamcity_web.click_run_button()
    teamcity_web.set_code_base(calc_app_version())
    if pattern.match(yN):
        teamcity_web.keep_stack_indefinitely()
    teamcity_web.selectR4Large()
    teamcity_web.toggle_shark_on()
    teamcity_web.start_build_job()


def calc_app_version():
    project_path = os.getcwd()
    feature_id = config.main['current_ticket_id']
    meta = json.load(open('{}/meta.json'.format(project_path)))

    return "{}-{}-SNAPSHOT".format(
        meta['version'],
        feature_id)


def confirm_current_project():
    tickets.show_current()
    answer = input('Proceed [Yn]? ')
    if answer.lower() == 'n':
        print('Aborted.')
        sys.exit(1)


main()
