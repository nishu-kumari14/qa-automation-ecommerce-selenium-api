from selenium.webdriver.common.by import By

from automation.pages.base_page import BasePage


class CartPage(BasePage):
    CHECKOUT_BUTTON = (By.ID, "checkout")

    def has_product(self, product_name):
        product_locator = (By.XPATH, f"//div[@class='inventory_item_name' and text()='{product_name}']")
        return self.is_visible(product_locator)

    def checkout(self):
        self.click(self.CHECKOUT_BUTTON)
