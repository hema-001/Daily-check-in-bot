@echo off

:: File: do_daily_check_in.bat 
:: Version: 0.2.0 
:: This batch file is used in case you want to set a windows task scheduler
:: for the daily check-in bot that automatically runs the bot for you
:: in the desired time.
:: Note: make sure that the web driver file and script file in 
:: the same directory as the batch file.

:: set the username
set username=%1

:: set the password
set password=%2

:: set the flag option
set flag=%3

:: default flag value, if the user didn't specify a driver, google chrome is used
IF NOT DEFINED flag set flag="-g" && set driverPath="chromedriver.exe" && goto next

:: set driver file path according to the flag option
IF "%flag%"=="-g" set driverPath="chromedriver.exe" 
IF "%flag%"=="-e" set driverPath="msedgedriver.exe"

:next
:: if the driver file doesn't exist in the same directory exist batch.
IF exist %driverPath% (
	ECHO driver found = %driverPath% 
	)ELSE (
		echo no matching drivers in current directory.
		exit /B 1
		)

:: looks for python launcher, and sets its absolute path on the user's machine
set pythonPath=
for /f "delims=" %%a in ('where python.exe') do @set pythonPath=%%a

:: run the command
"%pythonPath%" "script.py" %username% %password% %flag% "%driverPath%"
