from selenium.webdriver.common.by import By

from pageobject.BasePage import BasePage


class NavigationPage(BasePage):
    WOMEN_LOCATOR = (By.CSS_SELECTOR, ".menu-content a[title='Women']")

    def __init__(self, driver):
        super().__init__(driver)
        driver.get("http://automationpractice.com/index.php")

    def click_women_tab(self):
        self.driver.find_element(*self.WOMEN_LOCATOR).click()
