"""
Created on Dec 20, 2022

@author: Rajesh Ravichandran
"""

import time
from selenium.webdriver import ActionChains
from common.utilities.assertions import Assertions
from common.utilities.javascript import JavaScript
from selenium.webdriver.remote.webelement import WebElement
from selenium.common.exceptions import NoSuchElementException
from common.utilities.global_variables import Global_variables


class WebElementUtils:

    @property
    def click(self):
        return Click()

    def __init__(self):
        self._assert = Assertions()
        self._javascript = JavaScript()
        self._driver = Global_variables.webdriver
        self._actions = ActionChains(self._driver)

    def verify_elements_text(self, elements_instance, expected_text, step_num, element_name, assert_type="equal",
                             value_len=None, slicing=(None, None), parent_instance=None):
        """
        Description: Verify the web elements text
        """
        actual_text_list = self.get_elements_text(elements_instance, parent_instance)
        self.list_values_verification(expected_text, actual_text_list, step_num, element_name, assert_type,
                                      value_len, slicing)

    def verify_number_of_visible_elements(self, elements_instance, expected_count, msg, parent_instance=None):
        """
        Description: Verify the visible number of elements
        """
        elements = self._get_objects(elements_instance, parent_instance)
        actual_count = sum([1 for element in elements if element.is_displayed()])
        self._assert.as_equal(expected_count, actual_count, msg)

    def get_elements_text(self, elements_instance, parent_instance=None):
        """
        :param elements_instance: Web Element whose text need to be fetched
        :param parent_instance: Parent instance web element if any
        :return: List of text of web element
        """
        elements_instance = self._get_objects(elements_instance, parent_instance)
        return [element.text.strip() for element in elements_instance if element.is_displayed()]

    def wait_for_element_text(self, locator, element_text, time_out, pause_time=0, case_sensitive=False,
                              raise_error=True, javascript=False, parent_obj=None):
        """
        Description: WebDriver will wait until given text visible on given locator
        """
        end_time = time.time() + time_out
        while True:
            if time.time() > end_time:
                if raise_error:
                    msg = "Time out for find [{}] text in [{}] element".format(element_text, locator)
                    raise TimeoutError(msg)
                else:
                    return False
            try:
                element = parent_obj.find_element(*locator) if parent_obj else self._driver.find_element(*locator)
                actual_text = self._javascript.get_element_text(element) if javascript else element.text
                if not case_sensitive:
                    actual_text = actual_text.lower().replace(" ", "").replace("\n", "")
                    element_text = element_text.lower().replace(" ", "")
                if element_text in actual_text:
                    time.sleep(pause_time)
                    return element
            except:
                pass
            time.sleep(2)

    def wait_until_element_visible(self, locator, time_out, pause_time=0, raise_error=True, parent_obj=None):
        """
        Description: WebDriver will wait until element visible
        """
        end_time = time.time() + time_out
        while True:
            if time.time() > end_time:
                if raise_error:
                    msg = "Time out for get visibility status of element".format(locator)
                    raise TimeoutError(msg)
                else:
                    return False
            try:
                element = parent_obj.find_element(*locator) if parent_obj else self._driver.find_element(*locator)
                if element.is_displayed():
                    time.sleep(pause_time)
                    return element
            except:
                pass
            time.sleep(0.5)

    def wait_until_element_invisible(self, locator, time_out, pause_time=0, raise_error=True, parent_obj=None):
        """
        Description: WebDriver will wait until element invisible
        """
        end_time = time.time() + time_out
        while True:
            if time.time() > end_time:
                if raise_error:
                    msg = "Time out for get visibility status of element".format(locator)
                    raise TimeoutError(msg)
                else:
                    return False
            try:
                elements = parent_obj.find_elements(*locator) if parent_obj else self._driver.find_elements(*locator)

                if elements == [] or not elements[0].is_displayed():
                    time.sleep(pause_time)
                    return True
            except:
                pass
            time.sleep(0.5)

    def _get_objects(self, element_instance, parent_instance=None):

        is_locator = isinstance(element_instance, tuple) and len(element_instance) == 2
        if is_locator:
            if parent_instance:
                return parent_instance.find_elements(*element_instance)
            return self._driver.find_elements(*element_instance)
        if isinstance(element_instance, list):
            return element_instance
        else:
            raise TypeError("Element instance should be WebElements list or Locator")

    def _get_object(self, element_instance, element_name):

        is_locator = isinstance(element_instance, tuple) and len(element_instance) == 2
        if is_locator:
            return self.validate_and_get_webdriver_object_using_locator(element_instance, element_name)
        elif isinstance(element_instance, WebElement):
            return element_instance
        else:
            raise TypeError("Element instance should be WebElement or Locator")

    def select_object_based_on_name(self, element_instance, element_name, parent_instance=None):
        """
        Description: This function will left click on the element option based on element name
        :Usage - select_object_based_on_name()
        """
        element_objects = self._get_objects(element_instance, parent_instance)
        vis_ele_objects = [actual_ele_obj for actual_ele_obj in element_objects if actual_ele_obj.is_displayed()]
        element_index = self._javascript.find_element_index_by_text(vis_ele_objects, element_name)
        if element_index is not None and element_index != '':
            self._driver.click(vis_ele_objects[element_index])
        else:
            msg = "[{0}] option is not available".format(element_name)
            raise ValueError(msg)

    def list_values_verification(self, expected_list, acutal_list, step_num, values_name, assert_type, value_len=None,
                                 slicing=(None, None)):
        """
        Description: Verify the given list values with difference types of assert type.
        :Parameters:
            expected_list:list = List which contains expected values to verify.
            actual_list:list = List which contains actual values to verify.
            step_num:str = Verification msg step number. Exmp: "03.01".
            values_name:str = Name of the values to compose verification message. Exmp: ContextMenu, X-Axisi Labels and etc.
            assert_type:str: Method of assert. Exmp: "eqaul" , "notin", "in"
            value_len:int: Length of the list values. List should contains only string values.
            slicing:tuple: Slicing index values to slice given list before verify
        """
        assert_types = ("equal", "in", "notin")
        if assert_type not in assert_types:
            raise TypeError("[{}] is invalid assert type. Valid types are {}".format(assert_type, assert_types))
        actual_list = acutal_list.copy()[slicing[0]:slicing[1]]
        if value_len:
            expected_list = [value[:value_len] for value in expected_list]
            actual_list = [value[:value_len] for value in actual_list]
        if assert_type == assert_types[0]:
            msg = "Step {0} : Verify {1}".format(step_num, values_name)
            self._assert.as_List_equal(expected_list, actual_list, msg)
        elif assert_type == assert_types[1]:
            missing_values = set(expected_list) - set(actual_list)
            msg = "Step {0} : Verify {1} in {2}".format(step_num, expected_list, values_name)
            if len(expected_list) == 0:
                self._assert.as_in(expected_list, actual_list, msg)
            elif missing_values:
                self._assert.as_in(list(missing_values), actual_list, msg)
            else:
                self._assert.as_equal(True, True, msg)
        elif assert_type == assert_types[2]:
            msg = "Step {0} : Verify {1} not in {2}".format(step_num, expected_list, values_name)
            not_missing_values = set(expected_list).intersection(actual_list)
            if not_missing_values:
                self._assert.as_in(list(not_missing_values), actual_list, msg)
            else:
                self._assert.as_equal(True, True, msg)
        else:
            raise NotImplemented

    def validate_and_get_webdriver_object(self, css_locator, webdriver_object_name, parent_object=None):
        """
        Description: This function is used to validate the webdriver object
        css_locator: css will be provided by User(#TableChart_1)
        webdriver_object_name: The meaningful and related name of the object will be provided by User.(Preview chart)
        """
        try:
            if parent_object is not None:
                return parent_object.find_element_by_css_selector(css_locator)
            else:
                return self._driver.find_element_by_css_selector(css_locator)
        except NoSuchElementException:
            display_msg = "{0} is currently not available in the page. The Provided CSS attribute ['{1}'] might not be correct.".format(
                webdriver_object_name, css_locator)
            raise AttributeError(display_msg)

    def validate_and_get_webdriver_objects(self, css_locator, webdriver_objects_reference_name, parent_object=None):
        """
        Description: This function is used to verify the list of webdriver elements in the page
        css_locator: css will be provided by User((#TableChart_1)
        webdriver_objects_reference_name : The meaningful and related name of the objects will be provided by User.(Preview chart)
        """
        if parent_object is not None:
            resp = parent_object.find_elements_by_css_selector(css_locator)
        else:
            resp = self._driver.find_elements_by_css_selector(css_locator)
        if len(resp) == 0:
            display_msg = "{0} is currently not available in the page. The Provided CSS attribute ['{1}'] might not be correct.".format(
                webdriver_objects_reference_name, css_locator)
            raise AttributeError(display_msg)
        else:
            return resp

    def validate_and_get_webdriver_object_using_locator(self, locator, webdriver_object_name, parent_object=None):
        """
        Description: This function is used to validate the webdriver object
        css_locator: css will be provided by User(#TableChart_1)
        webdriver_object_name: The meaningful and related name of the object will be provided by User
        """
        try:
            if parent_object is not None:
                return parent_object.find_element(*locator)
            else:
                return self._driver.find_element(*locator)
        except NoSuchElementException:
            display_msg = "{0} is currently not available in the page. The Provided CSS attribute ['{1}'] might not be correct.".format(
                webdriver_object_name, locator)
            raise AttributeError(display_msg)

    def validate_and_get_webdriver_objects_using_locator(self, locator, webdriver_objects_reference_name,
                                                         parent_object=None):
        """
        This function is used to verify the list of webdriver elements in the page
        css_locator: css will be provided by User((#TableChart_1)
        webdriver_objects_reference_name : The meaningful and related name of the objects will be provided by User.(Preview chart)
        """
        if parent_object is not None:
            resp = parent_object.find_elements(*locator)
        else:
            resp = self._driver.find_elements(*locator)
        if len(resp) == 0:
            display_msg = "{0} is currently not available in the page. The Provided CSS attribute ['{1}'] might not be correct.".format(
                webdriver_objects_reference_name, locator)
            raise AttributeError(display_msg)
        else:
            return resp

    def verify_element_is_visible(self, webelement, element_name, step_num):
        """
        :param webelement: Web Element which visibility check need to perform
        :param element_name: Element name to check the visibility
        :param step_num: Step Num for visibility check
        :return: None
        """
        status = webelement.is_displayed()
        msg = "Step {0}: Verify {1} is displayed".format(step_num, element_name)
        self._assert.as_equal(True, status, msg)


"""----------------------------------------------Click Methods------------------------------------------------------"""


class Click:

    def __init__(self):
        self._driver = Global_variables.webdriver
        self._actions = ActionChains(self._driver)

    def left(self, web_element, xoffset=0, yoffset=0, action_chain_click=False, pause_time=1):
        """
        Desc:- This function will click on any web_element on a specified location using option ActionChains and webelement click
        :param web_element: webelement where left click need to be performed
        :param xoffset: xoffset if needed
        :param yoffset: yoffset if needed
        :param action_chain_click: True if Action chains click
        :return: None
        """
        if action_chain_click:
            self._actions.move_to_element_with_offset(web_element, xoffset, yoffset).click().perform()
        else:
            web_element.click()
        time.sleep(pause_time)
