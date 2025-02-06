
#Importing methods from selenium tools to lcoate stuff and to stroke keys
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select

#cREATING THE pAGE oBJECT cLASS
class WebFormPage():
    #Si hay muchos elementos del mismo tipo, vale la pena crear un métod.o que seleccione uno de ellos basado
    # en una locator query que el tester le pase como argumento?
    # (Para el joker una locator query es una normaltor query?)

    #URL
    URL = 'https://www.selenium.dev/selenium/web/web-form.html'

    #Initialization
    def __init__(self,browser):
        self.browser = browser

    def load(self):
        self.browser.get(self.URL)

        #Locators
        self.text_input = self.browser.find_element(By.NAME, "my-text")
        self.password_input = self.browser.find_element(By.NAME, "my-password")
        self.submit_button = self.browser.find_element(By.CLASS_NAME, 'btn.btn-outline-primary.mt-3')
        self.textarea_input = self.browser.find_element(By.NAME, "my-textarea")
        self.disabled_input = self.browser.find_element(By.NAME, "my-disabled")
        self.readonly_text_field = self.browser.find_element(By.NAME, "my-readonly")
        self.dropdown_select = self.browser.find_element(By.NAME, "my-select")
        self.dropdown_select_option = self.browser.find_element(By.CSS_SELECTOR, "[value='1']")
        self.dropdown_datalist = self.browser.find_element(By.NAME, "my-datalist")
        self.dropdown_datalist_option = self.browser.find_element(By.CSS_SELECTOR, "[value='San Francisco']")

    def dropdown_datalist_current_value(self):
        return self.dropdown_select.get_attribute('value')

    def click_dropdown_datalist_option(self):
        self.dropdown_datalist_option.click()

    def click_dropdown_datalist(self):
        self.dropdown_datalist.click()

    def send_keys_dropdown_datalist(self,text_to_send):
        self.dropdown_datalist.send_keys(text_to_send)

    def dropdown_select_current_value(self):
        return self.dropdown_select.get_attribute('value')

    def click_dropdown_select_option(self):
        self.dropdown_select_option.click()

    def dropdown_select_option_value(self):
        return self.dropdown_select_option.get_attribute('value')

    def click_dropdown_select(self):
        self.dropdown_select.click()

    def click_text_input(self):
        self.text_input.click()

    def click_password_input(self):
        self.password_input.click()

    def password_input_value(self):
        value = self.password_input.get_attribute('value')
        return value

    def send_keys_to_password_input(self,text_to_send):
        self.password_input.send_keys(text_to_send)

    #Stroke keys into the input
    def send_keys_to_text_input(self,text_to_send):
        self.text_input.send_keys(text_to_send)

    #Find and click submit button
    def submit_form(self):
        self.submit_button.click()

    #Find and click Textarea
    def click_textarea_input(self):
        self.textarea_input.click()

    #Stroke keys into the Textarea
    def send_keys_to_textarea_input(self,text_to_send):
        self.textarea_input.send_keys(text_to_send)

    #Get disbaled property value from disabled input
    def disabled_input_value(self):
        return self.disabled_input.get_attribute('disabled')

    #Get readonly property value from readonly field
    def readonly_text_field_value(self):
        return self.readonly_text_field.get_attribute('readOnly')