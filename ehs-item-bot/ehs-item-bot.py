#  
#
#   Welcome to the ehs item bot
#   Developed by Ryan Miller

#   Dependencies and packages
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from pynput.keyboard import Key, Controller
from selenium.webdriver.common.keys import Keys
import time

#   Enable keyboard as controller
keyboard = Controller()

#   Set driver/browser as chrome, open Teamcenter
options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=options)

#   IMPORTANT: Non prod TC URL. Replace with prod environment URL before release.
url_teamcenter_home = "N/A"
driver.get(url_teamcenter_home)
driver.maximize_window()

#   Prompt user to sign in to PLM system
print("Please sign in to the PLM system if prompted.\nAfter sign in, allow the system 30s to load prior to proceeding. Thanks you for your patience!")
time.sleep(35)

#   Collect eng item number from user
#   Test MN: 20131781
mn = str(input("Please enter the engineering item requiring EHS BOM creation: "))

#   Open filter search category dropdown
xpath_click1 = """//*[@id="main-view"]/aw-include/div/div/div[2]/div/div/ui-view/aw-page/div/div/div/div[1]/aw-header/div/div/div[2]/aw-global-search/div/aw-include/div/aw-search-global/div/div[1]/div[1]/div[1]/div[1]/div[2]/aw-search-prefilter/aw-listbox/aw-widget/div/div/div/aw-property-val/div/div/aw-property-string-val/div/aw-property-lov-val/div/aw-property-error/div/div/input"""
click1 = driver.find_element('xpath', xpath_click1)
click1.click()
time.sleep(1)

#   Select items
xpath_click2 = """//*[@id="ui-id-2"]/div/div/div/ul/li[4]"""
click2 = driver.find_element('xpath', xpath_click2)
click2.click()
time.sleep(1)

#   Click into search bar
xpath_click3 = """//*[@id="main-view"]/aw-include/div/div/div[2]/div/div/ui-view/aw-page/div/div/div/div[1]/aw-header/div/div/div[2]/aw-global-search/div/aw-include/div/aw-search-global/div/div[1]/div[1]/div[1]/div[2]/aw-search/div/aw-search-box/div/input"""
click3 = driver.find_element('xpath', xpath_click3)
click3.click()
time.sleep(1)

#   Enter MN and press enter
click3.send_keys(mn)
time.sleep(1)
click3.send_keys(Keys.RETURN)
time.sleep(10)

#   Open MN step 1
xpath_click4 = """//*[@id="Awp0OpenGroup"]"""
click4 = driver.find_element('xpath', xpath_click4)
click4.click()
time.sleep(1)

#   Open MN step 2
xpath_click5 = """//*[@id="Awp0ShowObject"]"""
click5 = driver.find_element('xpath', xpath_click5)
click5.click()
time.sleep(4)

#   Open BOM
xpath_click6 = """//*[@id="main-view"]/aw-include/div/div/div[2]/div/div/ui-view/aw-showobject-page/div/div/div/div[2]/div/aw-tab-container/div[1]/div[1]/div/aw-tab[5]/li"""
click6 = driver.find_element('xpath', xpath_click6)
click6.click()
time.sleep(10)

#   Open view dropdown
xpath_click7 = """//*[@id="Awp0ModelObjListDisplayToggles"]"""
click7 = driver.find_element('xpath', xpath_click7)
click7.click()
time.sleep(1)

#   Select tree
xpath_click8 = """//*[@id="Awp0ShowTableSummaryView"]"""
click8 = driver.find_element('xpath', xpath_click8)
click8.click()
time.sleep(1)

#   Select tree
xpath_click8 = """//*[@id="Awp0ShowTableSummaryView"]"""
click8 = driver.find_element('xpath', xpath_click8)
click8.click()
time.sleep(1)