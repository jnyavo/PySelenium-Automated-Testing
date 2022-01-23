# PySelenium-Automated-Testing

[![Selenium](https://www.selenium.dev/images/selenium_4_logo.png)](https://www.selenium.dev)
[![Python](https://www.python.org//static/img/python-logo.png)](https://www.python.org)

This python project allows us to automate testing on any login page using selenium.

## Features

- Automated testing on login page
- Add custom user list for automated testing
- Automated testing on different browsers
- Colored text in terminal 

## Prerequisite

### Python selenium package

Selenium package for python is required in order to launch the automated testing script.
Installation scripts are included in the project for windows and linux.

#### Windows

```batch
>cd windows/installation
>Selenium-Installation-Windows.bat
```

#### Linux
```sh
cd linux/installation
./Selenium-installation-linux.sh
```
These installation scripts will work assuming python3 has been installed with the default settings.

The package can be installed manually.

```sh
python3 -m pip --upgrade pip
python3 -m pip install selenium
```

or

```batch
>python.exe -m pip --upgrade pip
>python.exe -m pip install selenium
```

### Selenium driver

Selenium driver for the desired browser is needed in order to launch the automated testing.
The driver must correspond to the version of the installed browser.

The driver for Microsoft Edge Version 97.0.1072.69 is located in /windows/driver


## Usage

In order to launch the automated testing, you only need the Automated_test.py file.
You can access the parameters' information by using the --help argument as shown below.

```
./Automated_testing.py --help
usage: Automated_testing.py [-h] [-u URL] [--userid USERID] [--passid PASSID]
                            [-b BROWSER] [--driverpath DRIVERPATH] [-f FILE]
                            [-d DELAY] [--logoutid LOGOUTID]

options:
  -h, --help            show this help message and exit
  -u URL, --url URL     login page URL
  --userid USERID       ID attribute of username HTML element
  --passid PASSID       ID attribute of password HTML element
  -b BROWSER, --browser BROWSER
                        name of the browser used for the automated testing
                        (currently supported: edge (default), chrome, firefox,
                        opera)
  --driverpath DRIVERPATH
                        the selenium driver file for the specified browser
                        (default: windows/driver/msedgedriver.exe)
  -f FILE, --file FILE  the file containing the list of users in json format
  -d DELAY, --delay DELAY
                        maximum loading delay in seconds
  --logoutid LOGOUTID   ID attribute of logout button HTML element

```
### Default settings

The script can be launched without parameters, it will use the default settings.

```sh
./Automated_testing.py
```
The default settings are defined at the top of the Automated_testing.py python script.

```python
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
```




