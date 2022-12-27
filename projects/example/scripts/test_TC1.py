"""-------------------------------------------------------------------------------------------
Author Name  : Rajesh Ravichandran
Automated On : 20-December-2022
-------------------------------------------------------------------------------------------"""
from common.utilities.basetestcase import BaseTestCase
from projects.example.pages.methods.wikipedia import Wikipedia


class Test_TC1(BaseTestCase):

    def test_TC1_evergreen(self):

        # Test case Objects
        Wiki = Wikipedia()

        """
            STEP 1 : Invoke example website
        """
        Wiki.Homepage.launch_url()
        Wiki.infra_utils.logging().info("STEP 1 : Invoke example website")

        """
            STEP 2 : Enter "Automation" in the search and click on the search button
        """
        Wiki.Homepage.enter_text_in_search_text_box("Automation")
        Wiki.Homepage.click_on_the_search_button()
        Wiki.infra_utils.logging().info("STEP 2 : Enter 'Automation' in the search and click on the search button")

        """
            STEP 3 : Verify Automation Page displayed
        """
        Wiki.AutomationPage.wait_for_automation_page_text("Automation")
        Wiki.AutomationPage.verify_automation_page_displayed("3")
        Wiki.infra_utils.take_screenshot("STEP 3 : Verify Automation Page displayed")
