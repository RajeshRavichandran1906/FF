import re
import unittest
from common.utilities.infra_utils import InfrastructureUtils
from common.utilities.global_variables import Global_variables


class Assertions:

    def __init__(self):

        self._driver = Global_variables.webdriver
        self._unittest = unittest.TestCase()
        self._infra_utils = InfrastructureUtils()

    def as_List_equal(self, *params) -> None:
        try:
            self._unittest.assertListEqual(params[0], params[1], params[2])
            self._infra_utils.logging().info(params[2] + " - PASSED.")
            Global_variables.verification_steps.append(params[2] + " - PASSED.")
        except AssertionError as e:
            m = re.match(r'.*(Step.*)...', str(e.args))
            msg = m.group(1) + " - FAILED." + 'List Equal comparison : value1=[' + str(params[0]) + '], value2=[' + str(
                params[1]) + ']'
            self._infra_utils.logging().error(msg)
            Global_variables.assertion_failure_list.append(msg)
            Global_variables.assert_failure_count += 1

    def as_equal(self, *params) -> None:
        try:
            self._unittest.assertEqual(params[0], params[1], params[2])
            self._infra_utils.logging().info(params[2] + " - PASSED.")
            Global_variables.verification_steps.append(params[2] + " - PASSED.")
        except AssertionError as e:
            m = re.match(r'.*([S|s]tep.*)...', str(e.args))
            msg = m.group(1) + " - FAILED." + 'Equal comparison : value1=[' + str(params[0]) + '], value2=[' + str(
                params[1]) + ']'
            self._infra_utils.logging().error(msg)
            Global_variables.assertion_failure_list.append(msg)
            Global_variables.assert_failure_count += 1

    def as_not_equal(self, *params) -> None:
        try:
            self._unittest.assertNotEqual(params[0], params[1], params[2])
            self._infra_utils.logging().info(params[2] + " - PASSED.")
            Global_variables.verification_steps.append(params[2] + " - PASSED.")
        except AssertionError as e:
            m = re.match(r'.*(Step.*)...', str(e.args))
            msg = m.group(1) + " - FAILED." + 'Not Equal comparison : value1=[' + str(params[0]) + '], value2=[' + str(
                params[1]) + ']'
            self._infra_utils.logging().info(msg)
            Global_variables.assertion_failure_list.append(msg)
            Global_variables.assert_failure_count += 1

    def as_in(self, *params) -> None:
        try:
            assert params[0] in params[1], params[2]
            self._infra_utils.logging().info(params[2] + " - PASSED.")
            Global_variables.verification_steps.append(params[2] + " - PASSED.")
        except AssertionError as e:
            m = re.match(r'.*(Step.*)...', str(e.args))
            msg = m.group(1) + " - FAILED." + 'ASIN comparison : value1=[' + str(params[0]) + '], value2=[' + str(
                params[1]) + ']'
            self._infra_utils.logging().info(msg)
            Global_variables.assertion_failure_list.append(msg)
            Global_variables.assert_failure_count += 1

    def as_not_in(self, *params) -> None:
        try:
            assert params[0] not in params[1], params[2]
            self._infra_utils.logging().info(params[2] + " - PASSED.")
            Global_variables.verification_steps.append(params[2] + " - PASSED.")
        except AssertionError as e:
            m = re.match(r'.*(Step.*)...', str(e.args))
            msg = m.group(1) + " - FAILED." + 'Equal comparison : value1=[' + str(params[0]) + '], value2=[' + str(
                params[1]) + ']'
            self._infra_utils.logging().error(msg)
            Global_variables.assertion_failure_list.append(msg)
            Global_variables.assert_failure_count += 1

    def as_GE(self, *params) -> None:
        try:
            self._unittest.assertGreaterEqual(params[0], params[1], params[2])
            self._infra_utils.logging().info(params[2] + " - PASSED.")
            Global_variables.verification_steps.append(params[2] + " - PASSED.")
        except AssertionError as e:
            m = re.match(r'.*(Step.*)...', str(e.args))
            msg = m.group(1) + " - FAILED." + 'As GEqual to comparison : value1=[' + str(
                params[0]) + '], value2=[' + str(
                params[1]) + ']'
            self._infra_utils.logging().error(msg)
            Global_variables.assertion_failure_list.append(msg)
            Global_variables.assert_failure_count += 1

    def as_LE(self, *params) -> None:
        try:
            self._unittest.assertLessEqual(params[0], params[1], params[2])
            self._infra_utils.logging().info(params[2] + " - PASSED.")
            Global_variables.verification_steps.append(params[2] + " - PASSED.")
        except AssertionError as e:
            m = re.match(r'.*(Step.*)...', str(e.args))
            msg = m.group(1) + " - FAILED." + 'As LEqual to comparison : value1=[' + str(
                params[0]) + '], value2=[' + str(
                params[1]) + ']'
            self._infra_utils.logging().error(msg)
            Global_variables.assertion_failure_list.append(msg)
            Global_variables.assert_failure_count += 1
