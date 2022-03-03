"""
Usage: scrapy crawl emag -a search='samsung tablet'
"""
from itertools import product
from telnetlib import EC
import scrapy
from ..items import ECommerceItem


class EmagBgSpider(scrapy.Spider):
    name = "emag"
    main_url = ["https://www.emag.bg/search/", "?ref=effective_search"]
    
    def __init__(self, search):
        super().__init__()
        self.start_urls = self.build_url(search_term=search,main_url=self.main_url)
    
    def build_url(self, search_term, main_url):
        if not search_term:
            pass
        search_url = main_url[0] + search_term + main_url[1]
        return [search_url]

    def parse(self, response):
        items = ECommerceItem()

        product_name = response.css(".mrg-btm-xxs.js-product-url::text").extract()
        product_link = response.css(".mrg-btm-xxs.js-product-url::attr(href)").extract()
        product_price = response.css(".product-new-price::text").extract()

        items["product_name"] = product_name
        items["product_link"] = product_link
        items["product_price"] = product_price

        yield items
