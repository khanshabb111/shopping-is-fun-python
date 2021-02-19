from selenium.webdriver.common.by import By

from pageobject.BasePage import BasePage


class MyAccountPage(BasePage):
    TITLE_LOCATOR = (By.CLASS_NAME, "page-heading")

    def __init__(self, driver):
        super().__init__(driver)

    def get_account_page_title(self):
        return super().get_text(self.TITLE_LOCATOR)
