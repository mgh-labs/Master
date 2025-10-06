#  
#
#   Welcome to the auto revision generator
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

# Non prod TC URL. Replace with prod environment URL before release.
url_teamcenter_home = "N/A"
driver.get(url_teamcenter_home)
driver.maximize_window()

#   Prompt user to sign in to PLM system
print("Please sign in to the PLM system if prompted.\nAfter sign in, allow the system 30s to load prior to proceeding. Thanks you for your patience!")
time.sleep(40)

#   Collect document/material number(s) from user
#   Test MN: 20134056
mn_list = str(input("Please enter the document/material number(s) to be revised (if multiple numbers, please separate with single spaces. ie: 15013012 15013013 15013014): "))

#   Determine if CN exists from user
cn_exists = str(input("Is a CN already generated for this revision? Enter 'y' for yes or 'n' for no: "))

#   Generate CN # if CN does not exist
if cn_exists == "n":

    #   Collect change title from user
    #   Test title: Auto Rev Script Test 1.0
    change_title = str(input("Please enter the title of your change: ")) 

    #   Default statements
    detailedreasoning_statement = f"This CN contains the release of a revision to MN {mn_list} for (insert project name/driver for change)."
    detaileddescription_statement = f"Item Revision:\n{mn_list}\n-(Insert specific changes here)"
    justification_statement = "This revision does not impact the design, performance, specifications, effectiveness, or quality of end-products. (insert additional justification if required)"

    #   Click new change button
    xpath_newchange_button = """//*[@id="main-view"]/aw-include/div/div/div[2]/div/div/ui-view/aw-page/div/div/div/div[2]/div/ng-transclude/ui-view/aw-include/div/aw-base-sublocation/aw-sublocation/div/div[2]/div/aw-sublocation-body/aw-tile-canvas/div/div/div/div[1]/aw-tile-group/div[3]/aw-tile"""
    newchange_button = driver.find_element('xpath', xpath_newchange_button)
    newchange_button.click()
    time.sleep(10)

    #   Click change intake button
    xpath_changeintake_button = """//*[@id="aw_toolsAndInfo"]/div/aw-include/div/div/div[2]/div/form/form/form/aw-list/div/div/div/ul/li[1]"""
    changeintake_button = driver.find_element('xpath', xpath_changeintake_button)
    changeintake_button.click()
    time.sleep(2)

    #   Enter title into title box
    xpath_changeintake_title_input = """//*[@id="aw_toolsAndInfo"]/div/aw-include/div/div/div[2]/div/form/form/form[2]/div[2]/form/div/div/div/div/aw-property-text-box-val/aw-property-error/div/input"""
    changeintake_title_input = driver.find_element('xpath', xpath_changeintake_title_input)
    changeintake_title_input.clear # clear input box
    changeintake_title_input.send_keys(change_title)
    time.sleep(2)

    #   Open product impact dropdown
    xpath_changeintake_productimpact_button = """//*[@id="aw_toolsAndInfo"]/div/aw-include/div/div/div[2]/div/form/form/form[2]/div[2]/form/aw-listbox[1]/aw-widget/div/div/div/aw-property-val/div/div/aw-property-string-val/div/aw-property-lov-val/div/aw-property-error/div/div/input"""
    changeintake_productimpact_button = driver.find_element('xpath', xpath_changeintake_productimpact_button)
    time.sleep(2)
    changeintake_productimpact_button.click()
    time.sleep(2)

    #   Select product impact = no 
    changeintake_productimpact_button.send_keys("No")
    time.sleep(2)
    changeintake_productimpact_button.send_keys(Keys.RETURN)
    time.sleep(2)

    #   Open reg purpose dropdown
    xpath_changeintake_regpurpose = """//*[@id="aw_toolsAndInfo"]/div/aw-include/div/div/div[2]/div/form/form/form[2]/div[2]/form/aw-listbox[2]/aw-widget/div/div/div/aw-property-val/div/div/aw-property-array-val/div/div[2]/aw-property-array-edit-val/div/div/aw-property-string-val/div/aw-property-lov-val/div/aw-property-error/div/div/input"""
    changeintake_regpurpose = driver.find_element('xpath', xpath_changeintake_regpurpose)
    changeintake_regpurpose.click()
    time.sleep(2)

    #   Select reg purpose = RUO
    changeintake_regpurpose.send_keys("RUO")
    time.sleep(2)
    changeintake_regpurpose.send_keys(Keys.RETURN)
    time.sleep(2)

    #   Open business purpose dropdown
    xpath_changeintake_businesspurpose = """//*[@id="aw_toolsAndInfo"]/div/aw-include/div/div/div[2]/div/form/form/form[2]/div[2]/form/aw-listbox[3]/aw-widget/div/div/div/aw-property-val/div/div/aw-property-string-val/div/aw-property-lov-val/div/aw-property-error/div/div/input"""
    changeintake_businesspurpose = driver.find_element('xpath', xpath_changeintake_businesspurpose)
    changeintake_businesspurpose.click()
    time.sleep(2)

    #   Select business purpose = On-Market
    changeintake_businesspurpose.send_keys("On-Market")
    time.sleep(2)
    changeintake_businesspurpose.send_keys(Keys.RETURN)
    time.sleep(2)

    #   Open classification path dropdown
    xpath_changeintake_classificationpath = """//*[@id="aw_toolsAndInfo"]/div/aw-include/div/div/div[2]/div/form/form/form[2]/div[2]/form/aw-listbox[4]/aw-widget/div/div/div/aw-property-val/div/div/aw-property-string-val/div/aw-property-lov-val/div/aw-property-error/div/div/input"""
    changeintake_classificationpath = driver.find_element('xpath', xpath_changeintake_classificationpath)
    changeintake_classificationpath.click()
    time.sleep(2)

    #   Select classification path = Fast Track
    changeintake_classificationpath.send_keys("Fast Track")
    time.sleep(2)
    changeintake_classificationpath.send_keys(Keys.RETURN)
    time.sleep(2)

    #   Open business complexity dropdown
    xpath_changeintake_businesscomplexity = """//*[@id="aw_toolsAndInfo"]/div/aw-include/div/div/div[2]/div/form/form/form[2]/div[2]/form/aw-listbox[5]/aw-widget/div/div/div/aw-property-val/div/div/aw-property-string-val/div/aw-property-lov-val/div/aw-property-error/div/div/input"""
    changeintake_businesscomplexity = driver.find_element('xpath', xpath_changeintake_businesscomplexity)
    changeintake_businesscomplexity.click()
    time.sleep(2)

    #   Select business complexity = Low
    changeintake_businesscomplexity.send_keys("Low")
    time.sleep(2)
    changeintake_businesscomplexity.send_keys(Keys.RETURN)
    time.sleep(2)

    #   Select create
    xpath_changeintake_create = """//*[@id="aw_toolsAndInfo"]/div/aw-include/div/div/div[2]/div/form/div/button[5]"""
    changeintake_create = driver.find_element('xpath', xpath_changeintake_create)
    changeintake_create.click()
    time.sleep(15)

