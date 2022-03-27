"""
Usage: scrapy crawl emag -a search='samsung tablet'
"""
from asyncio.windows_events import NULL
from itertools import product
from telnetlib import EC
import scrapy
from scrapy.selector import Selector
from ..items import ECommerceItem
from datetime import datetime


class EmagBgSpider(scrapy.Spider):
    name = "emag"
    main_url = ["https://www.emag.bg/search/", "?ref=effective_search"]
    
    def __init__(self, search, brand=NULL, site=NULL, user=0):
        super().__init__()
        self.start_urls = self.build_url(search_term=search,main_url=self.main_url)
        self.search = search
        self.brand = brand
        self.site = site
        self.user = user
    
    def build_url(self, search_term, main_url):
        if not search_term:
            pass
        search_url = main_url[0] + search_term + main_url[1]
        return [search_url]


    def parse(self, response):
        e_item = ECommerceItem()
        items = []
        date = datetime.now().isoformat()
        product_items = response.css(".js-product-data").extract()
        # print(product_items)
        for item in product_items:
            print("-----------------------------------")
            html_item = Selector(text=item)
            e_item['product_name'] = html_item.css(".mrg-btm-xxs.js-product-url::text").extract()[0]
            e_item['product_link'] = html_item.css(".mrg-btm-xxs.js-product-url::attr(href)").extract()[0]
            e_item['product_price'] = html_item.css(".product-new-price::text").extract()[0]
            e_item['date'] = date
            e_item['search'] = self.search
            e_item['brand'] = self.brand
            e_item['site'] = self.site
            e_item['user'] = self.user

            items.append(e_item)
        
        yield items
