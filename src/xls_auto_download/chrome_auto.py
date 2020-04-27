import os
import glob
import pyautogui
from time import sleep
from splinter import Browser
from selenium import webdriver

PROXY_HOST = 'http://dc2proxy02.hella.com'  # rotating proxy or host
PROXY_PORT = '3128' # port
PROXY_USER = 'joshke1' # username
PROXY_PASS = 'Monitor$123' # password

# Output file path
Out_File_Path = "C:\\Data\\"

# Output file name
Out_File_Name = Out_File_Path + "covid19-data-responses.xlsx"

# Remove pre-existing xlsx file from the given path
def del_file() :
    filepath = glob.glob("C:\Data\*.xlsx")
    for file in filepath:
        os.remove(file)

# Rename file with new name
def rename_file() :
    filepath = glob.glob("C:\Data\*.xlsx")
    for file in filepath:
        os.rename(file, Out_File_Name)

# For proxy handling
def enter_proxy_auth( proxy_username, proxy_password ):
    sleep(1)
    pyautogui.typewrite(proxy_username)
    pyautogui.press('tab')
    pyautogui.typewrite(proxy_password)
    pyautogui.press('enter')
    return;

# For open webpage
def open_a_page ( browser, url ):
    browser.visit(url)
    return;

# delete pre-existing xls file
del_file()

chrome_options = webdriver.ChromeOptions()

# XLS download path
prefer_ = {'download.default_directory': 'C:\Data',
           'profile.default_content_settings.popups': 0,
           'directory_upgrade': True}

chrome_options.add_experimental_option('prefs', prefer_)
# chrome_options.add_argument("download.default_directory=C:\Data")
chrome_options.add_argument('--proxy-server={}'.format(PROXY_HOST + ":" + PROXY_PORT))
browser = Browser('chrome', options=chrome_options)

# Open Microsoft Form page
open_a_page(browser, "https://forms.office.com/")

# Enter proxy of Hella
enter_proxy_auth(PROXY_USER, PROXY_PASS)
sleep(4)

# Click to sign in button
browser.find_by_xpath('//*[@id="meControl"]/div').click()
sleep(5)

# Enter login email-id
pyautogui.press('tab')
pyautogui.typewrite("covidatahelp@hotmail.com")
pyautogui.press('tab', presses= 2)
pyautogui.press('enter')
sleep(10)

# Enter login password
pyautogui.typewrite("Adas@123")
browser.find_by_xpath('//*[@id="idSIButton9"]').click()
sleep(11)

# Select mention form
browser.find_by_text('POST-COVID19 : EHS Guideline(Test)',wait_time=100).click()
sleep(5)

# Click on response tab and download form by click open excel
browser.find_by_text('Responses',wait_time=100).click()
browser.find_by_text('Open in Excel',wait_time=100).click()
sleep(3)

# close the browser
browser.quit()

# Rename downloaded XLS
rename_file()

print("XLS Downloded here : " + Out_File_Name)
