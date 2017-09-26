# -*- coding: utf-8 -*

from faker import Faker
from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

from ..state import get_mail, get_sms_code

from ..pages.registration_page import CheckpointPage, RegistrationPage

from ..constans import PATH


class TestFaceBook:

    def test_facebook_registration(self):

        self.driver = webdriver.Chrome()
        driver = self.driver
        f = Faker('en_US')
        page = RegistrationPage(self.driver)
        page.open('https://www.facebook.com')
        page.find_element(*page.first_name_input).send_keys(f.first_name())
        page.find_element(*page.last_name_input).send_keys(f.last_name())

        tm_email = get_mail()
        page.find_element(*page.email_input).send_keys(tm_email)
        page.find_element(*page.re_enter_email_input).send_keys(tm_email)

        password = page.find_element(*page.password_input)
        pass_text = f.password()
        password.send_keys(pass_text)

        Select(page.find_element(*page.month_select)).select_by_value('1')
        Select(page.find_element(*page.year_select)).select_by_value('1992')
        page.find_elements(*page.gender_radio)[1].click()
        page.find_element(*page.submit_button).click()

        page = CheckpointPage(self.driver)
        code = get_sms_code(tm_email)
        wait = WebDriverWait(driver, 10)
        wait.until(
            ec.presence_of_element_located(page.download_image),
            message='mail_code_input is not found'
        )
        page.find_element(*page.mail_code_input).send_keys(code)
        wait.until(
            ec.visibility_of_element_located(page.download_image),
            message='download_image is not found'
        )
        page.find_element(*page.download_image).send_keys(PATH)
        driver.implicitly_wait(5)
        page.find_element(*page.continue_image).click()
        WebDriverWait(driver, 10).until(
            ec.visibility_of_element_located(page.submit_ok)
        )
        page.find_element(*page.submit_ok).click()
        driver.quit()
