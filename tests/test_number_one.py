
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

def test_dropdown_datalist(browser):
  raise Exception("Incomplete Test")

def test_file_input(browser):
  # Given el usuario está en la página del formulario.
  #Arrange
  web_form_under_test = WebFormPage(browser)
  #path_to_file = "C:\\Users\\Usuario\\selenium-test-4\\env\\tests\\testFileName.png"
  file_name = "testFileName.png"
  file = os.path.join(os.getcwd(), file_name)
  web_form_under_test.load()

  #ACT
  # When el usuario carga un archivo a través del campo de entrada de archivo.
  web_form_under_test.send_keys_to_file_input(file)
  #web_form_under_test.click_file_input()
  #web_form_under_test.select_file_to_upload(path_to_file) #Here you should type the path in your system pointing to the test file in the tests folder
  #value.split(sep="\\")
  data = web_form_under_test.file_input_value()
  # Then el nombre del archivo debe mostrarse correctamente en el campo de entrada.
  assert file_name in data

def test_checkboxes(browser):
  # ARRANGE
  web_form_under_test = WebFormPage(browser)

  #ACT
  # Given el usuario está en la página del formulario.
  web_form_under_test.load()
  # When el usuario selecciona el checkbox por defecto.
  web_form_under_test.click_default_checkbox()
  #ASSERT
  # Then el estado del checkbox debe cambiar a "checked".
  assert web_form_under_test.default_checkbox_value()

def test_radiobuttons(browser):
  #ARRANGE
  #Given el usuario está en la página del formulario.
  web_form_under_test = WebFormPage(browser)
  web_form_under_test.load()
  #ACT
  #When el usuario selecciona un radio button por defecto.
  web_form_under_test.click_default_radiobutton()
  #ASSERT
  #Then el estado del radio button debe cambiar a "checked"
  assert web_form_under_test.default_radiobutton_value()
  #And los otros radio buttons deben quedar en estado "unchecked".
  assert web_form_under_test.checked_radiobutton_value() == None
def test_color_picker(browser):
  raise Exception("Incomplete Test")

def test_date_picker_format(browser):
  # Given el usuario está en la página del formulario.
  my_date = date.today().strftime("%m/%d/%Y") #Fecha formateada en americano
  day_value = my_date.split('/')[1]
  web_form_under_test = WebFormPage(browser)
  web_form_under_test.load()
  # When el usuario selecciona una fecha válida en el selector de fecha.
  web_form_under_test.date_picker.click()
  web_form_under_test.click_date_day_element(day_value)
  # Then la fecha seleccionada debe reflejarse correctamente en el campo.
  assert web_form_under_test.date_picker_value() == my_date

def test_past_date(browser):
  # Given el usuario está en la página del formulario.

  #my_date = date.today().strftime("%m/%d/%Y") # Consigo fecha de hoy en Formato Americano
  my_date = date.today()
  calculate_date = my_date - relativedelta(years=2, months=2, days=2)
  target_date = calculate_date.strftime("%m/%d/%Y")
  target_year = target_date.split("/")[2]
  target_day = target_date.split("/")[1]
  # When el usuario selecciona una fecha igual a la fecha actual pero dos años, dos meses y dos días atrás
  web_form_under_test = WebFormPage(browser)
  web_form_under_test.load()
  web_form_under_test.click_date_picker()
  web_form_under_test.date_picker_switch_deploy_and_click()
  web_form_under_test.date_picker_switch_click_years(target_year)
  web_form_under_test.date_picker_switch_find_and_click_month(calculate_date.strftime("%B")[0:3])
  web_form_under_test.click_date_day_element(target_day)
  time.sleep(2)
  # Then la fecha seleccionada debe reflejarse correctamente en el campo.
  assert web_form_under_test.date_picker_value() == target_date

def test_manual_date_picker_date(browser):
  # Given el usuario está en la página del formulario.
  web_form_under_test = WebFormPage(browser)
  web_form_under_test.load()
  # When el usuario ingresa directamente una fecha válida en el selector de fecha.
  web_form_under_test.click_date_picker()
  target_date = date.today().strftime("%m/%d/%Y")
  web_form_under_test.send_keys_to_date_picker(target_date)
  # Then la fecha seleccionada debe reflejarse correctamente en el campo.
  assert web_form_under_test.date_picker_value() == target_date

def test_future_date(browser):
  my_date = date.today()
  calculate_date = my_date + relativedelta(years=1, months=1, days=1)
  target_date = calculate_date.strftime("%m/%d/%Y")
  target_year = target_date.split("/")[2]
  target_day = target_date.split("/")[1]
  web_form_under_test = WebFormPage(browser)
  # Given the user is viewing the form page
  web_form_under_test.load()
  # When the user selects a date in the the future
  web_form_under_test.click_date_picker()
  web_form_under_test.date_picker_switch_deploy_and_click()
  web_form_under_test.date_picker_switch_click_years(target_year)
  web_form_under_test.date_picker_switch_find_and_click_month(calculate_date.strftime("%B")[0:3])
  web_form_under_test.click_date_day_element(target_day)
  # Then the selected date must be correctly displayed in its corresponding field.
  assert web_form_under_test.date_picker_value() == target_date

def test_range_picker(browser):
  notches = 2
  #Given the User is at the Form page.
  web_form_under_test = WebFormPage(browser)
  web_form_under_test.load()
  #When the User modifies the Range Picker to a specific value.
  web_form_under_test.move_Range_picker(notches,"right")
  #Then said value should be displayed correctly on the associated field.
  assert web_form_under_test.get_range_picker_value()== web_form_under_test.get_range_picker_default_value()+notches


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
  #Datalist thing not done yet
  #File input test must be fixed first
  #Range test not done yet
  # When the User clicks the "Submit" button
  web_form_under_test.submit_form()
  # Then the page shows the message “Form submitted”
  h1_success = 'Form submitted' # MUST FIX OBJECT MODEL LOGIC TO AVOID HAVING THIS CODE HERE
  assert web_form_after_submit.h_form_submitted_text() == h1_success
  # And the page shows the message “Received!”
  correct_text = 'Received!' # MUST FIX OBJECT MODEL LOGIC TO AVOID HAVING THIS CODE HERE
  assert web_form_after_submit.message_correct_text() == correct_text





