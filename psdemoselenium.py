from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep

driver = webdriver.Chrome(executable_path='/home/ravijaya/drivers/chromedriver')
driver.get('http://www.python.org')
assert 'Python' in driver.title

element = driver.find_element_by_name('q')
element.clear()
element.send_keys('pycon')
element.send_keys(Keys.ENTER)

assert 'No result Found' not in driver.page_source
sleep(10)
driver.close()
