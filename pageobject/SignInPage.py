from selenium.webdriver.common.by import By

from pageobject.BasePage import BasePage


class SignInPage(BasePage):
    EMAIL_FIELD = (By.ID, "email")
    PASS_FIELD = (By.ID, "passwd")
    SIGN_IN_BTN = (By.ID, "SubmitLogin")

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def i_sign_in_with(self, username, password):
        super().set_text(self.EMAIL_FIELD, username)
        super().set_text(self.PASS_FIELD, password)
        super().click(self.SIGN_IN_BTN)
