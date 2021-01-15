import time
import urllib.parse
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains


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


class Facebook_Automator:
    options = webdriver.ChromeOptions()
    prefs = {"profile.default_content_setting_values.notifications": 1}
    options.add_experimental_option("prefs", prefs)
    browser = webdriver.Chrome(options=options)

    def login(self, fb_email, fb_password):
        self.browser.get("https://facebook.com")
        accept_all = self.browser.find_element_by_xpath('//*[@id="u_0_h"]')
        accept_all.click()
        email = self.browser.find_element_by_xpath('//*[@id="email"]')
        email.send_keys(fb_email)
        password = self.browser.find_element_by_xpath('//*[@id="pass"]')
        password.send_keys(fb_password)
        login_button = self.browser.find_element_by_xpath('//*[@id="u_0_b"]')
        login_button.click()
        time.sleep(3)

    def find_peoples(self, username):
        self.browser.get("https://www.facebook.com/search/people/?q=" + urllib.parse.quote(username))
        time.sleep(3)

    def find_posts(self, post_name):
        self.browser.get("https://www.facebook.com/search/posts?q=" + urllib.parse.quote(post_name))
        time.sleep(3)

    def find_photos(self, photo_name):
        self.browser.get("https://www.facebook.com/search/photos?q=" + urllib.parse.quote(photo_name))
        time.sleep(3)

    def find_videos(self, video_name):
        self.browser.get("https://www.facebook.com/search/videos?q=" + urllib.parse.quote(video_name))
        time.sleep(3)

    def find_pages(self, page_name):
        self.browser.get("https://www.facebook.com/search/pages?q=" + urllib.parse.quote(page_name))
        time.sleep(3)

    def find_fb_pages(self, page_name):
        self.browser.get("https://www.facebook.com/search/pages?q=" + urllib.parse.quote(page_name))
        time.sleep(3)

    def find_places(self, place_name):
        self.browser.get("https://www.facebook.com/search/places?q=" + urllib.parse.quote(place_name))
        time.sleep(3)

    def find_groups(self, group_name):
        self.browser.get("https://www.facebook.com/search/groups?q=" + urllib.parse.quote(group_name))
        time.sleep(3)

    def facebook_close(self):
        self.browser.close()


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
        first_result = self.browser.find_element_by_xpath("/html/body/div[1]/div/div[1]/div/div[2]/div/div/div[2]/div/div/div[1]/div[1]/div/div/div[1]/ul/div[1]/li/div/a/div/div[2]/div/div/span/span/span")
        first_result.click()
        time.sleep(3)
        message_box = self.browser.find_element_by_xpath("/html/body/div[1]/div/div[1]/div/div[2]/div/div/div[1]/div[1]/div[2]/div/div/div/div/div/div[1]/div[2]/div/div/div/div[2]/div/form/div/div[3]/div[2]/div[1]/div/div")
        message_box.click()
        actions = ActionChains(self.browser)
        actions.send_keys(message)
        actions.perform()
        send_button = self.browser.find_element_by_xpath("/html/body/div[1]/div/div[1]/div/div[2]/div/div/div[1]/div[1]/div[2]/div/div/div/div/div/div[1]/div[2]/div/div/div/div[2]/div/form/div/div[3]/span[2]/div")
        send_button.click()
