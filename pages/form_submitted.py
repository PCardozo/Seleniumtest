#Importing methods from selenium tools to lcoate stuff and to stroke keys
from selenium.webdriver.common.by import By

#cREATING THE pAGE oBJECT cLASS
class Form_submitted_page():

    # LOCATORS - NO ME FUNCIONA EL TUPLE UNPACKING - MUST CALL THEM USING SELF.VAR_NAME
    MESSAGE_CORRECT = 'message'
    H_FORM_SUBMITTED = "display-6"
    #Initialization
    def __init__(self,browser):
        self.browser = browser

    #Interaction Methods
    def message_correct_text(self):
        message = self.browser.find_element(By.ID,self.MESSAGE_CORRECT)
        message_text = message.get_attribute('textContent')
        return message_text

    def h_form_submitted_text(self):
        h1 = self.browser.find_element(By.CLASS_NAME,self.H_FORM_SUBMITTED)
        h_text = h1.get_attribute('textContent')
        return h_text