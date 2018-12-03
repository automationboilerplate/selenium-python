from pages.BasePage import BasePage as ParentPage
from page_objects import PageElement


class SignUpPage(ParentPage):
    firstName = PageElement(class_name='userdata-firstname')


