from http.client import responses
from wsgiref.util import request_uri

import pytest
from playwright.sync_api import sync_playwright
from helpers.search_helpers import extract_tariff_filter

BASE_URL = "https://sort.diginetica.net"

def test_search_filter_for_tarif():

    with sync_playwright() as p:

        request_context = p.request.new_context()

        params={
            "apiKey": "KDLO7HA988",
            "strategy": "vectors_extended,zero_queries",
            "fullData": "true",
            "size": 24,
            "offset": 0,
            "regionId": 98140,
            "st": "тарифы",
            "filter": "price:100;1300"
        }

        response = request_context.get(
            f"{BASE_URL}/search",
            params=params
        )

        assert response.status == 200

        body = response.json()

        assert "products" in body
        assert  len(body["products"]) > 0

        tariff_names = extract_tariff_filter(body["products"])

        assert tariff_names

        print(tariff_names)
