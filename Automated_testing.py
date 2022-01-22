#!/usr/bin/python3

import argparse
import sys
import json
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from selenium.common.exceptions import NoSuchElementException

"""
Use this class to add colors in terminal 
n.b: not applicable in windows command-line

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
"""


# No color
class bcolors:
    HEADER = ''
    OKBLUE = ''
    OKCYAN = ''
    OKGREEN = ''
    WARNING = ''
    FAIL = ''
    ENDC = ''
    BOLD = ''
    UNDERLINE = ''


DEFAULT_TEST_USERS = [
    {"username": "user", "password": "1234"},
    {"username": "unknown", "password": "fdsfdsdg"}
]

DEFAULT_BROWSER = "edge"

DEFAULT_DRIVER_PATH = r"./windows/driver/msedgedriver.exe"

DEFAULT_URL = "http://localhost/Automated_testing/login/"

DEFAULT_DELAY = 10

DEFAULT_USER_ID = "username"

DEFAULT_PASS_ID = "password"

DEFAULT_LOGOUT_ID = "logout"


def get_driver(browser=DEFAULT_BROWSER, driver_path=DEFAULT_DRIVER_PATH):
    if not browser:
        browser = DEFAULT_BROWSER
    if not driver_path:
        driver_path = DEFAULT_DRIVER_PATH

    if browser == "edge":
        return webdriver.Edge(service=webdriver.edge.service.Service(driver_path))
    elif browser == "chrome":
        return webdriver.Chrome(service=webdriver.chrome.service.Service(driver_path))
    elif browser == "firefox":
        return webdriver.Firefox(service=webdriver.firefox.service.Service(driver_path))
    elif browser == "opera":
        return webdriver.Opera(service=webdriver.opera.service.Service(driver_path))
    else:
        return None


def launch_test(driver, login_url=DEFAULT_URL, delay=DEFAULT_DELAY,
                users=DEFAULT_TEST_USERS, user_id=DEFAULT_USER_ID, pass_id=DEFAULT_PASS_ID,
                logout_id=DEFAULT_LOGOUT_ID):
    failed = []
    success = []

    if not login_url:
        login_url = DEFAULT_URL
    if not delay:
        delay = DEFAULT_DELAY
    if not users:
        users = DEFAULT_TEST_USERS
    if not user_id:
        user_id = DEFAULT_USER_ID
    if not pass_id:
        pass_id = DEFAULT_PASS_ID
    if not logout_id:
        logout_id = DEFAULT_LOGOUT_ID
    if not driver:
        print("Browser not supported")
        return

    print(f"{bcolors.HEADER}===AUTOMATED TESTING FOR LOGINS USING SELENIUM==={bcolors.ENDC}")
    browserName = driver.capabilities["browserName"]
    browserVersion = driver.capabilities["browserVersion"]
    print(f"Automated test will use {bcolors.BOLD} {browserName} V{browserVersion} {bcolors.ENDC} as specified or by "
          f"default.")
    print(f"On webpage {login_url}")

    print(f"{bcolors.UNDERLINE}Empty field test...{bcolors.ENDC}")
    if empty_field_test(driver, pass_id, login_url, delay):
        return

    print(f"{bcolors.UNDERLINE}User login test...{bcolors.ENDC}")
    for user in users:
        print("Login test for ", user)
        driver.get(login_url)
        wait_page(driver, delay)
        inputUser = driver.find_element(By.ID, user_id)
        inputPass = driver.find_element(By.ID, pass_id)
        inputUser.send_keys(user["username"])

        inputPass.send_keys(user["password"])
        inputPass.send_keys(Keys.ENTER)

        if len(driver.find_elements(By.ID, user_id)) == 0:
            print(f"\t{bcolors.OKCYAN}Login successful.{bcolors.ENDC}")
            success.append(user)
            driver.find_element(By.ID, logout_id).click()
            wait_page(driver, delay)
            if len(driver.find_elements(By.ID, user_id)) > 0:
                print(f"\t{bcolors.OKCYAN}Logout successful.{bcolors.ENDC}")
            else:
                print(f"\t{bcolors.FAIL}Logout failed. {bcolors.ENDC}")
        else:
            print(f"\t{bcolors.FAIL}Login failed. {bcolors.ENDC}")
            failed.append(user)
    driver.close()
    print(f"{bcolors.OKGREEN}===AUTOMATED TESTING ENDED SUCCESSFULLY==={bcolors.ENDC}")
    print(f"{len(success)} granted user(s): \n\t", success)
    print(f"{len(failed)} denied user(s): \n\t", failed)
    # input(" \nPress a key to exit.")


def empty_field_test(driver, passid, url, delay):
    driver.get(url)
    wait_page(driver, delay)
    driver.find_element(By.ID, passid).send_keys(Keys.ENTER)

    try:
        driver.find_element(By.ID, passid)
        print(f"\t{bcolors.OKBLUE}Test succeed {bcolors.ENDC}: login denied when fields are empty")
        return 0
    except NoSuchElementException:
        print(f"\t{bcolors.FAIL}Empty field test failed {bcolors.FAIL}: login granted when fields are empty")
        print("END OF TEST")
        return 1


def wait_page(driver, delay):
    try:
        body = WebDriverWait(driver, delay).until(EC.presence_of_element_located((By.TAG_NAME, 'body')))
    except TimeoutException:
        print("Loading took too much time!")


def get_parser():
    parser = argparse.ArgumentParser()
    parser.add_argument("-u", "--url", help="login page URL")
    parser.add_argument("--userid", help="ID attribute of username HTML element")
    parser.add_argument("--passid", help="ID attribute of password HTML element")
    parser.add_argument("-b", "--browser",
                        help="name of the browser used for the automated testing (currently supported: edge (default), chrome, firefox, opera) ")
    parser.add_argument("--driverpath",
                        help="the selenium driver file for the specified browser (default: /driver/msedgedriver.exe)")
    parser.add_argument("-f", "--file", help="the file containing the list of users in json format")
    parser.add_argument("-d", "--delay", help="maximum loading delay in seconds")
    parser.add_argument("--logoutid", help="ID attribute of logout button HTML element")

    return parser


if __name__ == "__main__":
    if len(sys.argv) < 2:
        launch_test(get_driver())
    else:
        args = get_parser().parse_args()
        users_list = None
        if args.file:
            f = open(args.file)
            users_list = json.load(f)["users"]
        if args.browser:
            if not args.driverpath:
                print("you need to specify the path to the selenium driver for the browser using --driverpath")
                exit()
        if args.url:
            exit_script = False
            if not args.userid:
                print("You need to specify the id of the HTML element of username input for this login page using "
                      "--userid")
                exit_script = True
            if not args.passid:
                print("You need to specify the id of the HTML element of password input for this login page using "
                      "--passid")
                exit_script = True
            if not args.logoutid:
                print("You need to specify the id of the HTML element of the logout button for this login page using "
                      "--logoutid")
                exit_script = True
            if exit_script:
                exit()

        launch_test(driver=get_driver(args.browser, args.driverpath), login_url=args.url, delay=args.delay,
                    users=users_list, user_id=args.userid, pass_id=args.passid, logout_id=args.logoutid)
