"""
This module contains shared fixtures.
"""

import pytest
import selenium.webdriver
from pages.web_form_se import WebFormPage

@pytest.fixture
def browser():
  # Initialize the ChromeDriver instance
  b = selenium.webdriver.Chrome()
  # Make its calls wait up to 10 seconds for elements to appear
  b.implicitly_wait(5)
  # Return the WebDriver instance for the setup
  yield b
  # Quit the WebDriver instance for the cleanup
  b.quit()

@pytest.fixture
def landing_page(browser):
  web_form_under_test = WebFormPage(browser)
  web_form_under_test.load()
  return web_form_under_test