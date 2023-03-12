import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service


class WebDriverWrapper:
    driver = None

    @pytest.fixture(scope="function", autouse=True)
    def browser_config(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.implicitly_wait(20)
        self.driver.get("https://opensource-demo.orangehrmlive.com/")
        yield
        self.driver.quit()

# class WebDriverWrapper:
#     @pytest.fixture(scope="function", autouse=True)
#     def browser_config(self):
#         serv_driver = Service(executable_path=r"C:\Users\JiDi\Downloads\chromedriver_win32 (5)\chromedriver.exe")
#         self.driver = webdriver.Chrome(service=serv_driver)
#         self.driver.maximize_window()
#         self.driver.implicitly_wait(20)
#         self.driver.get("https://opensource-demo.orangehrmlive.com/")
#         yield
#         self.driver.quit()
#
# class TestLogin(WebDriverWrapper):
#     def test_valid_login(self):
#         self.driver.find_element(By.NAME, "username").send_keys("Admin")
#         self.driver.find_element(By.NAME, "password").send_keys("admin123")
#         self.driver.find_element(By.XPATH, "//button[normalize-space()='Login']").click()
#         actual_text = self.driver.find_element(By.XPATH, "//h6[normalize-space()='Dashboard']").text
#         assert_that("Dashboard").is_equal_to(actual_text)
#
#     def test_invalid_login(self):
#        passclass TestLogin(WebDriverWrapper)
#
#     def test_title(self):
#         actual_title = self.driver.title
#         assert_that("OrangeHRM").is_equal_to(actual_title)
#     def test_header(self):
#         actual_header = self.driver.find_element(By.XPATH, "//h5").text
#         assert_that("Login").is_equal_to(actual_header)
#
#     def test_login_placeholder(self):
#         actual_username_placeholder = self.driver.find_element(By.NAME,"username").get_attribute("placeholder")
#         actual_password_placeholder = self.driver.find_element(By.NAME,"password").get_attribute("placeholder")
#         assert_that("Username").is_equal_to(actual_username_placeholder)
#         assert_that("Password").is_equal_to(actual_password_placeholder)
#
#     def test_invalid_login(self):
#         self.driver.find_element(By.NAME, "username").send_keys("Admin123")
#         self.driver.find_element(By.NAME, "password").send_keys("admin12893")
#         self.driver.find_element(By.XPATH, "//button[@type='submit']").click()
#         actual_error = self.driver.find_element(By.XPATH, "//p[contains(@class ,'oxd-alert-content-text')]").text
#         print(actual_error)
#         assert_that("Invalid credentials").is_equal_to(actual_error)