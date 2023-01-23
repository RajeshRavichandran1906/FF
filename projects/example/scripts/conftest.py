import os
import pytest
from projects.example.constants import Constants
from common.utilities.infra_utils import InfrastructureUtils
from common.utilities.global_variables import Global_variables
from common.webdriverfactory.WebDriverFactory import WebDriverFactory


@pytest.fixture(scope="function")
def setup_teardown():
    browser = os.getenv("browser") if os.getenv("browser") is not None else Constants.browser
    Global_variables.test_case_name = os.environ.get('PYTEST_CURRENT_TEST').split(':')[-1].split(' ')[0]
    driver = WebDriverFactory.getInstance(browser)
    driver.maximize_window()
    Global_variables.webdriver = driver
    InfrastructureUtils().logging().info(browser + " browser instance creation successful")
    yield
    if Global_variables.assert_failure_count > 0:
        InfrastructureUtils().logging().error(Global_variables.assertion_failure_list)
        raise_msg = "Assertion check point failed \n"
        Global_variables.asert_failure_count = 0
        raise AssertionError(raise_msg)
    driver.quit()


@pytest.hookimpl(hookwrapper=True, tryfirst=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()
    setattr(item, "rep_" + rep.when, rep)
    return rep