#   Open CN if CN exists
if cn_exists == "y":
    
    #   Collect CN # from user
    cn_num = str(input("Please enter the CN #: "))

    #   Open CN in Teamcenter
    #   Test CN #: 1112445
    xpath_homepagesearch = """//*[@id="main-view"]/aw-include/div/div/div[2]/div/div/ui-view/aw-page/div/div/div/div[1]/aw-header/div/div/div[2]/aw-global-search/div/aw-include/div/aw-search-global/div/div[1]/div[1]/div[1]/div[2]/aw-search/div/aw-search-box/div/input"""
    homepagesearch = driver.find_element('xpath', xpath_homepagesearch)
    homepagesearch.click()
    time.sleep(2)

    #   Open filter changes dropdown
    xpath_filtersearch = """//*[@id="main-view"]/aw-include/div/div/div[2]/div/div/ui-view/aw-page/div/div/div/div[1]/aw-header/div/div/div[2]/aw-global-search/div/aw-include/div/aw-search-global/div/div[1]/div[1]/div[1]/div[1]/div[2]/aw-search-prefilter/aw-listbox/aw-widget/div/div/div/aw-property-val/div/div/aw-property-string-val/div/aw-property-lov-val/div/aw-property-error/div/div/input"""
    filtersearch = driver.find_element('xpath', xpath_filtersearch)
    filtersearch.click()
    time.sleep(2)

    #   Select changes
    xpath_filtersearch_changes = """//*[@id="ui-id-1"]/div/div/div/ul/li[2]/aw-property-lov-child/div"""
    filtersearch_changes = driver.find_element('xpath', xpath_filtersearch_changes)
    filtersearch_changes.click()
    time.sleep(2)

    #   Enter CN # and search
    homepagesearch.send_keys(cn_num)
    time.sleep(2)
    homepagesearch.send_keys(Keys.RETURN)
    time.sleep(15)

    #   Open CN step 1
    xpath_open_1 = """//*[@id="Awp0OpenGroup"]"""
    open_1 = driver.find_element('xpath', xpath_open_1)
    open_1.click()
    time.sleep(2)

    #   Open CN step 2
    xpath_open_2 = """//*[@id="Awp0ShowObject"]"""
    open_2 = driver.find_element('xpath', xpath_open_2)
    open_2.click()
    time.sleep(4)

