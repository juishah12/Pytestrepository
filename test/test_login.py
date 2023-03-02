import pytest
from selenium import webdriver
from assertpy import assert_that
from selenium.webdriver.common.by import By


class TestLoginUI:
    @pytest.fixture(scope="function",autouse=True)
    def setup(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.implicitly_wait(20)
        self.driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
        yield
        self.driver.quit()

    def test_title(self,setup):

        actual_title = self.driver.title
        #assert actual_title == "OrangeHRM"
        assert_that("OrangeHRM").is_equal_to(actual_title)
    def test_header(self,setup):
        actual_header = self.driver.find_element(By.XPATH,"//h5").text
        #text = driver.find_element(By.XPATH, "//h5[text()='Login']")
        assert_that("Login").is_equal_to(actual_header)

    def test_forgot_link(self,setup):


