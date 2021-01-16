import time
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains


class Messenger_Automator:
    options = webdriver.ChromeOptions()
    prefs = {"profile.default_content_setting_values.notifications": 1}
    options.add_experimental_option("prefs", prefs)
    browser = webdriver.Chrome(options=options)

    def login(self, fb_mail, fb_password):
        self.browser.get("https://www.messenger.com/login")
        accept_button = self.browser.find_element_by_xpath('//*[@id="u_0_e"]')
        accept_button.click()
        email = self.browser.find_element_by_xpath('//*[@id="email"]')
        email.send_keys(fb_mail)
        password = self.browser.find_element_by_xpath('//*[@id="pass"]')
        password.send_keys(fb_password)
        login_button = self.browser.find_element_by_xpath('//*[@id="loginbutton"]')
        login_button.click()
        time.sleep(3)

    def send_message(self, username, message):
        search_area = self.browser.find_element_by_xpath(
            "/html/body/div[1]/div/div[1]/div/div[2]/div/div/div[1]/div[1]/div[1]/div/div/div/div[2]/div/div/div/div/label/input")
        search_area.send_keys(username)
        time.sleep(5)
        first_result = self.browser.find_element_by_xpath(
            "/html/body/div[1]/div/div[1]/div/div[2]/div/div/div[2]/div/div/div[1]/div[1]/div/div/div[1]/ul/div[1]/li/div/a/div/div[2]/div/div/span/span/span")
        first_result.click()
        time.sleep(3)
        message_box = self.browser.find_element_by_xpath(
            "/html/body/div[1]/div/div[1]/div/div[2]/div/div/div[1]/div[1]/div[2]/div/div/div/div/div/div[1]/div[2]/div/div/div/div[2]/div/form/div/div[3]/div[2]/div[1]/div/div")
        message_box.click()
        actions = ActionChains(self.browser)
        actions.send_keys(message)
        actions.perform()
        send_button = self.browser.find_element_by_xpath(
            "/html/body/div[1]/div/div[1]/div/div[2]/div/div/div[1]/div[1]/div[2]/div/div/div/div/div/div[1]/div[2]/div/div/div/div[2]/div/form/div/div[3]/span[2]/div")
        send_button.click()
