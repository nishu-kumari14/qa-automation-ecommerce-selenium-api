from automation.pages.cart_page import CartPage
from automation.pages.checkout_page import CheckoutPage
from automation.pages.inventory_page import InventoryPage


def test_add_product_to_cart(logged_in_driver):
    inventory_page = InventoryPage(logged_in_driver)
    cart_page = CartPage(logged_in_driver)

    product_name = "Sauce Labs Backpack"

    inventory_page.add_product_to_cart(product_name)
    assert inventory_page.get_cart_badge_count() == "1"

    inventory_page.open_cart()
    assert cart_page.has_product(product_name)


def test_complete_checkout_flow(logged_in_driver):
    inventory_page = InventoryPage(logged_in_driver)
    cart_page = CartPage(logged_in_driver)
    checkout_page = CheckoutPage(logged_in_driver)

    inventory_page.add_product_to_cart("Sauce Labs Backpack")
    inventory_page.open_cart()
    cart_page.checkout()

    checkout_page.fill_checkout_info("Hemanth", "QA", "500001")
    checkout_page.finish_checkout()

    assert checkout_page.get_completion_message() == "Thank you for your order!"
