import unittest
import json
import os
from pages.HomePage import HomePage
from pages.SignUpPage import SignUpPage
from selenium import webdriver


class BaseTest(unittest.TestCase):
    def __init__(self):
        script_dir = os.path.dirname(__file__)
        print("The Script directory is " + script_dir)
        file_path = os.path.join(script_dir, 'resources/config.json')
        print("The Complete filepAth is " + file_path)

        with open(file_path) as data_file:
            configData = json.load(data_file)

        driver = webdriver.Firefox()
        homePage = HomePage(driver)
        signUpPage = SignUpPage(driver)

