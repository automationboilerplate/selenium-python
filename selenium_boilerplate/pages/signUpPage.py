from pages.basePage import BasePage as ParentPage
from page_objects import PageElement


class SignUpPage(ParentPage):
    firstName = PageElement(class_name='userdata-firstname')


