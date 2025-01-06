import time
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import Locators  # Import the Locators class
from credentials import credentials  # Import the Credentials class

@pytest.fixture
def driver():
    # Setup WebDriver
    driver = webdriver.Chrome()
    yield driver
    # Cleanup
    driver.quit()

def test_login(driver):
        driver.get("https://devv2.voyager.marsvh.com/login")
        driver.maximize_window()

        # Wait until the Sign In button is clickable and then click it
        sign_in_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, Locators.sign_in_button()))  # Use static method
        )
        sign_in_button.click()

        # Verify the title of the page
        WebDriverWait(driver, 10).until(
            EC.title_is("Mars Group - Sign In")
        )
        print("Title is correct!")

        # Enter username
        username_input = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, Locators.username()))  # Use static method
        )
        username_input.send_keys(credentials.username())  # Use the Credentials class

        # Click submit
        submit_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, Locators.submit_button()))  # Use static method
        )
        submit_button.click()

        # Enter password
        password_input = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, Locators.password()))  # Use static method
        )
        password_input.send_keys(credentials.password())  # Use the Credentials class

        # Click Verify for password
        verify_button = driver.find_element(By.XPATH, Locators.password_verify_button())
        verify_button.click()

        # Security Question
        security_question = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, Locators.security_question()))
        )
        security_question.send_keys(credentials.security_question())  # Use the Credentials class

        # Verify button for SQ - button click
        submit_buttonSQ = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, Locators.click_buttonSQ()))
        )
        submit_buttonSQ.click()

        time.sleep(10)

        # Wait for the verification process to complete (adjust as necessary)
        WebDriverWait(driver, 15).until(
            EC.url_changes("https://devv2.voyager.marsvh.com/login")
        )


        # Validate successful login by checking the page title or an element visible after login
        # assert "Dashboard - MARS " in driver.title, "Login failed or incorrect page title"
        # WebDriverWait(driver, 10).until(
        #     EC.title_is("Da
def test_Choose_business_Type(driver):
    choose_business_type = WebDriverWait(driver,10).until(EC.presence_of_element_located(By.XPATH,))