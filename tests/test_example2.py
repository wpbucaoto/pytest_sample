from pylenium.driver import Pylenium
import pytest
from pylenium.config import PyleniumConfig, TestCase

@pytest.fixture(scope='function')
def browser():
    #py = Pylenium()
    config = PyleniumConfig()
    config.driver.browser = 'chrome'

    # Create a TestCase config (optional, you can customize it as needed)
    #test_case = TestCase(name="test_load_page", file_path="test_example2.py")

    # Initialize Pylenium with the created config
    py = Pylenium(config)
    py.visit('https://google.com')
    yield py
    py.quit()


def test_load_page(browser):
    try:
        consent_button = browser.get('[id="W0wltc"]', timeout=10)  # Wait for the element
        if consent_button.is_displayed():
            consent_button.click()
    except:
        pass  # If the element is not found, ignore and continue
    browser.get('[name="q"]').type('puppy')
    browser.get('[name="btnK"]').submit()
    assert browser.contains('puppy')