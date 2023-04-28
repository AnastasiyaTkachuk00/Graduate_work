from locators.locators_footer import FooterLocators
from base_page import BasePage
import time


class SearchHelper(BasePage):
    def click_vacansies_button(self):
        time.sleep(3)
        self.click_element(FooterLocators.LOCATOR_VACANCIES_BUTTON)
        time.sleep(3)

    def click_about_us_button(self):
        time.sleep(3)
        self.click_element(FooterLocators.LOCATOR_ABOUT_US_BUTTON)
        time.sleep(3)

    def click_stories_button(self):
        time.sleep(3)
        self.click_element(FooterLocators.LOCATOR_OUR_STORIES_BUTTON)

    def click_pick_up_button2(self):
        time.sleep(3)
        self.click_element(FooterLocators.LOCATOR_PICKUP_POINTS_BUTTON3)

    def click_delivery_map_button(self):
        time.sleep(3)
        self.click_element(FooterLocators.LOCATOR_DELIVERY_MAP_BUTTON)

    def click_lessors_button(self):
        time.sleep(3)
        self.click_element(FooterLocators.LOCATOR_LESSORS_BUTTON)

    def click_news_button(self):
        time.sleep(3)
        self.click_element(FooterLocators.LOCATOR_NEWS_BUTTON)

    def click_zooguests_button(self):
        time.sleep(3)
        self.click_element(FooterLocators.LOCATOR_ZOOGUESTS_BUTTON)

    def click_contacts_button(self):
        time.sleep(3)
        self.click_element(FooterLocators.LOCATOR_CONTACTS_BUTTON)

    def click_loyalty_program_button(self):
        self.click_element(FooterLocators.LOCATOR_LOYALTY_PROGRAM)

    def click_discount_button(self):
        self.click_element(FooterLocators.LOCATOR_DISCOUNT_FROM_PARTNERS)

    def click_order_program(self):
        self.click_element(FooterLocators.LOCATOR_ORDER_PROCESS)

    def click_delivery_payment_button(self):
        self.click_element(FooterLocators.LOCATOR_DELIVERY_PAYMENT)

    def click_return_button(self):
        self.click_element(FooterLocators.LOCATOR_RETURN)

    def click_legal_info_button(self):
        self.click_element(FooterLocators.LOCATOR_LEGAL_INFO)

    def click_consumer_rights(self):
        self.click_element(FooterLocators.LOCATOR_CONSUMER_RIGHTS)

    def click_map_website(self):
        self.click_element(FooterLocators.LOCATOR_MAP_WEBSITE)

