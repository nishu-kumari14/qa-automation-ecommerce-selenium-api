from automation.pages.inventory_page import InventoryPage
from automation.pages.login_page import LoginPage


def test_logout(logged_in_driver):
    inventory_page = InventoryPage(logged_in_driver)

    inventory_page.logout()

    login_page = LoginPage(logged_in_driver)
    assert login_page.is_visible(login_page.USERNAME_INPUT)

    logged_in_driver.get("https://www.saucedemo.com/inventory.html")
    assert "inventory.html" not in logged_in_driver.current_url
