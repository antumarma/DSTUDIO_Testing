import pytest
import time
from contact_page import ContactPage


@pytest.mark.sanity
def test_navigate_to_contact_page(driver):
    contact_page = ContactPage(driver)
    time.sleep(1)
    contact_page.navigate_to_contact_page()
    time.sleep(2)

@pytest.mark.sanity
def test_empty_data(driver):
    contact_page = ContactPage(driver)

    contact_page.clear_field()

    contact_page.enter_name("")
    time.sleep(0.5)
    contact_page.enter_email("")
    time.sleep(0.5)
    contact_page.enter_message("")
    time.sleep(0.5)
    contact_page.click_send_us()
    time.sleep(2)

@pytest.mark.sanity
def test_invalid_email(driver):
    contact_page = ContactPage(driver)

    contact_page.clear_field()

    contact_page.enter_name("Test User")
    time.sleep(0.5)
    contact_page.enter_email("test.com")
    time.sleep(0.5)
    contact_page.enter_message("Test message with invalid email.")
    time.sleep(1)
    contact_page.click_send_us()
    time.sleep(3)

@pytest.mark.sanity
def test_leave_name(driver):
    contact_page = ContactPage(driver)

    contact_page.clear_field()

    contact_page.enter_name("")
    time.sleep(0.5)
    contact_page.enter_email("test@gmail.com")
    time.sleep(0.5)
    contact_page.enter_message("Test message without Name .")
    time.sleep(1)
    contact_page.click_send_us()
    time.sleep(3)

@pytest.mark.sanity
def test_leave_email(driver):
    contact_page = ContactPage(driver)

    contact_page.clear_field()

    contact_page.enter_name("Test User")
    time.sleep(0.5)
    contact_page.enter_email("")
    time.sleep(0.5)
    contact_page.enter_message("Test message without Email .")
    time.sleep(0.5)
    contact_page.click_send_us()
    time.sleep(1)

@pytest.mark.sanity
def test_leave_message(driver):
    contact_page = ContactPage(driver)

    contact_page.clear_field()

    contact_page.enter_name("Test User")
    time.sleep(0.5)
    contact_page.enter_email("Test123@gmail.com")
    time.sleep(0.5)
    contact_page.enter_message("")
    time.sleep(0.5)
    contact_page.click_send_us()
    time.sleep(1)

@pytest.mark.sanity
def test_valid_data(driver):

    contact_page = ContactPage(driver)

    contact_page.clear_field()

    contact_page.enter_name("Test User")
    time.sleep(1)
    contact_page.enter_email("test@gmail.com")
    time.sleep(1)
    contact_page.enter_message("This is a test message.")
    time.sleep(1)
    contact_page.click_send_us()
    time.sleep(3)

