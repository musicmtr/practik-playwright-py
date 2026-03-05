import pytest

from pages.products_page import ProductsPage
from pages.services_page import ServicePage
from test_data.services_data import get_dop_services


@pytest.mark.parametrize(
    "region",
    [
        "krasnodar",
        "moskva",
    ]
)
def test_services_list_for_region(page, region):

    product_page = ProductsPage(page)
    services_page = ServicePage(page)

    product_page.open(region)
    product_page.open_services()

    ui_services = services_page.get_services_in_container("продукты билайна")

    expected_services = get_dop_services(region)
    print("Собранный из контейнера:", ui_services)

    assert set(ui_services) == set(expected_services)
