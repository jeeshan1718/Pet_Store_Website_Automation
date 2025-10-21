import os
import time

import pytest
from selenium import webdriver

@pytest.fixture
def setup():
    driver = webdriver.Chrome()
    driver.get("https://jpetstore.aspectran.com/")  # example JPetStore URL
    driver.maximize_window()

    yield driver
    driver.quit()


@pytest.hookimpl(hookwrapper=True, tryfirst=True)
def pytest_runtest_makereport(item, call):
    # Run all other hooks to get the report object
    outcome = yield
    rep = outcome.get_result()

    # Only capture when the test has failed
    if rep.when == "call" and rep.failed:
        driver = item.funcargs.get("setup")  # get driver from fixture
        if driver:
            screenshot_folder = "Screen_shots"
            os.makedirs(screenshot_folder, exist_ok=True)

            timestamp = time.strftime("%Y%m%d-%H%M%S")
            file_name = f"{screenshot_folder}/{item.name}_{timestamp}.png"

            driver.save_screenshot(file_name)
            print(f"\nScreenshot saved to {file_name}")


@pytest.hookimpl(hookwrapper=True, tryfirst=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()

    if rep.when == "call" and rep.failed:
        driver = item.funcargs.get("setup")
        if driver:
            screenshot_folder = "Reports/"
            os.makedirs(screenshot_folder, exist_ok=True)

            timestamp = time.strftime("%Y%m%d-%H%M%S")
            file_name = f"{screenshot_folder}/{item.name}_{timestamp}.png"

            driver.save_screenshot(file_name)
            print(f"\nScreenshot saved to {file_name}")
