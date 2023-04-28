import allure
from pages.page_check_filters import SearchHelper
from allure_commons.types import AttachmentType


@allure.feature('Check filters (Cats page)')
@allure.title('Check_base filters')
def test_check_filters_cats(browser):
    zoobazar_main_page = SearchHelper(browser)
    with allure.step('Go to the website page'):
     zoobazar_main_page.go_to_site()
    zoobazar_main_page.check_main_menu_cats()
    browser.execute_script("window.scrollTo(0, 900)")
    with allure.step('Check filter cats'):
     zoobazar_main_page.check_filters_cats()
    with allure.step("Скриншот"):
        allure.attach(browser.get_screenshot_as_png(), name='Screenshot', attachment_type=AttachmentType.PNG)


@allure.feature('Check filters (Cats page)')
@allure.title('Check weight filter')
def test_check_filter_weight(browser):
    zoobazar_main_page = SearchHelper(browser)
    with allure.step('Go to the website page'):
     zoobazar_main_page.go_to_site()
    zoobazar_main_page.check_main_menu_cats()
    zoobazar_main_page.click_on_the_dry_food()
    browser.execute_script("window.scrollTo(0, 900)")
    with allure.step('Check filter weight'):
     zoobazar_main_page.check_filter_weight()
    with allure.step("Скриншот"):
        allure.attach(browser.get_screenshot_as_png(), name='Screenshot', attachment_type=AttachmentType.PNG)
    assert 'https://zoobazar.by/catalog/koshki/sukhie_korma/filter/weight-from-0.19-to-0.35/apply/'\
           in browser.current_url


@allure.feature('Check filters (Cats page)')
@allure.title('Check brands filter')
def test_check_filter_brands(browser):
    zoobazar_main_page = SearchHelper(browser)
    with allure.step('Go to the website page'):
     zoobazar_main_page.go_to_site()
    zoobazar_main_page.check_main_menu_cats()
    zoobazar_main_page.click_on_the_dry_food()
    with allure.step('CHeck filter brands'):
     zoobazar_main_page.check_filter_brands()
    with allure.step("Скриншот"):
        allure.attach(browser.get_screenshot_as_png(), name='Screenshot', attachment_type=AttachmentType.PNG)
    assert 'https://zoobazar.by/catalog/koshki/sukhie_korma/chicopee/'\
           in browser.current_url


@allure.feature('Check filters (Cats page)')
@allure.title('Check feed filter')
def test_check_filter_type_of_feed(browser):
    zoobazar_main_page = SearchHelper(browser)
    with allure.step('Go to the website page'):
     zoobazar_main_page.go_to_site()
    zoobazar_main_page.check_main_menu_cats()
    zoobazar_main_page.click_on_the_dry_food()
    with allure.step('Check type of feed'):
     zoobazar_main_page.check_type_of_feed()
    with allure.step("Скриншот"):
        allure.attach(browser.get_screenshot_as_png(), name='Screenshot', attachment_type=AttachmentType.PNG)
    assert 'https://zoobazar.by/catalog/koshki/sukhie_korma/filter/' \
           'vid_korma-is-1152f3fe-b468-11ea-a4c1-0050568f1acb/apply/' in browser.current_url


@allure.feature('Check filters (Cats page)')
@allure.title('Check special series filter')
def test_check_filter_special_series(browser):
    zoobazar_main_page = SearchHelper(browser)
    with allure.step('Go to the website page'):
     zoobazar_main_page.go_to_site()
    zoobazar_main_page.check_main_menu_cats()
    zoobazar_main_page.click_on_the_dry_food()
    browser.execute_script("window.scrollTo(0, 500)")
    with allure.step('Check filter special series'):
     zoobazar_main_page.check_filter_special_series()
    with allure.step("Скриншот"):
        allure.attach(browser.get_screenshot_as_png(), name='Screenshot', attachment_type=AttachmentType.PNG)


@allure.feature('Check filters (Cats page)')
@allure.title('Check packing filter')
def test_check_filter_packing(browser):
    zoobazar_main_page = SearchHelper(browser)
    with allure.step('Go to the website page'):
     zoobazar_main_page.go_to_site()
    zoobazar_main_page.check_main_menu_cats()
    zoobazar_main_page.click_on_the_dry_food()
    browser.execute_script("window.scrollTo(0, 650)")
    with allure.step('Check filter of packing'):
     zoobazar_main_page.check_filter_of_packing()
    with allure.step("Скриншот"):
        allure.attach(browser.get_screenshot_as_png(), name='Screenshot', attachment_type=AttachmentType.PNG)
    assert "https://zoobazar.by/catalog/koshki/sukhie_korma/filter/" \
           "tip_upakovki-is-9726308d-bf8c-11ea-a4c7-0050568f1acb-or-a010d7c3-f8ee-11ea-a4d7-0050568fefb1/apply/"\
           in browser.current_url
