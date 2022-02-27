from itertools import product
from telnetlib import EC
import scrapy
from ..items import ECommerceItem


class EmagBgSpider(scrapy.Spider):
    name = "emag"
    # allowed_domains = ['emag.bg/search/tablet']
    start_urls = ["http://emag.bg/search/tablet/"]

    def parse(self, response):
        items = ECommerceItem()

        product_name = response.css(".mrg-btm-xxs.js-product-url::text").extract()
        product_link = response.css(".mrg-btm-xxs.js-product-url::attr(href)").extract()
        product_price = response.css(".product-new-price::text").extract()

        items["product_name"] = product_name
        items["product_link"] = product_link
        items["product_price"] = product_price

        yield items
