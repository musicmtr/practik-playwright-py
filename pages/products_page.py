from base_page import BasePage
from locators.products_locators import ProductsLocators

class ProductsPage(BasePage):

    def open_services(self):
        self.page.locator(ProductsLocators.SERVICES_LINK).click()
