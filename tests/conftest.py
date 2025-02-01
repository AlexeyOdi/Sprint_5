import pytest
from selenium import webdriver

@pytest.fixture(scope = "function")
def get_driver(request):
    driver = webdriver.Chrome()
    request.cls.driver = driver
    yield
    driver.quit()


