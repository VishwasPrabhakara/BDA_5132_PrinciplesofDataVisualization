# amazon_single_page_search/items.py

import scrapy

class AmazonItem(scrapy.Item):
    name = scrapy.Field()
    price = scrapy.Field()
    brand = scrapy.Field()
