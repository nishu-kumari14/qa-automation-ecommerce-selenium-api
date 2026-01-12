from selenium.webdriver.common.by import By

from automation.pages.base_page import BasePage


class InventoryPage(BasePage):
    INVENTORY_CONTAINER = (By.ID, "inventory_container")
    CART_BADGE = (By.CSS_SELECTOR, "span.shopping_cart_badge")
    CART_ICON = (By.ID, "shopping_cart_container")
    MENU_BUTTON = (By.ID, "react-burger-menu-btn")
    LOGOUT_LINK = (By.ID, "logout_sidebar_link")
    LOGIN_USERNAME_INPUT = (By.ID, "user-name")

    def add_product_to_cart(self, product_name):
        add_to_cart_button = (
            By.XPATH,
            f"//div[text()='{product_name}']/ancestor::div[@class='inventory_item']//button",
        )
        self.click(add_to_cart_button)

    def get_cart_badge_count(self):
        return self.get_text(self.CART_BADGE)

    def open_cart(self):
        self.click(self.CART_ICON)
        self.wait_for_url_contains("cart.html")

    def logout(self):
        self.click_js(self.MENU_BUTTON)
        self.click_js(self.LOGOUT_LINK)
        self.is_visible(self.LOGIN_USERNAME_INPUT)
