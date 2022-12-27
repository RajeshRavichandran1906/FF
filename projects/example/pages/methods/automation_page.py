from common.utilities.basepage import BasePage
from projects.example.pages.locators.automation_page import AutomationPage as locators


class AutomationPage(BasePage):

    def __init__(self):
        super().__init__()
        self._locators = locators

    def wait_for_automation_page_text(self, text):
        self.web_utils.wait_for_element_text(self._locators.parent, text, self.global_variables.medium_wait)

    def verify_automation_page_displayed(self, step):
        self.web_utils.verify_element_is_visible(self.web_utils.get_object(self._locators.texts, "Automation Page"), "Automation Page", step)
        self.assertion.as_equal(1, 1, "Step 3.2:")
        self.assertion.as_equal(1, 5, "Step 3.3:")
        self.assertion.as_equal(1, 4, "Step 3.4:")