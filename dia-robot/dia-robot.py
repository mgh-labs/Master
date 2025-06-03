#   Welcome to the document impact assessment robot.
#   Developer: Ryan Miller

#   test_doc_number = 15011413

#   Dependencies and packages
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from pynput.keyboard import Key, Controller
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
import time

#   Enable keyboard as controller.
keyboard = Controller()

#   Set driver/browser as chrome, open Teamcenter.
options = webdriver.ChromeOptions()

#   Supress the error messages/logs.
options.add_experimental_option("excludeSwitches", ["enable-logging"])
options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=options)

#   Non prod TC URL. Replace with prod environment URL before release.
url_teamcenter_home = "N/A"
driver.get(url_teamcenter_home)
driver.maximize_window()

#   Collect Teamcenter username and password from user.
tc_username = str(input("Please enter your Teamcenter username: "))
tc_password = str(input("Please enter your Teamcenter password: "))

#   Enter username into Teamcenter.
xpath_username_input = """//*[@id="main-view"]/form/div/div/div[2]/div/ul/li[1]/input"""
username_input = driver.find_element("xpath", xpath_username_input)
username_input.clear # clear input box
username_input.send_keys(tc_username)

time.sleep(1)

#   Enter password into Teamcenter.
xpath_password_input = """//*[@id="main-view"]/form/div/div/div[2]/div/ul/li[2]/input"""
password_input = driver.find_element("xpath", xpath_password_input)
password_input.clear # clear input box
password_input.send_keys(tc_password)

time.sleep(1)

#   Click sign in.
xpath_signin = """//*[@id="main-view"]/form/div/div/div[2]/div/ul/li[3]/div/div[1]/button"""
signin = driver.find_element("xpath", xpath_signin)
signin.click()

#   Instruct user to allow system to load.
print("Please allow a few moments for the system to load prior to proceedint. Thank you for your patience!")
time.sleep(10)

#   Collect document number(s) from user.
doc_nums = str(input("Please enter the document number(s) (if multiple numbers, please separate with single spaces. ie: 15011413 15013012 15013013): "))

#   ____________________________________________________________________
#   Copied code from auto-revision-generator.py below.

#   Click into search bar.
xpath_homepagesearch = """//*[@id="main-view"]/aw-include/div/div/div[2]/div/div/ui-view/aw-page/div/div/div/div[1]/aw-header/div/div/div[2]/aw-global-search/div/aw-include/div/aw-search-global/div/div[1]/div[1]/div[1]/div[2]/aw-search/div/aw-search-box/div/input"""
homepagesearch = driver.find_element("xpath", xpath_homepagesearch)
homepagesearch.click()
time.sleep(2)

#   Open filter search dropdown.
xpath_filtersearch = """//*[@id="main-view"]/aw-include/div/div/div[2]/div/div/ui-view/aw-page/div/div/div/div[1]/aw-header/div/div/div[2]/aw-global-search/div/aw-include/div/aw-search-global/div/div[1]/div[1]/div[1]/div[1]/div[2]/aw-search-prefilter/aw-listbox/aw-widget/div/div/div/aw-property-val/div/div/aw-property-string-val/div/aw-property-lov-val/div/aw-property-error/div/div/input"""
filtersearch = driver.find_element("xpath", xpath_filtersearch)
filtersearch.click()
time.sleep(2)

#   Select documents.
xpath_filtersearch_documents = """//*[@id="ui-id-2"]/div/div/div/ul/li[3]/aw-property-lov-child/div"""
filtersearch_documents = driver.find_element("xpath", xpath_filtersearch_documents)
filtersearch_documents.click()
time.sleep(2)

#   Enter document number and search.
homepagesearch.send_keys(doc_nums)
time.sleep(2)
homepagesearch.send_keys(Keys.RETURN)
time.sleep(15)

#   ____________________________________________________________________
#   End of copied code from auto-revision-generator.py.

