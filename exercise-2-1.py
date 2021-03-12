###
# Testcase: Test Lively Flip 'Learn More' button
# Goal:
#   Provide code for an automated test that clicks Lively flip "Learn More" button on https://www.greatcall.com. The code provided can be for an automated test using the tool and language of your choice (Selenium, etc.).
#
#   A complete submission will:
#     Locate the lively Flip "Learn More" button on the page
#     Click the button
#

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


greatcall_page_title = 'Senior Cell Phones, Medical Alert Systems & Safety for Seniors'
lively_flip_page_title = "Lively Flip | Best Basic Big Button Cell Phone for Seniors | GreatCall"
button_class_lively_flip = "btn btn-lg btn-primary product-spotlight-btn hidden-xxs hidden-xs hidden-sm hidden-sticky"
xpath_button_class_lively_flip = "//div[@id='Contentplaceholder1_C191_Col01']//a[@class='" + button_class_lively_flip + "']"


browser = webdriver.Chrome()

browser.get('https://www.greatcall.com/')
assert greatcall_page_title in browser.title


# Find and click Lively Flip 'Learn More' button
elem_learn_more_lively_flip_button = browser.find_element(By.XPATH, xpath_button_class_lively_flip)  # Find the Lively Flip 'Learn More' button
print(elem_learn_more_lively_flip_button.get_attribute('href')) # debug print
elem_learn_more_lively_flip_button.click

# Confirm we navigated to Lively FLip page
assert lively_flip_page_title in browser.title

browser.quit()
