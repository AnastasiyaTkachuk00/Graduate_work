from selenium.webdriver.common.by import By


class HeaderLocators:
    LOCATOR_CARD_ACTIVATION = (By.XPATH, '//div[@class="header-top-links"]/a[@title="Активировать карту"]')
    TITLE_CARD_ACTIVATION = (By.ID, 'pagetitle')
    LOCATOR_SEARCH_FIELD = (By.CLASS_NAME, "header-search__content")
    LOCATOR_PICKUP_PIONTS_BUTTON = (By.XPATH, '//*[@id="header"]/div[1]/div/div/div[2]/div[1]/a[4]')
    LOCATOR_DELIVERY_BUTTON = (By.XPATH, '//a[@title="Доставка"]')
    LOCATOR_FAVORITES_BUTTON = (By.XPATH, '//a[@title="Избранное"]')
    title = (By.CSS_SELECTOR, 'head > title')
    LOCATOR_SEARCH_BUTTON = (By.CLASS_NAME, "header-search__icon")
    LOCATOR_SEARCH_FRAME_FIELD = (By.XPATH, '//*[@id="multisearch-search"]/div/form/div/input')
    LOCATOR_CART_BUTTON = (By.CSS_SELECTOR, '[class="button button--clear cart-small"]')
    LOCATOR_LOGIN = (By.XPATH, '//div[@class="d-none d-lg-flex header-personal__wrapper header-main__action"]/button')
    LOCATOR_MAIN_PAGE = (By.XPATH, "/html/head/title/text()")
    LOCATOR_AUTH_TITLE = (By.CSS_SELECTOR, '#auth > div > div.popup__heading > div')
    LOCATOR_MAIN_MENU_CATS = (By.XPATH, '//div[@class="main-menu__item main-menu__item--1989"]/a[1]')
    LOCATOG_LOGGIN = (By.XPATH, '//*[@id="auth"]/div/div[1]')
    
