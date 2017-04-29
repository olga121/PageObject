from selenium import webdriver
from fixture.session import SessionHelper
#from fixture.group import GroupHelper
from pages.catalog_page import CatalogPage
class Application:

    def __init__(self, browser, base_url):
        if browser == "firefox":
            self.wd = webdriver.Firefox()
        elif browser == "chrome":
            self.wd = webdriver.Chrome()
        elif browser == "ie":
            self.wd = webdriver.Ie()
        else:
            raise ValueError("Unrecognized browser %s" % browser)
#        self.wd.implicitly_wait(5)
        self.session = SessionHelper(self)
#       self.group = GroupHelper(self)
        self.base_url=base_url
        self.catalog_page = CatalogPage(self.wd)

    def open_home_page(self):
        wd = self.wd
        wd.get(self.base_url)

    def destroy(self):
        self.wd.quit()

    def is_valid(self):
        try:
            self.wd.current_url
            return True
        except:
            return False

    def add_new_product(self, new_product):
        self.catalog_page.open()
        self.catalog_page.add_new_product_form()
        self.catalog_page.status_enabled()
        self.catalog_page.product_name_input.send_keys("name", new_product.name)
        self.catalog_page.product_code_input.send_keys("code", new_product.code)
        category = self.catalog_page.select_random_category()
        category.click()
        self.catalog_page.select_gender()
        self.catalog_page.quantity_input.send_keys("quantity", new_product.quantity)
        self.catalog_page.date_valid_from_input.send_keys("date_valid_from", new_product.date_valid_from)
        self.catalog_page.date_valid_to_input.send_keys("date_valid_to", new_product.date_valid_to)
        self.catalog_page.save_general_info()
    #   open catalog page where new product was saved
    #    number = category.get_attribute('value')
    #   self.catalog_page.find_element_be_css_selector('input[value=number]').click()



