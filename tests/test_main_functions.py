from pages.page_main_func import SearchHelper
import allure
from allure_commons.types import AttachmentType


@allure.feature('Header tests')
@allure.title('Card activation')
def test_check_card_activation(browser):
    zoobazar_main_page = SearchHelper(browser)
    zoobazar_main_page.go_to_site()
    zoobazar_main_page.check_activation_button()


@allure.feature('Choose category tests')
@allure.title('Choose category(Cats_page)')
def test_choose_caterogy(browser):
    zoobazar_main_page = SearchHelper(browser)
    zoobazar_main_page.go_to_site()
    zoobazar_main_page.choose_category_max_benefits()
    assert 'https://zoobazar.by/catalog/koshki/?sort=best_sale&order=desc' in browser.current_url
    zoobazar_main_page.choose_min_price()
    assert 'https://zoobazar.by/catalog/koshki/?sort=price&order=asc' in browser.current_url
    zoobazar_main_page.choose_max_price()
    assert 'https://zoobazar.by/catalog/koshki/?sort=price&order=desc' in browser.current_url
    zoobazar_main_page.choose_popular_category()
    assert 'https://zoobazar.by/catalog/koshki/?sort=popular&order=desc' in browser.current_url
    zoobazar_main_page.choose_most_popular_category()
    assert 'https://zoobazar.by/catalog/koshki/?sort=hit&order=desc' in browser.current_url
    zoobazar_main_page.choose_promotions_category()
    assert 'https://zoobazar.by/catalog/koshki/?sort=sale&order=desc' in browser.current_url


@allure.feature('Add to cart')
def test_add_to_cart(browser):
    zoobazar_main_page = SearchHelper(browser)
    zoobazar_main_page.go_to_site()
    zoobazar_main_page.add_goods_to_cart()


@allure.feature('Add to favorites')
def test_add_to_favorites(browser):
    zoobazar_main_page = SearchHelper(browser)
    browser.maximize_window()
    zoobazar_main_page.go_to_site()
    browser.execute_script("window.scrollTo(0, 650)")
    zoobazar_main_page.add_goods_to_favorites()
    with allure.step("Скриншот"):
        allure.attach(browser.get_screenshot_as_png(), name='Screenshot', attachment_type=AttachmentType.PNG)
