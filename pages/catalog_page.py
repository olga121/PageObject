from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import random


class CatalogPage:

    def __init__(self, wd):
        self.wd = wd
        self.wait = WebDriverWait(wd, 10)

    def open(self):
        self.wd.find_element_by_link_text("catalog").click()

    def add_new_product_form(self):
        self.wd.find_elements_by_css_selector(("a.button"))[1].click()
        WebDriverWait(self.wd, 10).until(
            EC.presence_of_element_located((By.XPATH, "//img[contains(@title,'My Store')]")))

    def status_enabled(self):
        self.wd.find_element_by_xpath("//input[@type='radio' and @value='1']").click()

    @property
    def product_name_input(self):
        return self.wd.find_element_by_xpath("//input[@name='name[en]']")

    @property
    def product_code_input(self):
        return self.wd.find_element_by_xpath("//input[@name='code']")

    def select_random_category(self):
        return random.choice(self.wd.find_elements_by_css_selector("[data-name]")[1:2])

    def select_gender(self):
        random.choice(self.wd.find_elements_by_css_selector("[name='product_groups[]']")).click()

    @property
    def quantity_input(self):
        return self.wd.find_element_by_css_selector(("[name=quantity]"))

    @property
    def date_valid_from_input(self):
        return self.wd.find_element_by_xpath(("//input[@name='date_valid_from']"))

    @property
    def date_valid_to_input(self):
        return self.wd.find_element_by_xpath(("//input[@name='date_valid_to']"))

    def save_general_info(self):
        self.wd.find_element_by_css_selector("[name=save]").click()

    def information_tab(self):
        self.wd.find_element_by_xpath("//a[@href='#tab-information']").click()

    def open_catalog(self):
        self.wd.sele




