# conftest.py
import os

import pytest
from selenium.webdriver.chrome.options import Options
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager




@pytest.fixture(scope="session")
def driver():
    chrome_options = Options()
    chrome_options.add_argument("--incognito")  # Enable incognito mode
    chrome_options.add_argument("--start-maximized")  # Optional: start maximized

    driver = webdriver.Chrome(
        service=Service(ChromeDriverManager().install()),
        options=chrome_options
    )

    driver.get("https://dstudio.com.bd/")

    yield driver

    driver.quit()


def pytest_html_results_table_header(cells):
    cells.insert(2, "Description")

def pytest_html_results_table_row(report, cells):
    cells.insert(2, getattr(report, "description", "No description"))

@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    # Get the standard report object
    outcome = yield
    report = outcome.get_result()

    # Attach the docstring as description
    if hasattr(item, "function"):
        report.description = str(item.function.__doc__) if item.function.__doc__ else "No description"

    # On failure, capture screenshot
    if report.when == "call" and report.failed:
        driver = item.funcargs.get("driver", None)
        if driver:
            # Define screenshot directory
            screenshot_dir = os.path.join(os.getcwd(), "screenshots")
            os.makedirs(screenshot_dir, exist_ok=True)

            # Save screenshot with test name
            file_path = os.path.join(screenshot_dir, f"{item.name}.png")
            driver.save_screenshot(file_path)
            print(f"\n Screenshot saved to: {file_path}")

