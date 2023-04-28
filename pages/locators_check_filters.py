from selenium.webdriver.common.by import By


class CheckFiltersLocators:
    LOCATOR_GLUTEN_FREE = (By.XPATH, '//button[@aria-label="Безглютеновый"]')
    LOCATOR_HOLISTIK_FOOD = (By.XPATH, '//button[@aria-label="Холистик"]')
    LOCATOR_MEDIUM_CHECKBOX_BRANDS = (By.ID, 'arrFilter_86_4174463861-popup')
    LOCATOR_SHOW_MORE_BRANDS = (By.XPATH, '//button[@class="button button--light button--sm"][@aria-label="Еще 45"]')
    LOCATOR_MIN_PRICE = (By.ID, 'arrFilter_P5_MIN')
    LOCATOR_MAX_PRICE = (By.ID, 'arrFilter_P5_MAX')
    LOCATOR_ONLY_ONLINE = (By.XPATH, '//button[@aria-label="% только онлайн"]')
    LOCATOR_BUTTON_IS_AVAILABLE = (By.XPATH, '//div[@class="filter-rounded-tags__item filter-rounded-tags__item--active"][3]/button')
    LOCATOR_BUTTON_BENEFITS = (By.XPATH, '//button[@aria-label="Акции и скидки"]')
    LOCATOR_MAIN_MENU_CATS = (By.XPATH, '//div[@class="main-menu__item main-menu__item--1989"]/a[1]')
    LOCATOR_CHECKBOX_BENEFITS =  (By.ID, 'arrFilter_2094_3865458834')
    LOCATOR_CHECKBOX_ONLY_ONLAIN = (By.ID, 'arrFilter_2094_1958325001')
    LOCATOR_CHECKBOX_ARE_AVAILABLE = (By.ID, 'arrFilter_617_3233089245')
    LOCATOR_SEARCHING_RESULT = (By.XPATH,
                                '//div[@sticky-offset="offset"]'
                                '//div[@class="button button--default button--xl smart-filter__button smart-filter__button--info"][1]')
    LOCATOR_MIN_WEIGHT = (By.XPATH, '//div[@class="multiselect__tags"][1]')
    LOCATOR_MIN_WEIGHT_DIGIT = (By.XPATH, '//span[@class="multiselect__option multiselect__option--highlight"][1]')
    LOCATOR_MAX_WEIGHT_DIGIT = (By.XPATH,
                                '//*[@id="app"]/main/div/div[3]/div/div/div[1]/div[2]/div[2]/form/div[1]/div[2]/'
                                'div[10]/div[2]/div/div/div[2]/div/div/div[3]/ul/li[7]/span/span')
    LOCATOR_MAX_WEIGHT = (By.XPATH, '//div[@class="row g-2"]/div[2]/div/div')
    LOCATOR_DRY_FOOD = (By.XPATH,'//*[@id="bx_510680952_2638"]/a/div[2]')
    LOCATOR_PHONE_FIELD = (By.XPATH, '//*[@id="auth-phone"]')
    LOCATOR_SHOW_RESULTS = (By.XPATH,
                    '//a[@class="button button--primary button--xl smart-filter__button smart-filter__button--show"]')
    LOCATOR_FILTER_MIN_PRICE = (By.ID, 'arrFilter_P5_MIN')
    LOCATOR_FILTER_MAX_PRICE = (By.ID, 'arrFilter_P5_MAX')
    LOCATOR_TYPE_OF_FEED_BUTTON = (By.XPATH, '//div[@class="parameters-box"][1]/div[1]/div')
    LOCATOR_DRY_FEED_CHECKBOX = (By.ID, 'arrFilter_303_1763061754')
    LOCATOR_FILTER_SPEC_SERIES_BUTTON = (By.XPATH, '//div[@class="smart-filter__properties"]/div[3]/div[1]/div')
    LOCATOR_GLUTEN_FREE_CHECKBOX = (By.ID, 'arrFilter_313_591306731')
    LOCATOR_GRAIN_FREE_CHECKBOX = (By.ID, 'arrFilter_313_1413066621')
    LOCATOR_VET_DIET = (By.ID, 'arrFilter_313_591306731')
    LOCATOR_LOW_GRAIN = (By.ID, 'arrFilter_313_3442540231')
    LOCATOR_HOLISTIK_CHECKBOX = (By.ID, 'arrFilter_313_1140397582')
    LOCATOR_TYPE_OF_PACKING = (By.XPATH, '//div[@class="parameters-box"][6]')
    LOCATOR_TYPE_OF_PACKING_BOX = (By.ID, 'arrFilter_229_2729817228')
    LOCATOR_TYPE_OF_PACKING_BAG = (By.ID, 'arrFilter_229_1210337208')

