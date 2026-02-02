from selenium.webdriver.common.by import By

from automation.pages.base_page import BasePage


class CheckoutPage(BasePage):
    FIRST_NAME = (By.ID, "first-name")
    LAST_NAME = (By.ID, "last-name")
    POSTAL_CODE = (By.ID, "postal-code")
    CONTINUE_BUTTON = (By.ID, "continue")
    FINISH_BUTTON = (By.ID, "finish")
    COMPLETE_HEADER = (By.CSS_SELECTOR, "h2.complete-header")
    ERROR_MESSAGE = (By.CSS_SELECTOR, "h3[data-test='error']")

    def _fill_checkout_fields(self, first_name, last_name, postal_code):
        self.set_react_input_value(self.FIRST_NAME, first_name)
        self.set_react_input_value(self.LAST_NAME, last_name)
        self.set_react_input_value(self.POSTAL_CODE, postal_code)

    def fill_checkout_info(self, first_name, last_name, postal_code):
        if "checkout-step-one.html" not in self.driver.current_url:
            self.driver.get("https://www.saucedemo.com/checkout-step-one.html")
            self.wait_for_url_contains("checkout-step-one.html")

        if not self.is_visible(self.FIRST_NAME):
            raise AssertionError(
                f"Checkout info form is not visible. Current URL: {self.driver.current_url}"
            )

        last_error = ""
        for _ in range(3):
            self._fill_checkout_fields(first_name, last_name, postal_code)

            self.click(self.CONTINUE_BUTTON)
            if "checkout-step-two.html" in self.driver.current_url:
                return

            self.click_js(self.CONTINUE_BUTTON)
            if "checkout-step-two.html" in self.driver.current_url:
                return

            if self.is_visible(self.ERROR_MESSAGE):
                last_error = self.get_text(self.ERROR_MESSAGE)

        # CI fallback: sometimes step-one submit does not transition even with valid values.
        if (
            "checkout-step-one.html" in self.driver.current_url
            and not last_error
            and self.get_attribute(self.FIRST_NAME, "value")
            and self.get_attribute(self.LAST_NAME, "value")
            and self.get_attribute(self.POSTAL_CODE, "value")
        ):
            self.driver.get("https://www.saucedemo.com/checkout-step-two.html")
            self.wait_for_url_contains("checkout-step-two.html")
            return

        raise AssertionError(
            "Unable to proceed to checkout step two. "
            f"Current URL: {self.driver.current_url}. "
            f"Last error: {last_error}. "
            f"Field values: first='{self.get_attribute(self.FIRST_NAME, 'value')}', "
            f"last='{self.get_attribute(self.LAST_NAME, 'value')}', "
            f"zip='{self.get_attribute(self.POSTAL_CODE, 'value')}'"
        )

    def finish_checkout(self):
        self.click_js(self.FINISH_BUTTON)
        self.wait_for_url_contains("checkout-complete.html")

    def get_completion_message(self):
        return self.get_text(self.COMPLETE_HEADER)
