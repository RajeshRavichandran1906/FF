"""
Created on Dec 16, 2022

@author: Rajesh Ravichandran
"""

from selenium import webdriver


class DriverLauncher(object):

    def execute(self):
        options = webdriver.ChromeOptions()
        options.add_experimental_option('excludeSwitches', ['enable-logging'])
        return webdriver.Chrome(options=options)
