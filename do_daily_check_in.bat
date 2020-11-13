:: File: do_daily_check_in.bat 
:: Version: 0.1.0 (for MS edge chromium)
:: This batch file is used in case you want to set a windows task scheduler
:: for the daily check-in bot that automatically runs the bot for you
:: in the desired time.
:: Note: make sure that the "msedgedriver.exe", and "script.py" files are in 
:: the same directory as the batch file.

@echo off

:: set the username
set username=%1

:: set the password
set password=%2

:: set MS edge driver file path
set driverPath=%CD%\msedgedriver.exe

:: looks for python launcher, and sets its absolute path on the user's machine
set pythonPath=
for /f "delims=" %%a in ('where python.exe') do @set pythonPath=%%a

:: run the command
"%pythonPath%" "%CD%\script.py" %username% %password% "%driverPath%"