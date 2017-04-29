
from selenium.webdriver.common.by import By


def test_add_new_product(app, json_products):
    product = json_products
    app.add_new_product(product)
    assert(app.find_element(By.LINK_TEXT, product.name))



