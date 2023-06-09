from browser import BasePage, ImagePage
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


class Search(BasePage):

    """ Yandex main page locators -->"""

    LOCATOR_YANDEX_SEARCH_FIELD = (By.ID, "text")
    LOCATOR_YANDEX_SEARCH_BUTTON = (By.XPATH, "//*/button[@type='submit']")
    LOCATOR_YANDEX_SUGGEST = (By.XPATH, "//*[@role='listbox']")
    LOCATOR_YANDEX_MENU = (By.CLASS_NAME, "services-suggest__list-item-more")
    LOCATOR_YANDEX_IMAGE_BUTTON = (By.XPATH, "//*/div[@data-id='images']/parent::span")
    LOCATOR_YANDEX_RESULTS_FIRST = (By.XPATH, "//*[@id='search-result']/li/div/div/a")[0]
    LOCATOR_YANDEX_RESULTS_BLOCK = (By.ID, "search-result")

    """ recurring function -->"""

    def general_search_field(self, locator):
        try:
            search_field = self.find_element(locator)
        except:
            search_field = None
        return search_field

    """ action functions -->"""

    def get_current_url(self):
        return self.get_url()

    def search_field(self):
        return self.general_search_field(self.LOCATOR_YANDEX_SEARCH_FIELD)

    def suggest_field(self):
        return self.general_search_field(self.LOCATOR_YANDEX_SUGGEST)

    def enter_word(self, word):
        search_field = self.search_field()
        search_field.clear()
        search_field.send_keys(word)
        return search_field

    def press_enter(self):
        return self.find_element(self.LOCATOR_YANDEX_SEARCH_FIELD).send_keys(Keys.ENTER)

    def result_block(self):
        return self.general_search_field(self.LOCATOR_YANDEX_RESULTS_BLOCK)

    def first_result(self):
        try:
            first_result = self.find_element(self.LOCATOR_YANDEX_RESULTS_FIRST).getAttribute("href")
        except:
            first_result = None
        return str(first_result)

    def click_to_search_field(self):
        search_field = self.search_field()
        search_field.click()

    def menu_find(self):
        return self.general_search_field(self.LOCATOR_YANDEX_MENU)

    def menu_is_visible(self):
        menu = self.menu_find()
        return self.check_if_dlisplayed(menu)

    def click_to_menu_field(self):
        menu_field = self.menu_find()
        menu_field.click()

    def pictures_button(self):
        return self.general_search_field(self.LOCATOR_YANDEX_IMAGE_BUTTON)

    def go_to_pictures(self):
        pictures_button = self.pictures_button()
        pictures_button.click()
        return pictures_button

    def get_tab_id(self):
        return self.get_window_handles()

    def switch_to_pictures_tab(self):
        return self.switch_to_new_tab()

class Images(ImagePage):

    """ Yandex Image page locators -->"""

    LOCATOR_YANDEX_IMAGE_FIRST = (By.CLASS_NAME, "PopularRequestList-Item_pos_0")
    LOCATOR_YANDEX_IMAGE_SEARCH = (By.NAME, "text")
    LOCATOR_YANDEX_IMAGE_FIRST_PIC = (By.XPATH, "//*[@role = 'listitem']/div")
    LOCATOR_YANDEX_NEXT_IMAGE = (By.CSS_SELECTOR, "div.MediaViewer-ButtonNext")
    LOCATOR_YANDEX_PREV_IMAGE = (By.CSS_SELECTOR, "div.MediaViewer-ButtonPrev")
    LOCATOR_YANDEX_IMAGE_SCR = (By.CSS_SELECTOR, "img.MMImage-Origin")

    """ recurring function -->"""

    def general_search_field(self, locator):
        try:
            search_field = self.find_element(locator)
        except:
            search_field = None
        return search_field


    """ action functions -->"""

    def get_current_url(self):
        return self.get_url()

    def first_image_block(self):
        return self.general_search_field(self.LOCATOR_YANDEX_IMAGE_FIRST)

    def first_result(self):
        try:
            first_result = self.first_image_block().get_attribute("data-grid-text")
        except:
            first_result = None
        return str(first_result)

    def go_to_first_images_block(self):
        first_image_block = self.first_image_block()
        return first_image_block.click()

    def get_value_from_search(self):
        try:
            value = self.find_element(self.LOCATOR_YANDEX_IMAGE_SEARCH).get_attribute('value')
        except:
            value = None
        return value

    def first_picture(self):
        return self.general_search_field(self.LOCATOR_YANDEX_IMAGE_FIRST_PIC)

    def go_to_first_picture(self):
        first_picture = self.first_picture()
        return first_picture.click()

    def next_image(self):
        return self.general_search_field(self.LOCATOR_YANDEX_NEXT_IMAGE)

    def go_to_next_picture(self):
        next_picture = self.next_image()
        return next_picture.click()

    def prev_image(self):
        return self.general_search_field(self.LOCATOR_YANDEX_PREV_IMAGE)

    def go_to_prev_picture(self):
        prev_image = self.prev_image()
        return prev_image.click()

    def get_src_of_pictures(self):
        try:
            value = self.find_element(self.LOCATOR_YANDEX_IMAGE_SCR).get_attribute('src')
        except:
            value = None
        return value