#   Open affected items tab
xpath_affecteditems = """//*[@id="main-view"]/aw-include/div/div/div[2]/div/div/ui-view/aw-showobject-page/div/div/div/div[2]/div/aw-tab-container/div[1]/div[1]/div/aw-tab[2]"""
affecteditems = driver.find_element('xpath', xpath_affecteditems)
affecteditems.click()
time.sleep(2)

#   Open add to current revision items tab
xpath_addcurrentrevisionitems = """//*[@id="Awp0ShowAddObject"]"""
addcurrentrevisionitems = driver.find_element('xpath', xpath_addcurrentrevisionitems)
addcurrentrevisionitems.click()
time.sleep(2)

#   Open add to search bar
xpath_addcurrentrevisionitems_search_tab = """//*[@id="aw_toolsAndInfo"]/div/aw-include/div/aw-include/div/div/div[2]/div/form/aw-add/form/aw-tab-set/aw-tab-container/div[1]/div[1]/div/aw-tab[3]"""
addcurrentrevisionitems_search_tab = driver.find_element('xpath', xpath_addcurrentrevisionitems_search_tab)
addcurrentrevisionitems_search_tab.click()
time.sleep(2)

#   Click search bar
xpath_addcurrentrevisionitems_search_input = """//*[@id="aw_toolsAndInfo"]/div/aw-include/div/aw-include/div/div/div[2]/div/form/aw-add/form/aw-tab-set/div/form[2]/form/aw-search-box/div/input"""
addcurrentrevisionitems_search_input = driver.find_element('xpath', xpath_addcurrentrevisionitems_search_input)
addcurrentrevisionitems_search_input.click()
time.sleep(2)

#   Enter MN and click enter
addcurrentrevisionitems_search_input.send_keys(mn_list)
time.sleep(2)
addcurrentrevisionitems_search_input.send_keys(Keys.RETURN)
time.sleep(15)

#   Select item
xpath_addcurrentrevisionitems_search_selectitem = """//*[@id="resultFilterPanel"]"""
addcurrentrevisionitems_search_selectitem = driver.find_element('xpath', xpath_addcurrentrevisionitems_search_selectitem)
addcurrentrevisionitems_search_selectitem.click()

#   Press add
xpath_addcurrentrevisionitems_search_selectitem_add = """//*[@id="aw_toolsAndInfo"]/div/aw-include/div/aw-include/div/div/div[2]/div/div/button[3]"""
addcurrentrevisionitems_search_selectitem_add = driver.find_element('xpath', xpath_addcurrentrevisionitems_search_selectitem_add)
addcurrentrevisionitems_search_selectitem_add.click()

#   Input MN into search bar


# #   Populate detailed reasoning
# xpath_detailedreasoning = """//*[@id="main-view"]/aw-include/div/div/div[2]/div/div/ui-view/aw-showobject-page/div/div/div/div[3]/div/ng-transclude/aw-xrt-sublocation/aw-sublocation/div/div[2]/div/aw-sublocation-body/div/aw-xrt-2/aw-walker-view/div[2]/aw-walker-element/div[1]/aw-walker-element/div/form/aw-walker-element/div[6]/div/aw-walker-property/aw-widget/div/div/div/aw-property-val/div/div/aw-property-string-val/div/div/aw-property-text-area-val/aw-property-error/div/textarea"""
# detailedreasoning = driver.find_element('xpath', xpath_detailedreasoning)
# detailedreasoning.click()
# time.sleep(2)

# detailedreasoning.send_keys(detailedreasoning_statement)