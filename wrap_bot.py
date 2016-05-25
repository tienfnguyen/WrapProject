from selenium import webdriver
# from selenium.common.exceptions import TimeoutException
# from selenium.webdriver.support.ui import WebDriverWait # available since 2.4.0
# from selenium.webdriver.support import expected_conditions as EC # available since 2.26.0
import time

bot = webdriver.Firefox()
bot.get('https://wrap.co')

login_button = bot.find_element_by_link_text('LOG IN')
login_button.click()
time.sleep(5)

signup_button = bot.find_element_by_link_text('SIGNUP FOR WRAP AUTHORING')
signup_button.click()
time.sleep(5)

smb_button = bot.find_element_by_link_text('TRY SMALL BUSINESS FOR FREE')
smb_button.click()
time.sleep(5)

email_box = bot.find_element_by_tag_name('input')
email_box.send_keys('testuser11235@gmail.com')
email_box.submit()
time.sleep(5)

inputs = bot.find_elements_by_tag_name('input')
inputs[-2].send_keys('testuser11235')
inputs[-1].send_keys('P@ssword1!')

buttons = bot.find_elements_by_tag_name('button')
for button in buttons:
    if button.text.find('CREATE ACCOUNT') != -1:
        button.click()
        time.sleep(10)
        button.click()
        break

inputs = bot.find_elements_by_tag_name('input')
inputs[0].send_keys('test')
inputs[1].send_keys('user1123')
inputs[2].send_keys('test company 1123')

buttons = bot.find_elements_by_tag_name('button')
for button in buttons:
    if button.text.find('CREATE ACCOUNT') != -1:
        button.click()
        time.sleep(10)
        button.click()
        break
