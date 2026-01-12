from automation.pages.inventory_page import InventoryPage
from automation.pages.login_page import LoginPage


def test_successful_login(driver, credentials):
    login_page = LoginPage(driver)
    inventory_page = InventoryPage(driver)

    login_page.load()
    login_page.login(credentials["standard_user"], credentials["password"])

    assert "inventory.html" in driver.current_url
    assert inventory_page.is_visible(inventory_page.INVENTORY_CONTAINER)


def test_locked_user_login_shows_error(driver, credentials):
    login_page = LoginPage(driver)

    login_page.load()
    login_page.login(credentials["locked_user"], credentials["password"])

    error_text = login_page.get_error_message().lower()
    assert "sorry" in error_text
    assert "locked out" in error_text
