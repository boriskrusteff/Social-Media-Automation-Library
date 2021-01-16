import time
import urllib.parse
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


class Instagram_Automator:
    options = webdriver.ChromeOptions()
    prefs = {"profile.default_content_setting_values.notifications": 1}
    options.add_experimental_option("prefs", prefs)
    browser = webdriver.Chrome(options=options)

    def login(self, emailz, passwordz):
        self.browser.get("https://instagram.com")
        accept_button = self.browser.find_element_by_xpath("/html/body/div[2]/div/div/div/div[2]/button[1]")
        accept_button.click()
        email = self.browser.find_element_by_xpath(
            "/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div/div[1]/div/label/input")
        email.send_keys(emailz)
        password = self.browser.find_element_by_xpath(
            "/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div/div[2]/div/label/input")
        password.send_keys(passwordz)
        login_button = self.browser.find_element_by_xpath(
            "/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div/div[3]")
        login_button.click()
        time.sleep(5)
        no_button = self.browser.find_element_by_xpath("/html/body/div[1]/section/main/div/div/div/div/button")
        no_button.click()
        time.sleep(5)

    def find_person(self, person):
        self.browser.get("https://www.instagram.com/" + urllib.parse.quote(person))
        time.sleep(5)
        message_button = self.browser.find_element_by_xpath("/html/body/div[1]/section/main/div/header/section/div[1]/div[1]/div/div[1]/div/button")
        message_button.click()
        time.sleep(3)

    def send_message(self, message):
        message_area = self.browser.find_element_by_xpath("/html/body/div[1]/section/div/div[2]/div/div/div[2]/div[2]/div/div[2]/div/div/div[2]/textarea")
        message_area.send_keys(message)
        message_area.send_keys(Keys.ENTER)
        time.sleep(2)

    def exit_instagram(self):
        self.browser.close()
