import json
import os
from selenium import webdriver


class BaseTest(object):
    def setUp(self):
        script_dir = os.path.dirname(__file__)
        file_path = os.path.join(script_dir, 'resources/config.json')

        with open(file_path) as data_file:
            configData = json.loads(data_file.read())

        browser = webdriver.Chrome(os.path.join(script_dir,  "resources/libs/chromedriver_2.40"))
        print("The Url is " + configData["environments"]["dev"]["host"])
        browser.get(configData["environments"]["dev"]["host"])
