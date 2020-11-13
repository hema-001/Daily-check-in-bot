# Daily check-in bot

build badge

****
The daily check-in platform is a countermeasure conducted by ZJNU following the events of COVID-19 to observe their students' daily health condition by requiring them to complete an online survey. However, the daily check-in bot is a counter-countermeasure for the cumbersome process of checking-in daily by utilizing [selenium](https://www.selenium.dev/) framework.

# Features!
****
  - One command, automated check-in process
  - Batch file to create Windows task scheduler

# New features!
****
**TBA**
# To do
****
  - [ ] Support for Mac OS
  - [ ] Supoort for Linux
  - [ ] Support for different browsers

# Requirements
****
In order to run this bot you'll need the following:
> - [Python](https://www.python.org/downloads/) 2.7 or higher
> - [Install selenium package for python](#Install-selenium-package-for-python)
> - [Web driver manager](#Web-driver-manager)
> - Web browser according to the desired web driver manager

## Install selenium package for python
****
After you have successfully installed Python on your machine, you should be able to run the following command on your Windows command prompet:
```sh
> pip install selenium
```
## Web driver manager
****


##### Before you download
make sure to find your correct build number: 
- **Launch** Microsoft Edge. 
- **Open** the Settings and more (*"..." menu on top right cornenr of the browser*)
- **Choose** Help and feedback 
- and then choose About Microsoft Edge. 

Download the correct [Microsoft WebDriver version](https://developer.microsoft.com/en-us/microsoft-edge/tools/webdriver/) for your build of Microsoft Edge.
Having the correct version of WebDriver for your build ensures it runs correctly.

# Running
****
Running the script itself requires three arguments, username, password, and the web driver path/name. The syntax is as follows:
```
python [username] [password] [path]
```
The username is the student ID, password is student's passport, path is the absolute path of the web driver file (if the file is in a different location than the script, e.g., D:\dir1\webDriverFile.exe and the script in D:\dir2\script.py),
```sh
> python usernameStr passStr D:\dir1\webDriverFile.exe
```
Or the web driver file name in case the file is in the same working directory.
```sh
> python usernameStr passStr webDriverFile.exe
```
### Releases 
Latest release
![GitHub release (latest by date)](https://img.shields.io/github/v/release/hema-001/Daily-check-in-bot)
All releases
* [MS edge chromium-latest](https://github.com/hema-001/Daily-check-in-bot/releases/tag/v0.1.0)
![GitHub](https://img.shields.io/github/license/hema-001/Daily-check-in-bot)

