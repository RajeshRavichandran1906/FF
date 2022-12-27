import allure
import psutil
import logging
from allure_commons.types import AttachmentType
from common.utilities.global_variables import Global_variables


class InfrastructureUtils:

    def __init__(self):

        self._driver = Global_variables.webdriver

    @staticmethod
    def kill_browser_process():
        """
        Description: This function will kill browser, browser driver and python shell process.
        """
        for proc in psutil.process_iter():
            try:
                # Get process name from process object.
                processName = proc.name()
                if processName in ['chromedriver.exe', 'geckodriver.exe', 'IEDriverServer.exe',
                                   'MicrosoftWebDriver.exe', 'chrome.exe', 'firefox.exe', 'MicrosoftEdge.exe',
                                   'iexplore.exe']:
                    proc.kill()
            except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
                pass

    @staticmethod
    def logging():
        """
        Description: This method is used for logging steps
        """
        logger_name = Global_variables.test_case_name
        logger = logging.getLogger(logger_name)
        if logger.hasHandlers():
            logger.handlers.clear()
        file_handler = logging.FileHandler("../../../logs/{0}.log".format(logger_name))
        formatter = logging.Formatter("%(asctime)s :%(levelname)s : %(message)s")
        file_handler.setFormatter(formatter)
        logger.addHandler(file_handler)
        logger.setLevel(logging.INFO)
        return logger

    @staticmethod
    def take_screenshot(screenshot_name):
        allure.attach(Global_variables.webdriver.get_screenshot_as_png(), name=screenshot_name,
                      attachment_type=AttachmentType.PNG)
