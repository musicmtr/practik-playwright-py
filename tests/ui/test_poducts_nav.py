from pages.products_page import ProductsPage

def test_open_services(page):

    products_page = ProductsPage(page)

    products_page.open()

    products_page.open_services()

    assert "/customers/products/services" in page.url
