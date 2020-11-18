"""
File: script.py
Version: 0.2.0
Homepage: https://github.com/hema-001/Daily-check-in-bot

This script automate the daily check-in process conducted by ZJNU students 
living in China.

The daily check-in platform requires the students to login with their student
ID and password(Normally, the password is the last 6 digits of their passport
number). Then the student selects the "Daily Check-in" option from the top 
nav-bar. If the user already did fill in the daily check-in form, a message 
notifying the user will be shown and a back button to go back to the main page
is provided. If he/she did not fill in the form then a "Fill in" button will 
be shown.
Clicking the "Fill in" button will redirect the student to the check-in form.
After the student fill in the form, he/she should click on the confirmation 
radio button at the end of the form before the save and submit button, then 
click on save, and confirm with the popup message.

This script saves the repetitive daily process of loging in and scrolling down 
the form, then click the confirmation radio button and submit the form by 
making it possible to be done with only one-click.

Written by,
IBRAHIM M.I. ISMAIL

DESCLAIMER: the script should be used only if the student feels well and in a 
good health. Otherwise, the student should fill in the form according to his 
current health condition and traveling situation.
"""
import sys
from selenium import webdriver
from msedge.selenium_tools import Edge, EdgeOptions
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, TimeoutException, WebDriverException

if len(sys.argv) <= 3:
	
	print('Invalid input: the command must have the following args: python script.py <username> <password> <driverPath>')
	exit()

else:
	
	usernameStr = sys.argv[1]
	passwordStr = sys.argv[2]
	flag = sys.argv[3]
	driverPath = sys.argv[4]

	## flag options 
	if flag == "-g":
		try:
			print(driverPath)
			browser = webdriver.Chrome(driverPath)

		except WebDriverException as err:
			print(err)
			exit()

	elif flag == "-e":
		try:
			## Launch Microsoft Edge (Chromium)
			options = EdgeOptions()
			options.use_chromium = True
			browser = Edge(driverPath, options = options)
	
		## If the user provides a wrong webdriver name.
		except WebDriverException as err:
			if "executable needs to be in PATH" in str(err):
				print("\"{}\" doesn't exists, make sure you have typed the correct web driver name or path".format(driverPath))
			exit()
	
	
	##enter the daily check-in website
	browser.get(('http://zyt.zjnu.edu.cn/H5/Login.aspx?op=phone_html5'))
	print('Openning website...')
	
	##find the username text and write the given username above
	print('Typing username and password...')
	username = browser.find_element_by_id('UserText')
	username.send_keys(usernameStr)

	##find the password text and write the given password above
	password = browser.find_element_by_id('PasswordText')
	password.send_keys(passwordStr)

	##find the login button and click it
	loginBtn = browser.find_element_by_id('btn_Login')
	loginBtn.click()
	print('Validating...')

	##wait until the daily check-in option appears on the page then click it
	try:
		WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.ID, '健康打卡')))
		clickFillForm = browser.find_element_by_xpath('//ul/li[2]')
		print('Openning form page...')
		clickFillForm.click()

		##if the user did not fill in the form for the day, continue, else close the browser
		continueToFillForm = WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.ID, 'submit')))
		print('Redirecting to form page...')
		fillInBtn = browser.find_elements_by_xpath("//button[@id='submit'][@style='display:;']")

		if len(fillInBtn) == 0:
		    
		    print('You have already checked in today!.')
		    print('Terminated.')
		    browser.quit()

		else:        
		    ##find the Fill in button in the redirect page
		    
		    fillInBtn[0].click()
		    
		    ##wait until the confirmation radio button appears and click it
		    submitForm = WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.ID, 'DATA_15')))
		    print('Filling and submitting the form...')
		    clickConfirmationRadioBtn = browser.find_element_by_id('DATA_15')
		    clickConfirmationRadioBtn.click()
		    
		    ##find save button and click
		    saveBtn = browser.find_element_by_id('btn_save')
		    saveBtn.click()
		    
		    ##wait and click on the confirmation button
		    waitForPopup = WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.CLASS_NAME, 'mui-popup-buttons')))
		    print('Confirming...')
		    confirmData = browser.find_element_by_class_name('mui-popup-buttons')
		    confirmData.click()
		    print('Checked in successfully!.')
		    browser.quit()
		    exit()

	## In case the password/username is wrong it will wait for sometime, if the website 
	## hasn't advanced, quit browser and report.
	except TimeoutException:
	
		print('Invalid username or password: make sure you wrote the correct credentials')
		print('Terminated.')
		browser.quit()
		exit()
