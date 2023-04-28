import allure
from pages.page_headers import SearchHelper
from allure_commons.types import AttachmentType


@allure.feature('Header tests')
@allure.title('Card activation')
def test_check_card_activation(browser):
    zoobazar_main_page = SearchHelper(browser)
    with allure.step('Open website page'):
        zoobazar_main_page.go_to_site()
    with allure.step('Check activation button'):
        zoobazar_main_page.check_activation_button()
    with allure.step("Скриншот"):
        allure.attach(browser.get_screenshot_as_png(), name='Screenshot', attachment_type=AttachmentType.PNG)
    assert 'https://zoobazar.by/activation/' in browser.current_url


@allure.feature('Header tests')
@allure.title('Check cart button')
def test_check_cart_button(browser):
    zoobazar_main_page = SearchHelper(browser)
    with allure.step('Open website page'):
        zoobazar_main_page.go_to_site()
    with allure.step('Click cart button'):
        zoobazar_main_page.click_cart_button()
    with allure.step("Скриншот"):
        allure.attach(browser.get_screenshot_as_png(), name='Screenshot', attachment_type=AttachmentType.PNG)
    assert 'Корзина' in browser.title


@allure.feature('Header tests')
@allure.title('Check search button')
def test_zoobazar_search(browser):
    zoobazar_main_page = SearchHelper(browser)
    with allure.step('Open website page'):
        zoobazar_main_page.go_to_site()
    with allure.step('Click search button'):
        zoobazar_main_page.click_search_button()
    with allure.step("Скриншот"):
        allure.attach(browser.get_screenshot_as_png(), name='Screenshot', attachment_type=AttachmentType.PNG)
    zoobazar_main_page.enter_word('Корм')


@allure.feature('Header tests')
@allure.title('Check pick up button')
def test_check_pick_up_button(browser):
    zoobazar_main_page = SearchHelper(browser)
    browser.maximize_window()
    with allure.step('Open website page'):
        zoobazar_main_page.go_to_site()
    with allure.step('Click pick up button'):
        zoobazar_main_page.click_pick_up_button()
    with allure.step("Скриншот"):
        allure.attach(browser.get_screenshot_as_png(), name='Screenshot', attachment_type=AttachmentType.PNG)
    assert 'Пункты самовывоза | Zoobazar' in browser.title


@allure.feature('Header tests')
@allure.title('Check payment button')
def test_check_payment_button(browser):
    zoobazar_main_page = SearchHelper(browser)
    with allure.step('Open website page'):
        zoobazar_main_page.go_to_site()
    with allure.step('Click payment button'):
        zoobazar_main_page.click_payment_button()
    with allure.step("Скриншот"):
        allure.attach(browser.get_screenshot_as_png(), name='Screenshot', attachment_type=AttachmentType.PNG)
    assert 'Доставка и оплата' in browser.title


@allure.feature('Header tests')
@allure.title('Check delivery button')
def test_check_delivery_button(browser):
    zoobazar_main_page = SearchHelper(browser)
    with allure.step('Open website page'):
        zoobazar_main_page.go_to_site()
    with allure.step('Click delivery button'):
        zoobazar_main_page.click_delivery_button()
    with allure.step("Скриншот"):
        allure.attach(browser.get_screenshot_as_png(), name='Screenshot', attachment_type=AttachmentType.PNG)
    assert 'Доставка и оплата' in browser.title


@allure.feature('Header tests')
@allure.title('Check favorites button')
def test_check_favorites_button(browser):
    zoobazar_main_page = SearchHelper(browser)
    with allure.step('Open website page'):
        zoobazar_main_page.go_to_site()
    with allure.step('Click favorite button'):
        zoobazar_main_page.click_favotire_button()
    with allure.step("Скриншот"):
        allure.attach(browser.get_screenshot_as_png(), name='Screenshot', attachment_type=AttachmentType.PNG)
    assert 'https://zoobazar.by/personal/favorites/' in browser.current_url


@allure.feature('Header tests')
@allure.title('Check login button')
def test_check_login_button(browser):
    zoobazar_main_page = SearchHelper(browser)
    with allure.step('Open website page'):
        zoobazar_main_page.go_to_site()
    with allure.step('Click login locator'):
        zoobazar_main_page.click_login_locator()
    with allure.step("Скриншот"):
        allure.attach(browser.get_screenshot_as_png(), name='Screenshot', attachment_type=AttachmentType.PNG)
