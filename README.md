# Daily check-in bot

![GitHub pull request check contexts](https://img.shields.io/github/status/contexts/pulls/hema-001/Daily-check-in-bot/2) ![GitHub](https://img.shields.io/github/license/hema-001/Daily-check-in-bot) ![GitHub release (latest by date)](https://img.shields.io/github/v/release/hema-001/Daily-check-in-bot) 

The daily check-in platform is a countermeasure conducted by ZJNU following the events of COVID-19 to observe their students' daily health condition by requiring them to complete an online survey. However, the **daily check-in bot** is a counter-countermeasure for the cumbersome process of checking-in daily by utilizing [selenium](https://www.selenium.dev/) framework.

# Disclaimer
The script should be used only if the student is feeling well and his current location is around the school. Otherwise, the student should fill in the form according to his current health condition and traveling situation. 
The author is **not responsible** for any misusage of the script.

# Features!
  - One command, automated check-in process
  - Batch file to create Windows task scheduler
  - Multiple support for different web drivers

# To do
  - [ ] Support for Mac OS
  - [ ] Supoort for Linux
  - [x] Support for different browsers
  - [x] Write more documentation

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
make sure to find your correct MS edge chromium browser build number: 
- **Launch** Microsoft Edge. 
- **Open** the Settings and more (*"..." menu on top right cornenr of the browser*)
- **Choose** Help and feedback 
- and then choose About Microsoft Edge. 

Or, if you are using Google chrome you can check your browser version in the sam fashion as well.

Download the correct [Microsoft WebDriver version](https://developer.microsoft.com/en-us/microsoft-edge/tools/webdriver/) for your build of Microsoft Edge.
Or, if you prefer Google chrome, Download the correct [Google Chrome driver version](https://chromedriver.chromium.org/downloads) for your build of Google chrome. 
Having the correct version of WebDriver for your build ensure it runs correctly.

# Running
#### Running the script
Running the script itself requires four arguments, `username`, `password`, `flag`, and `driverPath`. The syntax is as follows:
```
python [username] [password] [flag] [driverPath]
```
`flag` is either `-e` followed by the `driverPath` of MS edge driver, Or `-g` followed by the `driverPath` of Google chrome driver.
`driverPath` is the absolute path of the web driver file (if the web driver file in a different location than the script, e.g., `D:\dir1\webDriverFile.exe` and the script in `D:\dir2\script.py`),
```sh
> python usernameStr passStr -g D:\dir1\chromedriver.exe
```
Or the web driver file name, in case the file is in the same working directory.
```sh
> python usernameStr passStr -e msedgedriver.exe
```
#### Running the batch
Runnig the batch file requires only two arguments, `username` and `password`, the default running web driver is Google chrome. However, you can optionally specify which web driver you would like to use by providing a third `flag` argument as the last argument of the command.
The batch file is going to locate the web driver in the same working directory (Make sure to put the web driver executable in the same working directory) and provide it when running the script command.

**Note**: You don't have to provide the driver path when running the batch file, by default Google chrome driver is used, or you can provide `-e` to run using MS edge.

You can run the script file as follows:
```sh
> do_daily_check_in.bat [username] [password] opt[-e|-g]
```

For example, running the batch using google chrome driver you can issue the following:
 ```sh
 do_daily_check_in.bat usernameStr passStr 
 ```
Not specifying a `flag` argument will run the batch file using Google chrome driver.

While you can also add `-e` to run using MS edge driver like the following:
 ```sh
 do_daily_check_in.bat usernameStr passStr -e
 ```

The reason behind this design is that we want to enable the user to set a task scheduler using the batch file with as less overhead as possible.
Only providing username and password to a task schedluer program is much more convenient than providing a path to a file as well. By letting the batch file do the cumbersome task of providing a correct absolute file path, we can guarantee a minimum error levels that gives the user less problems while setting the daily task.
### Releases 
#### All releases 

* [Daily check-in botv0.2.0_msedge_chromium_and_google_chrome](https://github.com/hema-001/Daily-check-in-bot/releases/tag/v0.2.0)
* [Daily check-in botv0.1.2_msedge_chromium](https://github.com/hema-001/Daily-check-in-bot/releases/tag/v0.1.2)
* [Daily check-in botv0.1.1_msedge_chromium](https://github.com/hema-001/Daily-check-in-bot/releases/tag/v0.1.1)
* [Daily check-in botv0.1.0_msedge_chromium](https://github.com/hema-001/Daily-check-in-bot/releases/tag/v0.1.0)

## Report a bug
To report a bug go to "Issues", click on "New issue", You'll find a ready "bug report" template select it and follow the template.

## How to contribute
First, make sure that you carefully read the [Code of Conduct](https://github.com/hema-001/Daily-check-in-bot/blob/main/CODE_OF_CONDUCT.md) of this project and you understand it clearly.
Then, You can contribute simply by following the standard Feature Branch Workflow [see this helpful tutorial](https://www.atlassian.com/git/tutorials/comparing-workflows/feature-branch-workflow) to understand how it works. 
**Note**: you may want to change the word "master" whenever encountered in the above tutorial with "main", since github changed the name of the parent repo from "master" to "main" recently.
