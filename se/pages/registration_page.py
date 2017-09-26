from selenium.webdriver.common.by import By

from ..base import BasePage


class RegistrationPage(BasePage):

    first_name_input = (
        By.CSS_SELECTOR,
        '[name = "firstname"]'
    )
    last_name_input = (
        By.CSS_SELECTOR,
        '[name = "lastname"]'
    )
    email_input = (
        By.CSS_SELECTOR,
        '[name = "reg_email__"]'
    )
    re_enter_email_input = (
        By.CSS_SELECTOR,
        '[name = "reg_email_confirmation__"]'
    )
    password_input = (
        By.CSS_SELECTOR,
        '[name = "reg_passwd__"]'
    )
    month_select = (
        By.ID,
        'month'
    )
    year_select = (
        By.ID,
        'year'
    )
    gender_radio = (
        By.CSS_SELECTOR,
        'input[name = "sex"]'
    )
    submit_button = (
        By.CSS_SELECTOR,
        '[name = "websubmit"]'
    )


class CheckpointPage(BasePage):

    mail_code_input = (
        By.CSS_SELECTOR,
        '[name = "code"]'
    )
    download_image = (
        By.CLASS_NAME,
        'fileInputUpload'
    )
    continue_image = (
        By.CSS_SELECTOR,
        'button[name="submit[Continue]"]'
    )
    submit_ok = (
        By.CSS_SELECTOR,
        'button[name = "submit[OK]"]'
    )
