from selenium.common.exceptions import NoAlertPresentException
from .base_page import BasePage
from .locators import ProductPageLocators
import math

class ProductPage(BasePage):
    def add_in_basket(self):
        product_link = self.browser.find_element(*ProductPageLocators.ADD_PRODUCT)
        product_link.click()

    def solve_quiz_and_get_code(self):
        alert = self.browser.switch_to.alert
        x = alert.text.split(" ")[2]
        answer = str(math.log(abs((12 * math.sin(float(x))))))
        alert.send_keys(answer)
        alert.accept()
        try:
            alert = self.browser.switch_to.alert
            alert_text = alert.text
            print(f"Your code: {alert_text}")
            alert.accept()
        except NoAlertPresentException:
            print("No second alert presented")

    def check_name_add_in_basket(self):
        self.should_be_basket_and_product_same_name()
        self.should_be_basket_and_product_same_price()

    def should_be_basket_and_product_same_name(self):
        # Проверка того, что товар добавлен в корзину. Название товара в сообщении должно совпадать с тем товаром,
        # который добавили
        product_name_page = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME_PAGE).text
        product_name_basket = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME_BASKET).text
        assert product_name_basket == product_name_page, \
            f"Product names in page and basket are not the same! {product_name_page} != {product_name_basket}"

    def should_be_basket_and_product_same_price(self):
        # Проверка стоимости в корзине. Стоимость в корзине должна совпадать с ценой товара
        product_price = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE).text[1:]
        basket_price = self.browser.find_element(*ProductPageLocators.BASKET_PRICE).text[1:]
        assert product_price == basket_price, \
            f"Product prices in page and basket are not the same! {product_price} != {basket_price}"

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Success message is presented, but should not be"

    def should_not_be_success_message(self):
        assert self.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Success message is presented, but should be"

