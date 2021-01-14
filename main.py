import time
import urllib.parse
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


class Instagram_Automator:
    browser = webdriver.Chrome()
    browser.get("https://instagram.com")

    def login(self, emailz, passwordz):
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
        no2_button = self.browser.find_element_by_xpath("/html/body/div[4]/div/div/div/div[3]/button[2]")
        no2_button.click()

    def find_person(self, person):
        self.browser.get("https://www.instagram.com/" + urllib.parse.quote(person))
        time.sleep(5)
        message_button = self.browser.find_element_by_xpath(
            "/html/body/div[1]/section/main/div/header/section/div[1]/div[1]/div/div[1]/div/button")
        message_button.click()
        time.sleep(3)

    def send_message(self, message):
        message_area = self.browser.find_element_by_xpath(
            "/html/body/div[1]/section/div/div[2]/div/div/div[2]/div[2]/div/div[2]/div/div/div[2]/textarea")
        message_area.send_keys(message)
        message_area.send_keys(Keys.ENTER)
        time.sleep(2)

    def exit_instagram(self):
        self.browser.close()


messages = ("тест2", "Как си Алекс", "???")
alex = Instagram_Automator()
alex.login("boris@krusteff.com", "falcon1312")
alex.find_person("alex_3618")
for i in range(len(messages)):
    alex.send_message(messages[i])
alex.exit_instagram()

