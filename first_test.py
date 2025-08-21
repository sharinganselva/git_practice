import pytest
from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy


@pytest.fixture(scope="module")
def driver():
    caps = {
        "platformName": "iOS",
        "platformVersion": "17.2",
        "deviceName": "iPhone 15",
        "automationName": "XCUITEST",
        "app": "path/to/app",
        "noReset": True
    }

    driver = webdriver.Remote("http://127.0.0.1:4723", caps)
    yield driver
    driver.quit()


def test_example(driver):
    el = driver.find_element(AppiumBy.ACCESSIBILITY_ID, "LoginButton")
    el.click()
    # assert
