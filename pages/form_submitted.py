#Importing methods from selenium tools to lcoate stuff and to stroke keys
from pages.base_page import Base_page
from selenium.webdriver.common.by import By

#cREATING THE pAGE oBJECT cLASS
class Form_submitted_page(Base_page):

    MESSAGE_CORRECT = (By.ID, 'message')
    H_FORM_SUBMITTED = (By.CLASS_NAME, "display-6")
    #Initialization
    def __init__(self,browser):
        super().__init__(browser)