from locators.locators_header import HeaderLocators
from base_page import BasePage
import time


class SearchHelper(BasePage):
    def enter_word(self, word):
        search_field = self.find_element(HeaderLocators.LOCATOR_SEARCH_FRAME_FIELD)
        search_field.send_keys(word)
        time.sleep(5)
        return search_field

    def check_activation_button(self):
        time.sleep(3)
        self.click_element(HeaderLocators.LOCATOR_CARD_ACTIVATION)
        time.sleep(4)
        title_activation = self.get_text_from_element(HeaderLocators.TITLE_CARD_ACTIVATION)
        assert title_activation == "Активация карты"

    def click_cart_button(self):
        self.find_element(HeaderLocators.LOCATOR_CART_BUTTON)
        time.sleep(3)
        self.click_element(HeaderLocators.LOCATOR_CART_BUTTON)
        time.sleep(5)

    def click_search_button(self):
        time.sleep(3)
        self.click_element(HeaderLocators.LOCATOR_SEARCH_FIELD)
        time.sleep(5)

    def click_pick_up_button(self):
        time.sleep(3)
        self.click_element(HeaderLocators.LOCATOR_PICKUP_PIONTS_BUTTON)
        time.sleep(5)

    def click_payment_button(self):
        time.sleep(3)
        self.click_element(HeaderLocators.LOCATOR_DELIVERY_BUTTON)
        time.sleep(5)

    def click_delivery_button(self):
        self.find_element(HeaderLocators.LOCATOR_DELIVERY_BUTTON)
        time.sleep(3)
        self.click_element(HeaderLocators.LOCATOR_DELIVERY_BUTTON)
        time.sleep(3)

    def click_favotire_button(self):
        self.find_element(HeaderLocators.LOCATOR_FAVORITES_BUTTON)
        time.sleep(3)
        self.click_element(HeaderLocators.LOCATOR_FAVORITES_BUTTON)

    def click_login_locator(self):
        time.sleep(3)
        self.click_element(HeaderLocators.LOCATOR_LOGIN)
        time.sleep(3)
        logg = self.get_text_from_element(HeaderLocators.LOCATOG_LOGGIN)
        time.sleep(3)
        assert logg == "Авторизация"
        
