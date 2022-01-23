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

- DEFAULT_TEST_USERS : user list used for the test
- DEFAULT_BROWSER : the desired browser name in lowercase
- DEFAULT_DRIVER_PATH : the path to the selenium driver file
- DEFAULT_URL : the URL of the login page
- DEFAULT_DELAY: the timeout value in seconds
- DEFAULT_USER_ID: the id attribute of the username input
- DEFAULT_PASS_ID: the id attribute of the password input
- DEFAULT_LOGOUT_ID : the id attribute of the logout button

These settings can be modified if needed.

#### output example
```
===AUTOMATED TESTING FOR LOGINS USING SELENIUM===
Automated test will use  msedge V97.0.1072.69  as specified or by default.
On webpage http://localhost/Automated_testing/login/
Empty field test...
	Test succeed : login denied when fields are empty
User login test...
Login test for  {'username': 'user', 'password': '1234'}
	Login successful.
	Logout successful.
Login test for  {'username': 'unknown', 'password': 'fgsdgsdg'}
	Login failed. 
Login test for  {'username': 'nyavo', 'password': '1234'}
	Login failed. 
Login test for  {'username': 'darino', 'password': '1234'}
	Login failed. 
===AUTOMATED TESTING ENDED SUCCESSFULLY===
1 granted user(s): 
	 [{'username': 'user', 'password': '1234'}]
3 denied user(s): 
	 [{'username': 'unknown', 'password': 'fgsdgsdg'}, {'username': 'nyavo', 'password': '1234'}, {'username': 'darino', 'password': '1234'}]

```

### Using parameters

This is an example of an automated testing on a login page at www.login-page.com, which has
```html
<input id="username"/>
<input id="password"/> 
	   
```
and

```html
<a id="logout>
```

after login, using chrome browser.


```
./Automated_testing.py -u https://www.login-page.com --userid username --passid password --logoutid logout -b chrome --driverpath /path/to/driver -f /path/to/user/list/users.json -d 10

```

The user list for the testing must be in json format as shown below.

```json
{
  "users": [
    {
      "username": "user",
      "password": "1234"
    },
    {
      "username": "unknown",
      "password": "fgsdgsdg"
    },
    {
      "username": "nyavo",
      "password": "1234"
    },
    {
      "username": "darino",
      "password": "1234"
    }

  ]
}
```

This file can be found in the project : "users.json"

### Colored Text

The output for this script is designed to be colored. However, colored texts are not supported in windows command-line.

To enable colored texts remove the comment quotes on the following code and remove or comment the former class.

```python
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
```

### Rapid test

Assuming the php website at https://github.com/zahrah925/Automated-Testing has been set up correctly on windows 10.

The batch script at windows/rapid-test.bat can be used to test the login using the users.json file.

```batch
>cd /windows
>rapid-test.bat
```
The output of the script will be stored in a file named "Report.txt".

