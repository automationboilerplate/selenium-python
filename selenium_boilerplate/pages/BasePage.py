from page_objects import PageObject


class BasePage(PageObject):

    def __init__(self, driver, baseUrl):
        self.driver = driver
        self.baseUrl = baseUrl




