from  selenium.webdriver.common.by import By

class MainPageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, '#login_link')

class LoginPageLocators:
    LOGIN_FORM = (By.CSS_SELECTOR, '#login_form')
    REGISTER_FORM = (By.CSS_SELECTOR, '#register_form')

class ProductPageLocators:
    ADD_PRODUCT = (By.CSS_SELECTOR, '.btn.btn-lg.btn-primary.btn-add-to-basket')
    BASKET_PRICE = (By.CSS_SELECTOR, "div.alertinner > p > strong ")
    PRODUCT_NAME_PAGE = (By.CSS_SELECTOR, "div.row h1")
    PRODUCT_NAME_BASKET = (By.CSS_SELECTOR, "div.alertinner > strong")
    PRODUCT_PRICE = (By.CSS_SELECTOR, "h1 + .price_color")
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, "div.alertinner")