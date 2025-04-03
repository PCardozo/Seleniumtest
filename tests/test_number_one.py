
  # The browser argument passed to the function comes from the conftest.py file. That file contains a fixture
  # that is used for setup and cleanup of every individual test, so, whenever a test is executed
  # first is executed whatever comes before the yield statement contained in the fixture (setup)
  # and after the test is finished, whatever comes AFTER the yield statement gets executed (cleanup).
  # The conftest.py file must be located at the tests file. I think it's pytest what loads whatever is in there
  # to bring the arguments here, im not quite sure.

import os
import time
from email.policy import default
from datetime import date
from pages.web_form_se import WebFormPage
from pages.form_submitted import Form_submitted_page
from tests.conftest import browser
from dateutil.relativedelta import relativedelta
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

correct_text = 'Received!'
h1_success_text = 'Form submitted'
test_keys = 'charvarious'
test_password = 'Jhostynxon_Garcia'
dropDown_option_Text = "One"
file_name = "testFileName.png"
#Dates are tested in mmddyyyy format!!
my_date = date.today().strftime("%m/%d/%Y")
past_date = (date.today() - relativedelta(years=2, months=2, days=2)).strftime("%m/%d/%Y")
future_date = (date.today() + relativedelta(years=1, months=1, days=1)).strftime("%m/%d/%Y")
#future_date = (date.today() + relativedelta(years=3)).strftime("%m/%d/%Y")
range_picker_notches = 2

#This goes on the base page object
def get_element_textcontent(webelement):
  return webelement.get_attribute('textContent')


# Scenario 1: Validate text input
def test_prueba_uno(landing_page):
  # Given the User is in the web form page
  # When the user enters a valid text into the text input
  landing_page.click_and_send_keys_to_input(landing_page.text_input,test_keys)
  landing_page.submit_button.click()
  web_form_after_submit = Form_submitted_page(landing_page.browser)
  # Then the field accepts the value
  #assert get_element_textcontent(web_form_after_submit.h_form_submitted) == h1_success_text
  # And no error messages are shown
  assert web_form_after_submit.received_message_label.get_attribute('textContent') == correct_text
  assert web_form_after_submit.h_form_submitted.get_attribute('textContent') == h1_success_text
  assert test_keys in web_form_after_submit.get_current_url()

# Scenario 2: Validate password input
def test_password_field(landing_page):
  # Given the user is at the Form page.
  # When the user inputs a valid password in the password field
  landing_page.click_and_send_keys_to_input(landing_page.password_input,test_password)
  assert landing_page.password_input.get_attribute('value') == test_password
  # Then the field accepts the password and no error messages are shown.
  landing_page.submit_button.click()
  web_form_after_submit = Form_submitted_page(landing_page.browser)
  curr_url = web_form_after_submit.browser.current_url
  assert web_form_after_submit.received_message_label.get_attribute('textContent') == correct_text
  assert web_form_after_submit.h_form_submitted.get_attribute('textContent') == h1_success_text
  assert test_password in curr_url

# Scenario 3: Validate textarea input
def test_textarea(landing_page):
  # Given the user is at the Form page.
  # When the user inputs text into the textarea
  landing_page.click_and_send_keys_to_input(landing_page.textarea_input,test_keys)
  assert landing_page.textarea_input.get_attribute('value') == test_keys
  # Then the textarea receives the text and displays it correctamente.
  landing_page.submit_button.click()
  web_form_after_submit = Form_submitted_page(landing_page.browser)
  curr_url = web_form_after_submit.browser.current_url
  assert web_form_after_submit.received_message_label.get_attribute('textContent') == correct_text
  assert web_form_after_submit.h_form_submitted.get_attribute('textContent') == h1_success_text
  assert test_keys in curr_url

# Scenario 4: Validate disabled input
def test_disabled_input(landing_page):
  # Given the user is at the Form page.
  # When the user tries to interact with the disabled input.
  # Then the field has the property "disabled".
  assert landing_page.disabled_input.get_attribute('disabled')

# Scenario 5: Validate readonly input
def test_readonly_input(landing_page):
  # Given the user is at the Form page.
  # When the user tries to edit the Readonly field.
  # Then the field has the Readonly property.
  assert landing_page.readonly_text_field.get_attribute('readOnly')

