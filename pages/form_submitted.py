#Importing methods from selenium tools to lcoate stuff and to stroke keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

#cREATING THE pAGE oBJECT cLASS
class Form_submitted_page():

    # LOCATORS - NO ME FUNCIONA EL TUPLE UNPACKING - MUST CALL THEM USING SELF.VAR_NAME
    MESSAGE_CORRECT = 'message'
    H_FORM_SUBMITTED = "display-6"
    #Initialization
    def __init__(self,browser):
        self.browser = browser

        self.h_form_submitted = self.browser.find_element(By.CLASS_NAME,"display-6")
        self.h_form_locator= "display-6"
        self.received_message_label = self.browser.find_element(By.ID, 'message')

    def get_received_message_text(self):
        return self.received_message_label.get_attribute('textContent')

    def get_h_form_text_value(self):
        return self.browser.find_element(By.CLASS_NAME,"display-6").get_attribute('textContent')

    def get_current_url(self):
        return self.browser.current_url