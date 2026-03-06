def extract_tariff_filter(products: list) -> list[str]:
    return [
        product["name"]
        for product in products
        if isinstance(product.get("name"), str)
    ]
