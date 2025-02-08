




  # The browser argument passed to the function comes from the conftest.py file. That file contains a fixture
  # that is used for setup and cleanup of every individual test, so, whenever a test is executed
  # first is executed whatever comes before the yield statement contained in the fixture (setup)
  # and after the test is finished, whatever comes AFTER the yield statement gets executed (cleanup).
  # The conftest.py file must be located at the tests file. I think it's pytest what loads whatever is in there
  # to bring the arguments here, im not quite sure.


import os
from pages.web_form_se import WebFormPage
from pages.form_submitted import Form_submitted_page
from tests.conftest import browser


  # Escenario 1: Validar el campo de texto

def test_prueba_uno(browser):

  #ARRANGE
  correct_text = 'Received!' #Esta var asumo debería ir en el page obejct y no acá pero ni idea de como es la jugada, Aiura nawel pls
  h1_success = 'Form submitted'
  test_keys = 'charvarious'

  web_form_under_test = WebFormPage(browser) #Pag. de inicio del form
  web_form_after_submit = Form_submitted_page(browser) #Pagina una vez enviado el form

  #ACT
  # Given the User is in the web form page
  web_form_under_test.load()

  # When el usuario ingresa un texto válido en el campo de texto
  web_form_under_test.click_text_input()
  web_form_under_test.send_keys_to_text_input(test_keys)
  web_form_under_test.submit_form()

  #ASSERT
  # Then el campo debe aceptar el texto y no mostrar mensajes de error
  assert web_form_after_submit.message_correct_text() == correct_text
  assert web_form_after_submit.h_form_submitted_text() == h1_success
  curr_url = browser.current_url
  assert test_keys in curr_url

def test_password_field(browser):
  # ARRANGE
  correct_text = 'Received!' #Esta var asumo debería ir en el page obejct y no acá pero ni idea de como es la jugada, Aiura nawel pls
  h1_success = 'Form submitted'
  test_keys = 'Jhostynxon_Garcia'

  #get the password field, click it, send keys, submit
  web_form_under_test = WebFormPage(browser)  # Pag. de inicio del form
  web_form_after_submit = Form_submitted_page(browser)  # Pagina una vez enviado el form

  # Given usuario está en la página del formulario.
  web_form_under_test.load()

  # ACT
  # When el usuario ingresa una contraseña válida en el campo de contraseña
  web_form_under_test.click_password_input()
  web_form_under_test.send_keys_to_password_input(test_keys)
  assert web_form_under_test.password_input_value() == test_keys
  # Then el campo debe aceptar la contraseña y no mostrar mensajes de error.
  web_form_under_test.submit_form()

  # ASSERT
  curr_url = browser.current_url
  assert web_form_after_submit.message_correct_text() == correct_text
  assert web_form_after_submit.h_form_submitted_text() == h1_success
  assert test_keys in curr_url

def test_textarea(browser):
  # ARRANGE
  correct_text = 'Received!'  # Esta var asumo debería ir en el page obejct y no acá pero ni idea de como es la jugada, Aiura nawel pls
  h1_success = 'Form submitted'
  test_keys = "atestinputiguess"

  web_form_under_test = WebFormPage(browser)  # Pag. de inicio del form
  web_form_after_submit = Form_submitted_page(browser)  # Pagina una vez enviado el form

  # Given usuario está en la página del formulario.
  web_form_under_test.load()

  # ACT
  # When el usuario ingresa un texto en el textarea
  # get the textarea, click it, send keys, submit
  web_form_under_test.click_textarea_input()
  web_form_under_test.send_keys_to_textarea_input(test_keys)
  # Then el textarea debe aceptar el texto y mostrarlo correctamente.
  web_form_under_test.submit_form()

  # pytest -s .\test_number_one.py::test_textarea
  # ASSERT
  assert web_form_after_submit.message_correct_text() == correct_text
  assert web_form_after_submit.h_form_submitted_text() == h1_success
  curr_url = browser.current_url
  assert test_keys in curr_url

def test_disabled_input(browser):
  # ARRANGE
  web_form_under_test = WebFormPage(browser)  # Pag. de inicio del form

  # Given usuario está en la página del formulario.
  web_form_under_test.load()

  # ACT
  # When el usuario intenta interactuar con el campo de entrada deshabilitado.
  # Then el campo debe tener la propiedad disabled en su locator.

  # ASSERT
  assert web_form_under_test.disabled_input_value()

def test_readonly_input(browser):
  # ARRANGE
  web_form_under_test = WebFormPage(browser)

  # Given el usuario está en la página del formulario.
  web_form_under_test.load()

  # ACT
  # When el usuario intenta editar el campo de entrada de solo lectura.
  # Then el campo debe tener la propiedad readonly en su locator.
  assert web_form_under_test.readonly_text_field_value()

def test_dropdown_select(browser):
  # ARRANGE
  web_form_under_test = WebFormPage(browser)  # Pag. de inicio del form

  # Given usuario está en la página del formulario.
  web_form_under_test.load()

  # ACT
  # When el usuario selecciona una opción del dropdown (select).
  web_form_under_test.click_dropdown_select()
  web_form_under_test.click_dropdown_select_option()
  # Then la opción seleccionada debe reflejarse correctamente en el campo.
  # ASSERT
  assert web_form_under_test.dropdown_select_current_value() == web_form_under_test.dropdown_select_option_value()

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

def test_color_picker(browser):
  # Given el usuario está en la página del formulario.
  web_form_under_test = WebFormPage(browser)
  # When el usuario ingresa los valores RGB para un color en el selector de color.
  # Then el color seleccionado debe reflejarse correctamente en el campo.

def test_date_picker_format(browser):
  raise Exception("Incomplete Test")

def test_past_date(browser):
  raise Exception("Incomplete Test")

def test_manual_date_picker_date(browser):
  raise Exception("Incomplete Test")

def test_future_date(browser):
  raise Exception("Incomplete Test")

def test_floating_elements(browser):
  raise Exception("Incomplete Test")

def test_submit_button(browser):
  raise Exception("Incomplete Test")