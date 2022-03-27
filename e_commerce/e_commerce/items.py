# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class ECommerceItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    # product_type = scrapy.Field()
    product_name = scrapy.Field()
    product_link = scrapy.Field()
    product_price = scrapy.Field()
    search = scrapy.Field()
    date = scrapy.Field()
    brand = scrapy.Field()
    site = scrapy.Field()
    user = scrapy.Field()
