import pytest
import allure
from allure_commons.types import AttachmentType
from common.utilities.global_variables import Global_variables


@pytest.mark.usefixtures("log_on_failure")
@pytest.mark.usefixtures("setup_teardown")
class BaseTestCase:

    @staticmethod
    @pytest.fixture()
    def log_on_failure(request) -> None:
        yield
        item = request.node
        if item.rep_call.failed:
            allure.attach(Global_variables.webdriver.get_screenshot_as_png(), name="Failed Step Screenshot",
                          attachment_type=AttachmentType.PNG)
