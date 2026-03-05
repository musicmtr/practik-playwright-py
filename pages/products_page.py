from pages.base_page import BasePage
from locators.products_locators import ProductsLocators

class ProductsPage(BasePage):

    URL = "https://{region}.beeline.ru/customers/products/"

    def open(self, region="moskva"):
        url = self.URL.format(region=region)
        self.page.goto(url)

    def open_services(self):
        # self.click(ProductsLocators.SERVICES_LINK)
        self.page.get_by_role("link", name=ProductsLocators.SERVICES_LINK, exact=True).click()

