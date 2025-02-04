
#Importing methods from selenium tools to lcoate stuff and to stroke keys
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

#cREATING THE pAGE oBJECT cLASS
class WebFormPage():
    #Si hay muchos elementos del mismo tipo, vale la pena crear un métod.o que seleccione uno de ellos basado
    # en una locator query que el tester le pase como argumento?
    # (Para el joker una locator query es una normaltor query?)

    #URL
    URL = 'https://www.selenium.dev/selenium/web/web-form.html'

    #LOCATORS - NO ME FUNCIONA EL TUPLE UNPACKING - MUST CALL THEM USING SELF.VAR_NAME
    TEXT_INPUT_NAME = "my-text"
    SUBMIT_BUTTON = 'btn.btn-outline-primary.mt-3'
    PASSWORD_INPUT_NAME = "my-password"
    TEXTAREA_INPUT_NAME = "my-textarea"
    DISABLED_INPUT_NAME= "my-disabled"
    READONLY_TEXT_FIELD_NAME = "my-readonly"
    #Initialization
    def __init__(self,browser):
        self.browser = browser

    # Interaction Methods
    # Load page son we can puppeteer it
    def load(self):
        self.browser.get(self.URL)

    #Find the text input and click it
    def click_text_input(self):
        text_input = self.browser.find_element(By.NAME,self.TEXT_INPUT_NAME)
        text_input.click()

    def click_password_input(self):
        password_input = self.browser.find_element(By.NAME,self.PASSWORD_INPUT_NAME)
        password_input.click()

    def password_input_value(self):
        value = self.browser.find_element(By.NAME,self.PASSWORD_INPUT_NAME).get_attribute('value')
        return value

    def send_keys_to_password_input(self,text_to_send):
        password_input = self.browser.find_element(By.NAME,self.PASSWORD_INPUT_NAME)
        password_input.send_keys(text_to_send)

    #Stroke keys into the input
    def send_keys_to_text_input(self,text_to_send):
        text_input = self.browser.find_element(By.NAME,self.TEXT_INPUT_NAME)
        text_input.send_keys(text_to_send)

    #Find and click submit button
    def submit_form(self):
        submit_button = self.browser.find_element(By.CLASS_NAME,self.SUBMIT_BUTTON)
        submit_button.click()

    #Find and click Textarea
    def click_textarea_input(self):
        textarea_input = self.browser.find_element(By.NAME,self.TEXTAREA_INPUT_NAME)
        textarea_input.click()

    #Stroke keys into the Textarea
    def send_keys_to_textarea_input(self,text_to_send):
        textarea_input = self.browser.find_element(By.NAME,self.TEXTAREA_INPUT_NAME)
        textarea_input.send_keys(text_to_send)

    #Get disbaled property value from disabled input
    def disabled_input_value(self):
        value = self.browser.find_element(By.NAME,self.DISABLED_INPUT_NAME).get_attribute('disabled')
        return value

    #Get readonly property value from readonly field
    def readonly_text_field_value(self):
        value = self.browser.find_element(By.NAME,self.READONLY_TEXT_FIELD_NAME).get_attribute('readOnly')
        return value