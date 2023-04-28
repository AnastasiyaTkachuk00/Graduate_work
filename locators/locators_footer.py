from selenium.webdriver.common.by import By


class FooterLocators:
    LOCATOR_VACANCIES_BUTTON = (By.XPATH, "//li[@class='footer-menu__item']/a[@title='Вакансии']")
    LOCATOR_ABOUT_US_BUTTON = (By.XPATH, "//li[@class='footer-menu__item']/a[@title='О нас']")
    LOCATOR_OUR_STORIES_BUTTON = (By.XPATH, "//li[@class='footer-menu__item']/a[@title='Наши магазины']")
    LOCATOR_PICKUP_POINTS_BUTTON3 = (By.XPATH, "//li[@class='footer-menu__item']/a[@title='Пункты самовывоза']")
    LOCATOR_DELIVERY_MAP_BUTTON = (By.XPATH, "//li[@class='footer-menu__item']/a[@title='Зоны доставки']")
    LOCATOR_LESSORS_BUTTON = (By.XPATH, "//li[@class='footer-menu__item']/a[@title='Аренда помещений']")
    LOCATOR_NEWS_BUTTON = (By.XPATH, "//li[@class='footer-menu__item']/a[@title='Публикации']")
    LOCATOR_ZOOGUESTS_BUTTON = (By.XPATH, "//li[@class='footer-menu__item']/a[@title='Zoobazar гости']")
    LOCATOR_CONTACTS_BUTTON = (By.XPATH, "//li[@class='footer-menu__item']/a[@title='Контакты и реквизиты']")
    LOCATOR_LOYALTY_PROGRAM = (By.XPATH, '//a[@href="/programma-loyalnosti/"][@class="footer-menu__link"]')
    LOCATOR_DISCOUNT_FROM_PARTNERS = (By.XPATH, '//a[@href="/partners/"][@class="footer-menu__link footer-menu__link--selected"]')
    LOCATOR_ORDER_PROCESS = (By.XPATH, '//a[@href="/order-process/"]')
    LOCATOR_DELIVERY_PAYMENT = (By.XPATH, '//a[@href="/delivery-and-payment/"]')
    LOCATOR_RETURN = (By.XPATH, '//a[@href="/return-and-exchange/"]')
    LOCATOR_LEGAL_INFO = (By.XPATH, '//a[@href="/legal-information/"]')
    LOCATOR_CONSUMER_RIGHTS = (By.XPATH, '//a[@href="/consumer-rights/"]')
    LOCATOR_MAP_WEBSITE = (By.XPATH, '//a[@href="/sitemap/"]')
