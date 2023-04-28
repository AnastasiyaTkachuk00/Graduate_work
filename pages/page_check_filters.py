from pages.page_headers import HeaderLocators
from locators.locators_check_filters import CheckFiltersLocators
from base_page import BasePage
import time


class SearchHelper(BasePage):
    def enter_word(self, word):
        search_field = self.find_element(HeaderLocators.LOCATOR_SEARCH_FRAME_FIELD)
        search_field.send_keys(word)
        time.sleep(5)
        return search_field

    def check_main_menu_cats(self):
        self.click_element(CheckFiltersLocators.LOCATOR_MAIN_MENU_CATS)

    def check_filters_cats(self):
        self.click_element(CheckFiltersLocators.LOCATOR_CHECKBOX_BENEFITS)
        self.click_element(CheckFiltersLocators.LOCATOR_CHECKBOX_ARE_AVAILABLE)
        self.click_element(CheckFiltersLocators.LOCATOR_CHECKBOX_ONLY_ONLAIN)
        self.click_element(CheckFiltersLocators.LOCATOR_SEARCHING_RESULT)
        time.sleep(6)
        button_benefits = self.get_text_from_element(CheckFiltersLocators.LOCATOR_BUTTON_BENEFITS)
        button_only_online = self.get_text_from_element(CheckFiltersLocators.LOCATOR_ONLY_ONLINE)
        button_is_available = self.get_text_from_element(CheckFiltersLocators.LOCATOR_BUTTON_IS_AVAILABLE)
        assert button_benefits == "Акции и скидки"
        assert button_only_online == "% только онлайн"
        assert button_is_available == "Есть в наличии"

    def click_on_the_dry_food(self):
        time.sleep(4)
        self.click_element(CheckFiltersLocators.LOCATOR_DRY_FOOD)

    def check_filter_weight(self):
        self.click_element(CheckFiltersLocators.LOCATOR_MIN_WEIGHT)
        self.click_element(CheckFiltersLocators.LOCATOR_MIN_WEIGHT_DIGIT)
        self.click_element(CheckFiltersLocators.LOCATOR_MAX_WEIGHT)
        time.sleep(3)
        self.click_element(CheckFiltersLocators.LOCATOR_MAX_WEIGHT_DIGIT)
        time.sleep(4)
        self.click_element(CheckFiltersLocators.LOCATOR_SHOW_RESULTS)
        time.sleep(3)

    def check_filter_brands(self):
        self.click_element(CheckFiltersLocators.LOCATOR_SHOW_MORE_BRANDS)
        self.click_element(CheckFiltersLocators.LOCATOR_MEDIUM_CHECKBOX_BRANDS)
        time.sleep(3)
        self.click_element(CheckFiltersLocators.LOCATOR_SHOW_RESULTS)
        time.sleep(4)

    def check_type_of_feed(self):
        time.sleep(3)
        self.click_element(CheckFiltersLocators.LOCATOR_TYPE_OF_FEED_BUTTON)
        self.click_element(CheckFiltersLocators.LOCATOR_DRY_FEED_CHECKBOX)
        self.click_element(CheckFiltersLocators.LOCATOR_SHOW_RESULTS)

    def check_filter_special_series(self):
        self.click_element(CheckFiltersLocators.LOCATOR_FILTER_SPEC_SERIES_BUTTON)
        self.click_element(CheckFiltersLocators.LOCATOR_GLUTEN_FREE_CHECKBOX)
        time.sleep(2)
        self.click_element(CheckFiltersLocators.LOCATOR_HOLISTIK_CHECKBOX)
        time.sleep(2)
        self.click_element(CheckFiltersLocators.LOCATOR_SHOW_RESULTS)
        gluten_free = self.get_text_from_element(CheckFiltersLocators.LOCATOR_GLUTEN_FREE)
        holistik = self.get_text_from_element(CheckFiltersLocators.LOCATOR_HOLISTIK_FOOD)
        assert "Безглютеновый" == gluten_free
        assert 'Холистик' == holistik

    def check_filter_of_packing(self):
        self.click_element(CheckFiltersLocators.LOCATOR_TYPE_OF_PACKING)
        time.sleep(3)
        self.click_element(CheckFiltersLocators.LOCATOR_TYPE_OF_PACKING_BOX)
        time.sleep(3)
        self.click_element(CheckFiltersLocators.LOCATOR_TYPE_OF_PACKING_BAG)
        time.sleep(3)
        self.click_element(CheckFiltersLocators.LOCATOR_SHOW_RESULTS)
