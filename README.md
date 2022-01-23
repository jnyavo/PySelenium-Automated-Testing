# PySelenium-Automated-Testing

[![N|Solid](https://www.python.org//static/img/python-logo.png)](https://www.python.org)
![](https://upload.wikimedia.org/wikipedia/commons/9/9f/Selenium_logo.svg)(https://www.python.org)

This python project allows us to automate testing on any login page using selenium.


```
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
