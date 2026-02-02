from selenium.webdriver.common.by import By

from automation.pages.base_page import BasePage


class InventoryPage(BasePage):
    INVENTORY_CONTAINER = (By.ID, "inventory_container")
    CART_BADGE = (By.CSS_SELECTOR, "span.shopping_cart_badge")
    CART_ICON = (By.CSS_SELECTOR, "a.shopping_cart_link")
    MENU_BUTTON = (By.ID, "react-burger-menu-btn")
    LOGOUT_LINK = (By.ID, "logout_sidebar_link")
    LOGIN_USERNAME_INPUT = (By.ID, "user-name")

    @staticmethod
    def _slugify_product_name(product_name):
        return product_name.strip().lower().replace(" ", "-")

    def wait_until_loaded(self):
        if not self.is_visible(self.INVENTORY_CONTAINER):
            raise AssertionError(
                f"Inventory page did not load. Current URL: {self.driver.current_url}"
            )

    def add_product_to_cart(self, product_name):
        self.wait_until_loaded()
        product_slug = self._slugify_product_name(product_name)
        add_to_cart_button = (
            By.CSS_SELECTOR,
            f"button[data-test='add-to-cart-{product_slug}']",
        )
        remove_button = (
            By.CSS_SELECTOR,
            f"button[data-test='remove-{product_slug}']",
        )

        for _ in range(3):
            self.click_js(add_to_cart_button)
            if self.is_visible(remove_button):
                return

        raise AssertionError(
            f"Unable to add product '{product_name}' to cart. Current URL: {self.driver.current_url}"
        )

    def get_cart_badge_count(self):
        return self.get_text(self.CART_BADGE)

    def open_cart(self):
        for _ in range(3):
            self.click(self.CART_ICON)
            if "cart.html" in self.driver.current_url:
                return

        self.driver.get("https://www.saucedemo.com/cart.html")
        self.wait_for_url_contains("cart.html")

    def logout(self):
        for _ in range(3):
            self.click_js(self.MENU_BUTTON)
            self.is_visible(self.LOGOUT_LINK)
            self.click_js(self.LOGOUT_LINK)

            if self.is_visible(self.LOGIN_USERNAME_INPUT):
                return

        raise AssertionError(
            f"Logout did not navigate to login page. Current URL: {self.driver.current_url}"
        )
