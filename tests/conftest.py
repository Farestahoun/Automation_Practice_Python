import pytest
from selenium import webdriver


@pytest.fixture()
def setUp_main():
    print("Running method level setUp")
    yield
    print("Running method level tearDown")


@pytest.fixture()
def oneTimeSetUp(request, browser):
    driver = None
    print("Running one time setUp")
    if browser == "Chrome":
        driver = webdriver.Chrome("C:\\Users\\sedky\\PycharmProjects\\Automation_Practice\\Basics\\libs\\chromedriver.exe")
        driver.get("https://www.expedia.com/")
        driver.maximize_window()

    elif browser == "FF":
        driver = webdriver.Firefox("C:\\Users\\sedky\\PycharmProjects\\Automation_Practice\\Basics\\libs\\chromedriver.exe")
    elif browser == "Safari":
        driver = webdriver.Safari("C:\\Users\\sedky\\PycharmProjects\\Automation_Practice\\Basics\\libs\\chromedriver.exe")
    else:
        print("Undefined WebDriver")

    if request.cls is not None:
        request.cls.driver = driver

    yield driver
    driver.quit()
    print("Running one time tearDown")


def pytest_addoption(parser):
    parser.addoption("--browser")
    parser.addoption("--osType", help="Type of operating system")


@pytest.fixture()
def browser(request):
    return request.config.getoption("--browser")


@pytest.fixture()
def osType(request):
    return request.config.getoption("--osType")
