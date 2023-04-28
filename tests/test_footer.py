import allure
from pages.page_footers import SearchHelper
from allure_commons.types import AttachmentType


@allure.feature('Footer tests')
@allure.story('Footer menu: Company')
@allure.title('Check vacancies button')
def test_vacancies_button(browser):
    zoobazar_main_page = SearchHelper(browser)
    with allure.step('Open website page'):
        zoobazar_main_page.go_to_site()
    browser.execute_script("window.scrollTo(0, 3000)")
    with allure.step('Click vacansies button'):
        zoobazar_main_page.click_vacansies_button()
    with allure.step("Скриншот"):
        allure.attach(browser.get_screenshot_as_png(), name='Screenshot', attachment_type=AttachmentType.PNG)
    assert 'https://zoobazar.by/vacancies/' in browser.current_url


@allure.feature('Footer tests')
@allure.story('Footer menu: Company')
@allure.title('Check about us button')
def test_about_us_button(browser):
    zoobazar_main_page = SearchHelper(browser)
    with allure.step('Open website page'):
        zoobazar_main_page.go_to_site()
    with allure.step('Click about_us_button'):
        zoobazar_main_page.click_about_us_button()
    with allure.step("Скриншот"):
        allure.attach(browser.get_screenshot_as_png(), name='Screenshot', attachment_type=AttachmentType.PNG)
    assert 'https://zoobazar.by/about/' in browser.current_url


@allure.feature('Footer tests')
@allure.story('Footer menu: Company')
@allure.title('Check our stories button')
def test_our_stories_button(browser):
    zoobazar_main_page = SearchHelper(browser)
    with allure.step('Go to website page'):
        zoobazar_main_page.go_to_site()
    browser.execute_script("window.scrollTo(0, 3000)")
    with allure.step('Click_our_stories_button'):
        zoobazar_main_page.click_stories_button()
    with allure.step("Скриншот"):
        allure.attach(browser.get_screenshot_as_png(), name='Screenshot', attachment_type=AttachmentType.PNG)
    assert 'https://zoobazar.by/shops/' in browser.current_url


@allure.feature('Footer tests')
@allure.story('Footer menu: Company')
@allure.title('Check pick up button')
def test_pick_up_button(browser):
    zoobazar_main_page = SearchHelper(browser)
    with allure.step('Go to website page'):
        zoobazar_main_page.go_to_site()
    browser.execute_script("window.scrollTo(0, 3000)")
    with allure.step('Click pick up button'):
        zoobazar_main_page.click_pick_up_button2()
    with allure.step("Скриншот"):
        allure.attach(browser.get_screenshot_as_png(), name='Screenshot', attachment_type=AttachmentType.PNG)
    assert 'https://zoobazar.by/pickup/' in browser.current_url


@allure.feature('Footer tests')
@allure.story('Footer menu: Company')
@allure.title('Check delivery map button')
def test_delivery_map_button(browser):
    zoobazar_main_page = SearchHelper(browser)
    with allure.step('Go to website page'):
        zoobazar_main_page.go_to_site()
    browser.execute_script("window.scrollTo(0, 3000)")
    with allure.step('Click delivery button'):
        zoobazar_main_page.click_delivery_map_button()
    with allure.step("Скриншот"):
        allure.attach(browser.get_screenshot_as_png(), name='Screenshot', attachment_type=AttachmentType.PNG)
    assert 'https://zoobazar.by/delivery-map/' in browser.current_url


@allure.feature('Footer tests')
@allure.story('Footer menu: Company')
@allure.title('Check lessors button')
def test_lessors_button(browser):
    zoobazar_main_page = SearchHelper(browser)
    with allure.step('Go to website page'):
        zoobazar_main_page.go_to_site()
    with allure.step('Click lessors button'):
        zoobazar_main_page.click_lessors_button()
    with allure.step("Скриншот"):
        allure.attach(browser.get_screenshot_as_png(), name='Screenshot', attachment_type=AttachmentType.PNG)
    assert 'https://zoobazar.by/lessors/' in browser.current_url


@allure.feature('Footer tests')
@allure.story('Footer menu: Company')
@allure.title('Check news button')
def test_news_button(browser):
    zoobazar_main_page = SearchHelper(browser)
    with allure.step('Go to website page'):
        zoobazar_main_page.go_to_site()
    with allure.step('Click news button'):
        zoobazar_main_page.click_news_button()
    with allure.step("Скриншот"):
        allure.attach(browser.get_screenshot_as_png(), name='Screenshot', attachment_type=AttachmentType.PNG)
    assert 'https://zoobazar.by/news/' in browser.current_url


@allure.feature('Footer tests')
@allure.story('Footer menu: Company')
@allure.title('Check Zoobazar guests button')
def test_zooguests_button(browser):
    zoobazar_main_page = SearchHelper(browser)
    with allure.step('Go to website page'):
        zoobazar_main_page.go_to_site()
    with allure.step('Click zooguests button'):
        zoobazar_main_page.click_zooguests_button()
    with allure.step("Скриншот"):
        allure.attach(browser.get_screenshot_as_png(), name='Screenshot', attachment_type=AttachmentType.PNG)
    assert 'https://zoobazar.by/visit/' in browser.current_url


