from pages.BasePage import BasePage as ParentPage
from page_objects import PageElement


class HomePage(ParentPage):
    firstName = PageElement(id_='signup-button')

