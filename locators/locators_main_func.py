from selenium.webdriver.common.by import By


class MainFunctionsLocators:
    LOCATOR_SMALL_ICON_COUNT = (By.XPATH, '//a[@title="Избранное"]/span')
    LOCATOR_ITEMS_COUNT = (By.XPATH, '//span[@class="items-count"]')
    LOCATOR_CART_BUTTON = (By.CSS_SELECTOR, '[class="button button--clear cart-small"]')
    LOCATOR_CONFIRM_ADDRESS = (By.XPATH, '//*[@id="location-select"]/div/div[2]/div[3]/button')
    LOCATOR_CLOSE_ADV = (By.XPATH, '//*[@id="sale-popup"]/button')
    LOCATOR_AMOUNT_OF_GOODS = (By.XPATH, '//*[@id="app"]/main/div/div[3]/div/div[2]/div[2]/div[2]/div/div/div[2]/div[2]')
    LOCATOR_PICKUP_PIONTS_BUTTON2 = (By.XPATH, '//*[@id="location-select"]/div/div[2]/div/div[2]/button[2]')
    LOCATOR_MAIN_MENU_CATS = (By.XPATH, '//div[@class="main-menu__item main-menu__item--1989"]/a[1]')
    LOCATOR_ADD_TO_FAVORITES1 = (By.XPATH, '//*[@id="catalog-list--catalog"]/div/div[1]/div/a/button')
    LOCATOR_ADD_TO_FAVORITES2 = (By.XPATH, '//*[@id="catalog-list--catalog"]/div/div[2]/div/a/button')
    LOCATOR_ADD_TO_FAVORITES3 = (By.XPATH, '//*[@id="catalog-list--catalog"]/div/div[3]/div/a/button')
    LOCATOR_CATEGORY_BUTTON = (By.CLASS_NAME, 'multiselect__tags')
    LOCATOR_CATEGORY_POPULAR = (By.XPATH, '//li[@class="multiselect__element"][1]')
    LOCATOR_CATEGORY_MAX_BENEFITS = (By.XPATH, '//li[@class="multiselect__element"][2]')
    LOCATOR_CATEGORY_MIN_PRICE = (By.XPATH, '//li[@class="multiselect__element"][3]')
    LOCATOR_CATEGORY_MAX_PRICE = (By.XPATH, '//li[@class="multiselect__element"][4]')
    LOCATOR_CATEGORY_PROMOTIONS = (By.XPATH, '//li[@class="multiselect__element"][5]')
    LOCATOR_CATEGORY_MOST_POPULAR = (By.XPATH, '//li[@class="multiselect__element"][6]')
    LOCATOR_CART_ICON1 = (By.XPATH, '//div[@class="col col-12 col-md-6 col-lg-4 col-xl-3"][1]/div/div/div/div/button')
    LOCATOR_CART_ICON2 = (By.XPATH, '//div[@class="col col-12 col-md-6 col-lg-4 col-xl-3"][2]/div/div/div/div/button')
    LOCATOR_CART_ICON3 = (By.XPATH, '//div[@class="col col-12 col-md-6 col-lg-4 col-xl-3"][3]/div/div/div/div/button')
    LOCATOR_FIRST_CHECKBOX_BRANDS = (By.ID, 'arrFilter_86_3222927397')
    LOCATOR_FAVORITES_BUTTON = (By.XPATH, '//a[@title="Избранное"]')
    LOCATOR_MEDIUM_CHECKBOX_BRANDS = (By.ID, 'arrFilter_86_4174463861-popup')
    LOCATOR_SHOW_MORE_BRANDS = (By.XPATH, '//button[@class="button button--light button--sm"][@aria-label="Еще 45"]')
