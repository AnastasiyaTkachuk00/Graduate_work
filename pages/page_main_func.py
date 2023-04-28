from locators.locators_main_func import MainFunctionsLocators
from base_page import BasePage
import time


class SearchHelper(BasePage):

    def choose_category_max_benefits(self):
        self.click_element(MainFunctionsLocators.LOCATOR_MAIN_MENU_CATS)
        self.click_element(MainFunctionsLocators.LOCATOR_CATEGORY_BUTTON)
        self.click_element(MainFunctionsLocators.LOCATOR_CATEGORY_MAX_BENEFITS)

    def choose_min_price(self):
        self.click_element(MainFunctionsLocators.LOCATOR_CATEGORY_BUTTON)
        self.click_element(MainFunctionsLocators.LOCATOR_CATEGORY_MIN_PRICE)

    def choose_max_price(self):
        self.click_element(MainFunctionsLocators.LOCATOR_CATEGORY_BUTTON)
        self.click_element(MainFunctionsLocators.LOCATOR_CATEGORY_MAX_PRICE)

    def choose_popular_category(self):
        self.click_element(MainFunctionsLocators.LOCATOR_CATEGORY_BUTTON)
        self.click_element(MainFunctionsLocators.LOCATOR_CATEGORY_POPULAR)

    def choose_most_popular_category(self):
        self.click_element(MainFunctionsLocators.LOCATOR_CATEGORY_BUTTON)
        self.click_element(MainFunctionsLocators.LOCATOR_CATEGORY_MOST_POPULAR)

    def choose_promotions_category(self):
        self.click_element(MainFunctionsLocators.LOCATOR_CATEGORY_BUTTON)
        self.click_element(MainFunctionsLocators.LOCATOR_CATEGORY_PROMOTIONS)

    def add_goods_to_cart(self):
        self.click_element(MainFunctionsLocators.LOCATOR_MAIN_MENU_CATS)
        self.click_element(MainFunctionsLocators.LOCATOR_CART_ICON1)
        self.click_element(MainFunctionsLocators.LOCATOR_PICKUP_PIONTS_BUTTON2)
        self.click_element(MainFunctionsLocators.LOCATOR_CONFIRM_ADDRESS)
        time.sleep(3)
        self.click_element(MainFunctionsLocators.LOCATOR_CART_ICON2)
        time.sleep(3)
        self.click_element(MainFunctionsLocators.LOCATOR_CART_ICON3)
        self.click_element(MainFunctionsLocators.LOCATOR_CART_BUTTON)
        goods_in_cart = self.get_text_from_element(MainFunctionsLocators.LOCATOR_AMOUNT_OF_GOODS)
        assert '2 шт' in goods_in_cart

    def add_goods_to_favorites(self):
        self.click_element(MainFunctionsLocators.LOCATOR_MAIN_MENU_CATS)
        self.click_element(MainFunctionsLocators.LOCATOR_ADD_TO_FAVORITES1)
        self.click_element(MainFunctionsLocators.LOCATOR_ADD_TO_FAVORITES2)
        self.click_element(MainFunctionsLocators.LOCATOR_ADD_TO_FAVORITES3)
        time.sleep(4)
        small_icon_count = self.get_text_from_element(MainFunctionsLocators.LOCATOR_SMALL_ICON_COUNT)
        assert small_icon_count == '3'
        self.click_element(MainFunctionsLocators.LOCATOR_FAVORITES_BUTTON)
        items_count = self.get_text_from_element(MainFunctionsLocators.LOCATOR_ITEMS_COUNT)
        assert items_count == '3'
