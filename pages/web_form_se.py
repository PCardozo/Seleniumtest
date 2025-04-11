import calendar
from datetime import date
from pages.base_page import Base_page
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.action_chains import ActionChains



#cREATING THE pAGE oBJECT cLASS
class WebFormPage(Base_page):
    #URL
    URL = 'https://www.selenium.dev/selenium/web/web-form.html'

    #LOCATORS
    TEXT_INPUT = (By.NAME, "my-text")
    SUBMIT_BUTTON = (By.CLASS_NAME, 'btn.btn-outline-primary.mt-3')
    PASSWORD_FIELD = (By.NAME, "my-password")
    TEXTAREA = (By.NAME, "my-textarea")
    DISABLED_INPUT = (By.NAME, "my-disabled")
    READONLY = (By.NAME, "my-readonly")
    DROPDOWN_SELECT = (By.CLASS_NAME,"form-select")
    FILE_INPUT = (By.NAME,"my-file")
    DEFAULT_CHK = (By.ID,"my-check-2")
    DEFAULT_RADIO = (By.ID, "my-radio-1")
    CHECKED_RADIO = (By.ID, "my-radio-2")
    DATE_PICKER = (By.NAME, "my-date")
    DP_INITIAL_SWITCH = (By.XPATH,"//div[contains(@class, 'datepicker')]//div[contains(@class, 'datepicker-days')]//th[contains(@class, 'datepicker-switch')]")
    DAY_ELEMENT_BP = "//td[text()='{}' and not(contains(@Class, 'old')) and not(contains(@Class, 'new'))]"
    MONTH_ELEMENT_BP = "//td//span[contains(@Class, 'month') and (text()='{}')]"
    YEAR_SWITCHER_PREV = (By.XPATH, "//div[contains(@class, 'datepicker')]//div[contains(@class, 'datepicker-months')]//th[contains(@class, 'prev')]")
    YEAR_SWITCHER_NEXT = (By.XPATH, "//div[contains(@class, 'datepicker')]//div[contains(@class, 'datepicker-months')]//th[contains(@class, 'next')]")
    RANGE_PICKER = (By.CLASS_NAME, 'form-range')
    #Initialization
    def __init__(self,browser):
        super().__init__(browser)

    def load(self):
        self.browser.get(self.URL)
        #Locators
        self.color_picker = self.browser.find_element(By.NAME, "my-colors")
        self.title_header = self.browser.find_element(By.CLASS_NAME, 'display-6')

    def select_from_dropdown(self,locator_tuple,optionTextValue):
        element = self.browser.find_element(*locator_tuple)
        select = Select(element)
        select.select_by_visible_text(optionTextValue)

    def get_selected_option_value(self,locator_tuple):
        element = self.browser.find_element(*locator_tuple)
        select = Select(element)
        return select.first_selected_option.text

    def select_date(self,mmddyyyy_string):
        date_picker = self.browser.find_element(*self.DATE_PICKER)
        date_picker.click()
        #Treat the received date so I can actually use it
        array_target_date = mmddyyyy_string.split('/')
        target_day = array_target_date[1]
        target_month = array_target_date[0]
        target_date_year = array_target_date[2]

        #Switcher is selected so I can compare year
        date_picker_switch = self.browser.find_element(*self.DP_INITIAL_SWITCH)
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

    def select_and_click_day_element(self,day_number):
        day_number = str(int(day_number))
        constructed_xpath = self.DAY_ELEMENT_BP.format(day_number)
        day_element = self.browser.find_element(By.XPATH, constructed_xpath)
        day_element.click()

    def select_month(self,target_month):
        constructed_xpath = self.MONTH_ELEMENT_BP.format(calendar.month_abbr[int(target_month)])
        self.browser.find_element(By.XPATH, constructed_xpath).click()

    def search_year_in_switcher(self,target_year,actual_year):
        diff = abs(int(actual_year) - int(target_year))
        switcher_button = None
        if(target_year>actual_year):
            switcher_button = self.browser.find_element(*self.YEAR_SWITCHER_NEXT)
        else:
            switcher_button = self.browser.find_element(*self.YEAR_SWITCHER_PREV)
        for i in range(diff):
            switcher_button.click()

    def get_range_picker_value(self):
        return int(self.range_picker.get_attribute("valueAsNumber"))

    def get_range_picker_default_value(self):
        return int(self.range_picker.get_attribute("defaultValue"))

    def move_Range_picker(self,notches,direction):
        range_picker = self.browser.find_element(*self.RANGE_PICKER)
        lateral = notches*20
        if (direction=="left"):
            lateral = lateral*-1
        action = ActionChains(self.browser)
        action.click_and_hold(range_picker)
        action.move_by_offset(lateral,0)
        action.release(on_element=None)
        action.perform()