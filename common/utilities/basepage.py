from common.utilities.javascript import JavaScript
from common.utilities.assertions import Assertions
from common.utilities.web_utilites import WebElementUtils
from common.utilities.infra_utils import InfrastructureUtils
from common.utilities.global_variables import Global_variables


class BasePage:

    def __init__(self):
        self.assertion = Assertions()
        self.javascript = JavaScript()
        self.web_utils = WebElementUtils()
        self.infra_utils = InfrastructureUtils()
        self.driver = Global_variables.webdriver
        self.global_variables = Global_variables

