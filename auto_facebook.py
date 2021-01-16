import time
import urllib.parse
from selenium import webdriver


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

    def find_places(self, place_name):
        self.browser.get("https://www.facebook.com/search/places?q=" + urllib.parse.quote(place_name))
        time.sleep(3)

    def find_groups(self, group_name):
        self.browser.get("https://www.facebook.com/search/groups?q=" + urllib.parse.quote(group_name))
        time.sleep(3)

    def exit_facebook(self):
        self.browser.close()
