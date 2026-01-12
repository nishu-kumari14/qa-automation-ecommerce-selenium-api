from selenium.webdriver.common.by import By

from automation.pages.base_page import BasePage


class CheckoutPage(BasePage):
    FIRST_NAME = (By.ID, "first-name")
    LAST_NAME = (By.ID, "last-name")
    POSTAL_CODE = (By.ID, "postal-code")
    CONTINUE_BUTTON = (By.ID, "continue")
    FINISH_BUTTON = (By.ID, "finish")
    COMPLETE_HEADER = (By.CSS_SELECTOR, "h2.complete-header")

    def fill_checkout_info(self, first_name, last_name, postal_code):
        self.type_text(self.FIRST_NAME, first_name)
        self.type_text(self.LAST_NAME, last_name)
        self.type_text(self.POSTAL_CODE, postal_code)
        for _ in range(3):
            self.click_js(self.CONTINUE_BUTTON)
            if "checkout-step-two.html" in self.driver.current_url:
                return

        self.wait_for_url_contains("checkout-step-two.html")

    def finish_checkout(self):
        self.click_js(self.FINISH_BUTTON)
        self.wait_for_url_contains("checkout-complete.html")

    def get_completion_message(self):
        return self.get_text(self.COMPLETE_HEADER)
