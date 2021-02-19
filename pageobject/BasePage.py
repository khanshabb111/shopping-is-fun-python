from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import WebDriverWait


class BasePage(object):

    def __init__(self, driver):
        self.driver = driver

    def __setText__(self, locator, value):
        WebDriverWait(self.driver, 1000) \
            .until(lambda driver: driver.find_element(locator))
        element = self.driver.find_element()
        element.clear()
        element.send_keys(value)

    def click(self, by_locator):
        WebDriverWait(self.driver, 10) \
            .until(ec.element_to_be_clickable(by_locator)).click()

    def set_text(self, locator, value):
        element = WebDriverWait(self.driver, 10) \
            .until(ec.visibility_of_element_located(locator))
        element.clear()
        element.send_keys(value)

    def get_text(self, locator):
        element = WebDriverWait(self.driver, 10) \
            .until(ec.visibility_of_element_located(locator))
        return element.text

    def find_elements_by(self, locator):
        return WebDriverWait(self.driver, 10) \
            .until(ec.visibility_of_all_elements_located(locator))
