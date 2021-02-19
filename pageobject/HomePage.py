from selenium.webdriver.common.by import By

from pageobject.BasePage import BasePage


class HomePage(BasePage):
    SIGN_IN_LOCATOR = (By.CLASS_NAME, "login")
    FIRST_POPULAR_ITEM_BY = (By.CSS_SELECTOR, "a[title='Faded Short Sleeve T-shirts'][itemprop='url']>img")

    def __init__(self, driver):
        super().__init__(driver)

    def click_sign_in_btn(self):
        super().click(self.SIGN_IN_LOCATOR)

    def click_add_first_popular_item(self):
        elements = super().find_elements_by(self.FIRST_POPULAR_ITEM_BY)
