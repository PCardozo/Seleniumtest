
#Importing methods from selenium tools to lcoate stuff and to stroke keys
import os
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

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
        self.file_input = self.browser.find_element(By.NAME,"my-file")
        self.default_checkbox = self.browser.find_element(By.ID,"my-check-2")
        self.default_radiobutton = self.browser.find_element(By.ID, "my-radio-1")
        self.checked_radiobutton = self.browser.find_element(By.ID, "my-radio-2")
        self.date_picker = self.browser.find_element(By.NAME, "my-date")
        self.color_picker = self.browser.find_element(By.NAME, "my-colors")
        self.title_header = self.browser.find_element(By.CLASS_NAME, 'display-6')

    def  date_picker_switch_deploy_and_click(self): #this function clicks the switchers to get the list of years
        self.switches_array = self.browser.find_elements(By.CLASS_NAME, "datepicker-switch")
        self.switches_array[0].click()
        self.switches_array[1].click()

    def date_picker_switch_click_years(self,target_year):
        self.year_elements = self.browser.find_elements(By.CLASS_NAME, "year")
        if (len(self.year_elements)<1):
            raise Exception("Jajaj no encontré ná") #Failsafe
        for e in self.year_elements:
            if(e.get_attribute('textContent')==target_year):
                e.click()
                break

    def date_picker_switch_find_and_click_month(self,month_init):
        self.month_elements = self.browser.find_elements(By.CLASS_NAME, "month")
        if (len(self.month_elements) < 1):
            raise Exception("Jajaj no encontré ná")  # Failsafe
        for e in self.month_elements:
            if (e.get_attribute('textContent') == month_init):
                e.click()
                break



    def date_picker_value(self):
        return self.date_picker.get_attribute("value")

    def send_keys_to_date_picker(self,text_to_send):
        self.date_picker.send_keys(text_to_send)

    def click_date_day_element(self,day):
        day_elements = self.browser.find_elements(By.CSS_SELECTOR, ".day:not(.old)")
        day_text = day
        if (day_text[0] == "0"):
            day_text = day_text[1]
        if (len(day_elements)<1):
            raise Exception("Jajaj no encontré ná") #Failsafe
        for e in day_elements:
            if(e.get_attribute("textContent")==day_text):
                e.click()
                break

    def click_date_picker(self):
        self.date_picker.click()

    def default_radiobutton_value(self):
        return self.default_radiobutton.get_attribute("checked")

    def checked_radiobutton_value(self):
        return self.checked_radiobutton.get_attribute("checked")

    def click_default_radiobutton(self):
        self.default_radiobutton.click()

    def click_default_checkbox(self):
        self.default_checkbox.click()

    def default_checkbox_value(self):
        return self.default_checkbox.get_attribute("checked")

    def send_keys_to_file_input(self,text_to_send):
        self.file_input.send_keys(text_to_send)

    def file_input_value(self):
        value = self.file_input.get_attribute('value')
        return value

    def click_file_input(self):
        self.file_input.click()

    def select_file_to_upload(self,local_file_path):
        keyboard = Controller()
        keyboard.type(local_file_path)
        keyboard.press(Key.enter)
        keyboard.release(Key.enter)

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

    def click_color_picker(self):
        self.color_picker.click()

    def click_title_header(self):
        self.tilte_header.click()