import os
from common.utilities.basepage import BasePage
from projects.example.constants import Constants
from projects.example.pages.locators.homepage import Homepage as locators


class HomePage(BasePage):

    def __init__(self):
        super().__init__()
        self._locators = locators
        self._constants = Constants

    def launch_url(self):
        url = os.getenv("url") if os.getenv("url") is not None else self._constants.url
        self.driver.get(url)
        try:
            self.microsoft_azure_handler()
        except:
            pass
        self.web_utils.wait_for_element_text(self._locators.parent, "Wikipedia", self.global_variables.medium_wait)

    def microsoft_azure_handler(self):
        email = os.getenv("email") if os.getenv("email") is not None else self._constants.email
        password = os.getenv("password") if os.getenv("password") is not None else self._constants.password
        self.web_utils.wait_until_element_visible(self._locators.email_text_box, 10)
        email_textbox_obj = self.web_utils.validate_and_get_webdriver_object_using_locator(
            self._locators.email_text_box, "Email textbox")
        submit_obj = self.web_utils.get_object(self._locators.submit_button, "Submit Button")
        email_textbox_obj.send_keys(email)
        self.web_utils.click.left(submit_obj)
        self.web_utils.wait_until_element_visible(self._locators.password_text_box, 10)
        password_textbox_obj = self.web_utils.validate_and_get_webdriver_object_using_locator(
            self._locators.password_text_box, "Password Text Box")
        password_textbox_obj.send_keys(password)
        submit_obj = self.web_utils.validate_and_get_webdriver_object_using_locator(self._locators.submit_button,
                                                                                    "Submit Button")
        self.web_utils.click.left(submit_obj)

    def enter_text_in_search_text_box(self, text_to_enter):
        search_input_box = self.web_utils.validate_and_get_webdriver_object_using_locator(
            self._locators.search_input_box, "Search Input Box")
        search_input_box.send_keys(text_to_enter)

    def click_on_the_search_button(self):
        search_button = self.web_utils.validate_and_get_webdriver_object_using_locator(self._locators.search_button,
                                                                                       "Search Button")
        self.web_utils.click.left(search_button)
