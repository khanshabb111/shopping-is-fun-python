import unittest

from selenium import webdriver

from pageobject.HomePage import HomePage
from pageobject.MyAccountPage import MyAccountPage
from pageobject.SignInPage import SignInPage


class NavigationTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(executable_path='../lib/chromedriver.exe')
        self.driver.get("http://automationpractice.com/index.php")

    def test_email(self):
        driver = self.driver

        HomePage(driver).click_sign_in_btn()
        sign_in_page = SignInPage(driver)
        sign_in_page.i_sign_in_with("daisydove@gmail.com", "daisydove")
        my_account_page = MyAccountPage(driver)
        self.assertEqual(my_account_page.get_account_page_title(), "MY ACCOUNT", "Title Did not match as expected")
