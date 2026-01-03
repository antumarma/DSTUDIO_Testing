from selenium import webdriver
from selenium.webdriver.common.by import By

class ContactPage:
    def __init__(self, driver):
        self.driver = driver

    def navigate_to_contact_page(self):
        contact_link = self.driver.find_element(By.XPATH, "/html[1]/body[1]/div[1]/div[1]/section[1]/nav[1]/div[1]/div[3]/ul[1]/li[13]/a[1]")
        contact_link.click()

    def enter_name(self, name):
        self.driver.find_element(By.ID, "name").send_keys(name)

    def enter_email(self, email):
        self.driver.find_element(By.ID, "email").send_keys(email)


    def enter_message(self, message):
        self.driver.find_element(By.ID, "message").send_keys(message)

    def click_send_us(self):
        submit_button = self.driver.find_element(By.XPATH, "/html[1]/body[1]/div[12]/div[1]/div[2]/form[1]/div[4]/button[1]")
        submit_button.click()

    def clear_field(self):
        self.driver.find_element(By.ID, "name").clear()
        self.driver.find_element(By.ID, "email").clear()
        self.driver.find_element(By.ID, "message").clear()
