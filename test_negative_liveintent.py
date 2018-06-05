import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options


URL_LIVEINTENT = "https://platform.liveintent.com/login"
USERNAME = 'secret@secret.com'
PASS = 'secret'
ADV_NAME = 'test'

CONTAINS_TEXT = '//*[contains(text(), "{}")]'

TRACKER_NAME = 'helloworld'
TYPE = 'LiveConnect'
ATTR_VALUE = '14 Days'

EMAIL_XPATH = '//*[@id="email"]'
PASS_XPATH = '//*[@id="password"]'
SUBMIT_BTN_XPATH = '//*[@type="submit"]'

# main menu
CONVERSION_TRACKERS_BTN_XPATH = '//*[@routerlink="/campaign-manager/conversion-trackers"]'

# campaign manager
CREATE_NEW_CAMPAIGN_BTN_XPATH = '//*[@class="button--create"]'
NOTIFICATION_XPATH = '//*[@class="alert"]'

# creation
MODAL_XPATH = '//*[@class="lightbox ng-trigger ng-trigger-lightbox"]'

ADV_FIELD_XPATH = MODAL_XPATH + '//*[@name="advertiser"]//input'
ADV_DDL_XPATH = MODAL_XPATH + '//*[@name = "advertiser"]//*[@class = "dropdown"]/*'

TRACKER_NAME_XPATH = MODAL_XPATH + '//input[@name="name"]'

TYPE_BTN_XPATH = MODAL_XPATH + '//*[@name="type"]//*[@class="dropdown regular"]'
_TYPE_DDL = TYPE_BTN_XPATH + '/..//*[@class="dropdown--container ng-star-inserted"]'
TYPE_CHOICE_XPATH = _TYPE_DDL + CONTAINS_TEXT.format(TYPE)

ATTR_WINDOW_BTN_XPATH = MODAL_XPATH + '//*[@name="expiration"]//*[@class="dropdown regular"]'
_ATTR_WINDOW_DDL = ATTR_WINDOW_BTN_XPATH + '/parent::*//*[@class="dropdown--container ng-star-inserted"]'
ATTR_WINDOW_CHOICE_XPATH = _ATTR_WINDOW_DDL + CONTAINS_TEXT.format(ATTR_VALUE)

CREATE_TRACKER_BTN_XPATH = MODAL_XPATH + CONTAINS_TEXT.format('Create Tracker')

chrome_options = Options()


# chrome_options.add_argument("--start-maximized")


class TestConversionTrackers(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(options=chrome_options)

    def test_negative_conversion_tracker(self):
        driver = self.driver
        wait = WebDriverWait(driver, 10)
        """Navigate to: https://platform.liveintent.com/login"""
        driver.get(URL_LIVEINTENT)

        """Log in with credentials provided"""
        email_form = driver.find_element(By.XPATH, EMAIL_XPATH)
        email_form.clear()
        email_form.send_keys(USERNAME)

        pass_form = driver.find_element(By.XPATH, PASS_XPATH)
        pass_form.clear()
        pass_form.send_keys(PASS)

        submit_btn = driver.find_element(By.XPATH, SUBMIT_BTN_XPATH)
        submit_btn.click()

        # main
        """Selecting option 'Conversion Trackers' from Right Navigation"""
        campaign_trackers_btn = wait.until(EC.visibility_of_element_located((By.XPATH, CONVERSION_TRACKERS_BTN_XPATH)))
        campaign_trackers_btn.click()

        # campaign manager part
        create_new_campaign_btn = driver.find_element(By.XPATH, CREATE_NEW_CAMPAIGN_BTN_XPATH)
        create_new_campaign_btn.click()

        advertiser_name_field = wait.until(EC.visibility_of_element_located((By.XPATH, ADV_FIELD_XPATH)))
        advertiser_name_field.send_keys(ADV_NAME)
        advertiser_name_field.clear()
        advertiser_name_field.send_keys(ADV_NAME)

        advertiser_ddl = wait.until(EC.element_to_be_clickable((By.XPATH, ADV_DDL_XPATH)))
        advertiser_ddl.click()

        tracker_name_field = driver.find_element(By.XPATH, TRACKER_NAME_XPATH)
        tracker_name_field.clear()
        tracker_name_field.send_keys(TRACKER_NAME)

        type_dd = driver.find_element(By.XPATH, TYPE_BTN_XPATH)
        type_dd.click()
        selected_type = driver.find_element(By.XPATH, TYPE_CHOICE_XPATH)
        selected_type.click()

        attr_window_dd = driver.find_element(By.XPATH, ATTR_WINDOW_BTN_XPATH)
        attr_window_dd.click()
        selected_attr_window = driver.find_element(By.XPATH, ATTR_WINDOW_CHOICE_XPATH)
        selected_attr_window.click()

        create_tracker_btn = driver.find_element(By.XPATH, CREATE_TRACKER_BTN_XPATH)
        create_tracker_btn.click()

        alert = wait.until(EC.visibility_of_element_located((By.XPATH, NOTIFICATION_XPATH)))

        assert alert.is_displayed()
        assert TRACKER_NAME in alert.text

    def tearDown(self):
        self.driver.quit()


if __name__ == "__main__":
    unittest.main()
