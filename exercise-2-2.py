###
# Testcase: Test Lively Flip 'Learn More' button
# Goal:
#  Provide code for an automated test that clicks the bottommost "Learn More" button on https://www.greatcall.com/
#
#  A complete submission will:
#
#   Assert that a "Learn More" button exists at the bottom of the page
#   Click the button
#

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


greatcall_page_title = 'Senior Cell Phones, Medical Alert Systems & Safety for Seniors'

support_page_title = "Customer Support | Product Support | GreatCall"
button_class_learn_more_support = "btn btn-lg  btn-primary"
xpath_button_class_learn_more_support = "//div[@id='Contentplaceholder1_C030_Col00']//a[@class='" + button_class_learn_more_support + "']"


browser = webdriver.Chrome()

browser.get('https://www.greatcall.com/')
assert greatcall_page_title in browser.title


# Find and click Support 'Learn More' button
elem_learn_more_support_button = browser.find_element(By.XPATH, xpath_button_class_learn_more_support)  # Find the Support 'Learn More' button
print(elem_learn_more_support_button.get_attribute('href')) # debug print
elem_learn_more_support_button.click

# Confirm we navigated to Support page
assert support_page_title in browser.title

browser.quit()

