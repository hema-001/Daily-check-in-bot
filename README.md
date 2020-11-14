# Daily check-in bot

![GitHub pull request check contexts](https://img.shields.io/github/status/contexts/pulls/hema-001/Daily-check-in-bot/2)

The daily check-in platform is a countermeasure conducted by ZJNU following the events of COVID-19 to observe their students' daily health condition by requiring them to complete an online survey. However, the **daily check-in bot** is a counter-countermeasure for the cumbersome process of checking-in daily by utilizing [selenium](https://www.selenium.dev/) framework.

# Features!
  - One command, automated check-in process
  - Batch file to create Windows task scheduler

# New features!
**TBA**
# To do
  - [ ] Support for Mac OS
  - [ ] Supoort for Linux
  - [ ] Support for different browsers
  - [ ] Write more documentation

# Requirements
In order to run this bot you'll need the following:
> - [Python](https://www.python.org/downloads/) 2.7 or higher
> - [Install selenium package for python](#Install-selenium-package-for-python)
> - [Web driver manager](#Web-driver-manager)
> - Web browser according to the desired web driver manager

## Install selenium package for python
After you have successfully installed Python on your machine, you should be able to run the following command on your Windows command prompet:
```sh
> pip install selenium
```
## Web driver manager
##### Before you download
make sure to find your correct build number: 
- **Launch** Microsoft Edge. 
- **Open** the Settings and more (*"..." menu on top right cornenr of the browser*)
- **Choose** Help and feedback 
- and then choose About Microsoft Edge. 

Download the correct [Microsoft WebDriver version](https://developer.microsoft.com/en-us/microsoft-edge/tools/webdriver/) for your build of Microsoft Edge.
Having the correct version of WebDriver for your build ensures it runs correctly.

# Running
#### Running the script
Running the script itself requires three arguments, `username`, `password`, and `driverPath`. The syntax is as follows:
```
python [username] [password] [driverPath]
```
`driverPath` is the absolute path of the web driver file (if the file is in a different location than the script, e.g., D:\dir1\webDriverFile.exe and the script in D:\dir2\script.py),
```sh
> python usernameStr passStr D:\dir1\webDriverFile.exe
```
Or the web driver file name, in case the file is in the same working directory.
```sh
> python usernameStr passStr webDriverFile.exe
```
#### Running the batch
Runnig the batch file requires only two arguments, `username` and `password`.
For the third argument `driverPath`, the batch file is going to locate the web driver on the same working directory(Make sure to put the web driver executable in the same working directory) and provide it in running the script command arguments.

You can run the script file as follows:
```sh
> do_daily_check_in.bat [username] [password]
```

The reason behind this design is that we want to enable the user to set a task scheduler using the batch file with as less overhead as possible.
Only providing username and password to a task schedluer program is much more convenient than providing a path to a file as well. By letting the batch file do the cumbersome task of providing a correct absolute file path, we can guarantee a minimum error levels that gives the user less problems while setting the daily task.
### Releases 
![GitHub release (latest by date)](https://img.shields.io/github/v/release/hema-001/Daily-check-in-bot) 

#### All releases 

* [MS edge chromium](https://github.com/hema-001/Daily-check-in-bot/releases/tag/v0.1.0)
* [MS edge chromium-latest](https://github.com/hema-001/Daily-check-in-bot/releases/tag/v0.1.1)

![GitHub](https://img.shields.io/github/license/hema-001/Daily-check-in-bot)

