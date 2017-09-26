# -*- coding: utf-8 -*

# from selenium import webdriver


class BasePage(object):

    def __init__(self, driver):
        self.driver = driver

    def find_element(self, *locator):
        return self.driver.find_element(*locator)

    def find_elements(self, *locator):
        return self.driver.find_elements(*locator)

    def get_url(self):
        return self.driver.current_url

    def open(self, url):
        self.driver.get(url)
        self.driver.maximize_window()
