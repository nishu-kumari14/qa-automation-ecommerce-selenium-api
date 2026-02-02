import os

import pytest
from dotenv import load_dotenv
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

from automation.pages.inventory_page import InventoryPage
from automation.pages.login_page import LoginPage


load_dotenv()


def pytest_configure(config):
    os.makedirs("reports", exist_ok=True)
    os.makedirs("screenshots", exist_ok=True)


def pytest_addoption(parser):
    parser.addoption(
        "--browser-mode",
        action="store",
        default=os.getenv("BROWSER_MODE", "headed"),
        choices=["headed", "headless"],
        help="Run browser in headed or headless mode",
    )


@pytest.fixture(scope="session")
def credentials():
    return {
        "standard_user": os.getenv("SAUCE_STANDARD_USER", "standard_user"),
        "locked_user": os.getenv("SAUCE_LOCKED_USER", "locked_out_user"),
        "password": os.getenv("SAUCE_PASSWORD", "secret_sauce"),
    }


@pytest.fixture(scope="function")
def driver(request):
    browser_mode = request.config.getoption("--browser-mode")

    options = Options()
    options.add_argument("--window-size=1920,1080")
    options.add_argument("--disable-gpu")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")

    if browser_mode == "headless":
        options.add_argument("--headless=new")

    service = Service(ChromeDriverManager().install())
    driver_instance = webdriver.Chrome(service=service, options=options)
    driver_instance.implicitly_wait(3)

    yield driver_instance

    driver_instance.quit()


@pytest.fixture(scope="function")
def logged_in_driver(driver, credentials):
    login_page = LoginPage(driver)
    inventory_page = InventoryPage(driver)
    login_page.load()
    login_page.login(credentials["standard_user"], credentials["password"])
    inventory_page.wait_until_loaded()
    return driver


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()

    if report.when != "call" or report.passed:
        return

    driver = item.funcargs.get("driver") or item.funcargs.get("logged_in_driver")
    if driver is None:
        return

    safe_test_name = (
        item.nodeid.replace("::", "_").replace("/", "_").replace("\\", "_")
    )
    screenshot_path = os.path.join("screenshots", f"{safe_test_name}.png")
    driver.save_screenshot(screenshot_path)