# Scenario 6: Validate dropdown
def test_dropdown_select(landing_page):
  # Given the user is at the Form page.
  # When the user selects an option from the dropdown
  landing_page.select_from_dropdown(landing_page.dropdown_select,dropDown_option_Text)
  # Then the selected option is displayed on the field.
  assert landing_page.get_selected_option_value(landing_page.dropdown_select,dropDown_option_Text) == dropDown_option_Text

# Scenario 7: Validate dropdown datalist - Uses native elements ,cannot be tested
#def test_dropdown_datalist(browser):
  #raise Exception("Incomplete Test")

# Scenario 8: Validate File input
def test_file_input(landing_page):
  file = os.path.join(os.getcwd(), file_name)
  # Given the user is at the Form page.
  # When the user loads a file through the file input.
  landing_page.file_input.send_keys(file)
  # Then the file's name is displayed on the input field.
  assert file_name in landing_page.file_input.get_attribute('value')

# Scenario 9: Validate Checkboxes
def test_checkboxes(landing_page):
  # Given the User is at the Form page.
  # When the User selects the "default checkbox"
  landing_page.default_checkbox.click()
  # Then the checkbox's state changes to "checked".
  assert landing_page.default_checkbox.get_attribute("checked")

# Scenario 10: Validate Radiobuttons
def test_radiobuttons(landing_page):
  # Given the User is at the Form page.
  # When the User selects the "default radiobutton"
  landing_page.default_radiobutton.click()
  # Then the default radiobutton's state changes to "checked".
  assert landing_page.default_radiobutton.get_attribute("checked")
  #And any other radiobuttons change to "unchecked".
  assert landing_page.checked_radiobutton.get_attribute("checked") == None

# Scenario 11: Validate Colorpicker - Uses native OS interface - Cannot be tested.
#def test_color_picker(browser):
  #raise Exception("Incomplete Test")

# Scenario 12: Validate Date Picker
def test_date_picker_format(landing_page):
  # Given the User is at the Form page.
  # When the user selects a valid date in the Date Picker.
  landing_page.select_date(my_date)
  # Then the selected Date is displayed on the field.
  assert landing_page.date_picker.get_attribute("value") == my_date

def test_past_date(landing_page):
  # Given the User is at the Form page.
  # When the User selects a date equal to today's date, but 2 years, 2 months and 2 days in the past
  landing_page.select_date(past_date)
  # Then the selected date should be reflected on the corresponding field
  assert landing_page.date_picker.get_attribute('value')== past_date

def test_manual_date_picker_date(landing_page):
  # Given the User is at the Form page.
  # When the User manually enters a valid Date on the Date picker
  landing_page.click_and_send_keys_to_input(landing_page.date_picker,my_date)
  # Then the selected Date is diplayed on the field.
  assert landing_page.date_picker.get_attribute('value') == my_date

def test_future_date(landing_page):
  # Given the User is at the Form page.
  # When the user selects a date in the the future
  landing_page.select_date(future_date)
  # Then the selected date must be correctly displayed in its corresponding field.
  assert landing_page.date_picker.get_attribute('value') == future_date

def test_range_picker(landing_page):
  #Given the User is at the Form page.
  #When the User modifies the Range Picker to a specific value.
  web_form_under_test.move_Range_picker(range_picker_notches,"right")
  #Then said value should be displayed correctly on the associated field.
  assert web_form_under_test.get_range_picker_value()== web_form_under_test.get_range_picker_default_value()+range_picker_notches


def test_submit_button(browser):
  web_form_under_test = WebFormPage(browser)
  web_form_after_submit = Form_submitted_page(browser)
  web_form_under_test.load()
  # Given the user has filled all the mandatory fields on the form
  web_form_under_test.click_text_input()
  web_form_under_test.send_keys_to_text_input('Fill all the inputs')
  web_form_under_test.click_password_input()
  web_form_under_test.send_keys_to_password_input('MyTestPassword')
  web_form_under_test.click_textarea_input()
  web_form_under_test.send_keys_to_textarea_input('aQuestionablyLongTextString')
  #DROPDOWN TEST NOT WORKING - STEPS SHOULD GO HERE
  web_form_under_test.click_date_picker()
  web_form_under_test.send_keys_to_date_picker(date.today().strftime("%m/%d/%Y"))
  #File input test must be fixed first
  #Range test not done yet
  # When the User clicks the "Submit" button
  web_form_under_test.submit_form()
  # Then the page shows the message “Form submitted”
  assert web_form_after_submit.h_form_submitted_text() == h1_success_text
  # And the page shows the message “Received!”
  assert web_form_after_submit.message_correct_text() == correct_text





