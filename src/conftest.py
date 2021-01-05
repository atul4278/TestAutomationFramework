from selenium import webdriver
import pytest
import json


def pytest_addoption(parser):
    parser.addoption("--browser", default="chrome",
                     help="list of stringinputs to pass to test functions")


@pytest.fixture(scope='function', autouse=True)
def driver():
    driver = webdriver.Chrome(executable_path='drivers/chromedriver')
    yield driver
    driver.quit()


@pytest.fixture(scope='function', autouse=True)
def launch_sausedemo(driver, pytestconfig, request):
    driver.get("https://www.saucedemo.com")


@pytest.fixture(scope='function', autouse=True)
def data():
    with open('./config/framework.settings.json') as f:
        dataObj = json.load(f)
        
    return dataObj
    