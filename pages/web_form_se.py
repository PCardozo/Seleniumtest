
import re
import os
import time
import calendar
from datetime import date

from select import select
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.action_chains import ActionChains



#cREATING THE pAGE oBJECT cLASS
class WebFormPage():
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
        self.dropdown_select = self.browser.find_element(By.CLASS_NAME,"form-select")
        self.file_input = self.browser.find_element(By.NAME,"my-file")
        self.default_checkbox = self.browser.find_element(By.ID,"my-check-2")
        self.default_radiobutton = self.browser.find_element(By.ID, "my-radio-1")
        self.checked_radiobutton = self.browser.find_element(By.ID, "my-radio-2")
        self.date_picker = self.browser.find_element(By.NAME, "my-date")
        self.color_picker = self.browser.find_element(By.NAME, "my-colors")
        self.title_header = self.browser.find_element(By.CLASS_NAME, 'display-6')
        self.range_picker = self.browser.find_element(By.CLASS_NAME, 'form-range')
        self.xpath_initial_switcher = "//div[contains(@class, 'datepicker')]//div[contains(@class, 'datepicker-days')]//th[contains(@class, 'datepicker-switch')]"
        self.xpath_days_prev_year_switcher = "//div[contains(@class, 'datepicker')]//div[contains(@class, 'datepicker-days')]//th[contains(@class, 'prev')]"
        self.xpath_days_next_year_switcher = "//div[contains(@class, 'datepicker')]//div[contains(@class, 'datepicker-days')]//th[contains(@class, 'next')]"
        self.xpath_months_prev_year_switcher = "//div[contains(@class, 'datepicker')]//div[contains(@class, 'datepicker-months')]//th[contains(@class, 'prev')]"
        self.xpath_months_next_year_switcher = "//div[contains(@class, 'datepicker')]//div[contains(@class, 'datepicker-months')]//th[contains(@class, 'next')]"
        self.xpath_switcher = "//th[@colspan='5' and @class='datepicker-switch' and not(contains(@style, 'display: none;')) and text()='{}']"
        self.day_element_xpath = "//td[text()='{}' and not(contains(@Class, 'old')) and not(contains(@Class, 'new'))]"
        self.month_element_xpath = "//td//span[contains(@Class, 'month') and (text()='{}')]"
        self.switcher_selector_prev_xpath = '/html/body/div/div[2]/table/thead/tr[2]/th[1]'
        self.switcher_selector_next_xpath = '/html/body/div/div[2]/table/thead/tr[2]/th[3]'

    def select_date(self,mmddyyyy_string):
        self.date_picker.click()
        #Treat the received date so I can actually use it
        array_target_date = mmddyyyy_string.split('/')
        target_day = array_target_date[1]
        target_month = array_target_date[0]
        target_date_year = array_target_date[2]

        #Switcher is selected so I can compare year
        date_picker_switch = self.browser.find_element(By.XPATH, self.xpath_initial_switcher)
        switcher_text_content = date_picker_switch.get_attribute('textContent')

        #If there is no match, I proceed to search
        if((target_date_year in switcher_text_content)):
            if(calendar.month_name[int(target_month)] in switcher_text_content):
                self.select_and_click_day_element(target_day)
                return

        #Year doesn't match, proceed to search year
        date_picker_switch.click()
        self.search_year_in_switcher(target_date_year, date.today().strftime("%m/%d/%Y").split('/')[2])
        self.select_month(target_month)
        self.select_and_click_day_element(target_day)

    def select_month(self,target_date_month):
        month_element = self.month_element_xpath.format(calendar.month_abbr[int(target_date_month)])
        self.browser.find_element(By.XPATH, month_element).click()

    def search_year_in_switcher(self,target_year,actual_year):
        diff = abs(int(actual_year) - int(target_year))
        switcher_button = None
        if(target_year>actual_year):
            switcher_button = self.browser.find_element(By.XPATH, self.xpath_months_next_year_switcher)
        else:
            switcher_button = self.browser.find_element(By.XPATH, self.xpath_months_prev_year_switcher)
        for i in range(diff):
            switcher_button.click()


    def select_and_click_day_element(self,day_number):
        day_number = str(int(day_number))
        local_day_element_xpath = self.day_element_xpath.format(day_number)
        day_element = self.browser.find_element(By.XPATH, local_day_element_xpath)
        day_element.click()

    def select_from_dropdown(self,dropdownElement,optionTextValue):
        select = Select(dropdownElement)
        select.select_by_visible_text(optionTextValue)

    def get_selected_option_value(self,dropdownElement,optionTextValue):
        select = Select(dropdownElement)
        return select.first_selected_option.text

    def click_and_send_keys_to_input(self,web_element,text_to_send):
        web_element.click()
        web_element.send_keys(text_to_send)

    def get_range_picker_value(self):
        return int(self.range_picker.get_attribute("valueAsNumber"))

    def get_range_picker_default_value(self):
        return int(self.range_picker.get_attribute("defaultValue"))

    def move_Range_picker(self,notches,direction):
        lateral = notches*20
        if (direction=="left"):
            lateral = lateral*-1
        action = ActionChains(self.browser)
        action.click_and_hold(self.range_picker)
        action.move_by_offset(lateral,0)
        action.release(on_element=None)
        action.perform()


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

    #Find and click submit button
    def submit_form(self):
        self.submit_button.click()

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