@allure.feature('Footer tests')
@allure.story('Footer menu: Company')
@allure.title('Check Zoobazar contacts button')
def test_contacts_button(browser):
    zoobazar_main_page = SearchHelper(browser)
    with allure.step('Go to website button'):
        zoobazar_main_page.go_to_site()
    with allure.step('Click contacts button'):
        zoobazar_main_page.click_contacts_button()
    with allure.step("Скриншот"):
        allure.attach(browser.get_screenshot_as_png(), name='Screenshot', attachment_type=AttachmentType.PNG)
    assert 'https://zoobazar.by/contacts/' in browser.current_url


@allure.feature('Footer tests')
@allure.story('Footer menu: Buyers')
@allure.title('Check loyalty program button')
def test_loyalty_program(browser):
    zoobazar_main_page = SearchHelper(browser)
    with allure.step('Go to website button'):
        zoobazar_main_page.go_to_site()
    with allure.step('Click loyalty program button'):
        zoobazar_main_page.click_loyalty_program_button()
    with allure.step("Скриншот"):
        allure.attach(browser.get_screenshot_as_png(), name='Screenshot', attachment_type=AttachmentType.PNG)
    assert 'https://zoobazar.by/programma-loyalnosti/' in browser.current_url


@allure.feature('Footer tests')
@allure.story('Footer menu: Buyers')
@allure.title('Check discount button')
def test_discount_button(browser):
    zoobazar_main_page = SearchHelper(browser)
    with allure.step('Go to website button'):
        zoobazar_main_page.go_to_site()
    with allure.step('Click discount button'):
        zoobazar_main_page.click_discount_button()
    with allure.step("Скриншот"):
        allure.attach(browser.get_screenshot_as_png(), name='Screenshot', attachment_type=AttachmentType.PNG)
    assert 'https://zoobazar.by/partners/' in browser.current_url


@allure.feature('Footer tests')
@allure.story('Footer menu: Buyers')
@allure.title('Check order process button')
def test_discount_button(browser):
    zoobazar_main_page = SearchHelper(browser)
    with allure.step('Go to website button'):
        zoobazar_main_page.go_to_site()
    with allure.step('Click order process button'):
        zoobazar_main_page.click_order_program()
    with allure.step("Скриншот"):
        allure.attach(browser.get_screenshot_as_png(), name='Screenshot', attachment_type=AttachmentType.PNG)
    assert 'https://zoobazar.by/order-process/' in browser.current_url


@allure.feature('Footer tests')
@allure.story('Footer menu: Buyers')
@allure.title('Check delivery payment button')
def test_discount_button(browser):
    zoobazar_main_page = SearchHelper(browser)
    with allure.step('Go to website button'):
        zoobazar_main_page.go_to_site()
    with allure.step('Click delivery payment button'):
        zoobazar_main_page.click_delivery_payment_button()
    with allure.step("Скриншот"):
        allure.attach(browser.get_screenshot_as_png(), name='Screenshot', attachment_type=AttachmentType.PNG)
    assert 'https://zoobazar.by/delivery-and-payment/' in browser.current_url


@allure.feature('Footer tests')
@allure.story('Footer menu: Buyers')
@allure.title('Check return button')
def test_discount_button(browser):
    zoobazar_main_page = SearchHelper(browser)
    with allure.step('Go to website button'):
        zoobazar_main_page.go_to_site()
    with allure.step('Click return button'):
        zoobazar_main_page.click_return_button()
    with allure.step("Скриншот"):
        allure.attach(browser.get_screenshot_as_png(), name='Screenshot', attachment_type=AttachmentType.PNG)
    assert 'https://zoobazar.by/return-and-exchange/' in browser.current_url


@allure.feature('Footer tests')
@allure.story('Footer menu: Buyers')
@allure.title('Check legal info button')
def test_discount_button(browser):
    zoobazar_main_page = SearchHelper(browser)
    with allure.step('Go to website button'):
        zoobazar_main_page.go_to_site()
    with allure.step('Click legal info button'):
        zoobazar_main_page.click_legal_info_button()
    with allure.step("Скриншот"):
        allure.attach(browser.get_screenshot_as_png(), name='Screenshot', attachment_type=AttachmentType.PNG)
    assert 'https://zoobazar.by/legal-information/' in browser.current_url


@allure.feature('Footer tests')
@allure.story('Footer menu: Buyers')
@allure.title('Check consumer rights button')
def test_discount_button(browser):
    zoobazar_main_page = SearchHelper(browser)
    with allure.step('Go to website button'):
        zoobazar_main_page.go_to_site()
    with allure.step('Click consumer rights button'):
        zoobazar_main_page.click_consumer_rights()
    with allure.step("Скриншот"):
        allure.attach(browser.get_screenshot_as_png(), name='Screenshot', attachment_type=AttachmentType.PNG)
    assert 'https://zoobazar.by/consumer-rights/' in browser.current_url


@allure.feature('Footer tests')
@allure.story('Footer menu: Buyers')
@allure.title('Check map website button')
def test_discount_button(browser):
    zoobazar_main_page = SearchHelper(browser)
    with allure.step('Go to website button'):
        zoobazar_main_page.go_to_site()
    with allure.step('Click map website button'):
        zoobazar_main_page.click_map_website()
    with allure.step("Скриншот"):
        allure.attach(browser.get_screenshot_as_png(), name='Screenshot', attachment_type=AttachmentType.PNG)
    assert 'https://zoobazar.by/sitemap/' in browser.current_url
