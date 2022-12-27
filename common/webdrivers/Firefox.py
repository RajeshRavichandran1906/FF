"""
Created on Dec 20, 2022

@author: Rajesh Ravichandran
"""

from selenium import webdriver


class DriverLauncher(object):
        
    def execute(self):
        return webdriver.Firefox()