from common.utilities.basepage import BasePage
from projects.example.pages.methods.homepage import HomePage
from projects.example.pages.methods.automation_page import AutomationPage


class Wikipedia(BasePage):

    def __init__(self):
        super().__init__()

    @property
    def Homepage(self): return HomePage()

    @property
    def AutomationPage(self): return AutomationPage()
