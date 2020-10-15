import pytest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep
driver_path = open('driver.cnf').read()

@pytest.fixture()
def selenium_driver():
    driver = webdriver.Chrome(executable_path=driver_path)  # setUp
    yield driver
    driver.close()  # tearDown


class TestPythonOrg:
    def test_title(self, selenium_driver):
        selenium_driver.get('http://python.org')
        assert 'Python' in selenium_driver.title

    def test_search_result(self, selenium_driver):
        selenium_driver.get('http://python.org')
        element = selenium_driver.find_element_by_name('q')
        element.clear()
        element.send_keys('pycon')
        element.send_keys(Keys.ENTER)
        assert 'No result Found' not in selenium_driver.page_source
