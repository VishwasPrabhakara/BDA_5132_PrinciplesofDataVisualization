# -*- coding: utf-8 -*-
"""
Created on Wed Oct 21 14:07:45 2020

@author: MAHE-MIT-00
"""

import scrapy
from ..items import QuotetutorialItem  #describe when items are explained


class QuotesSpider(scrapy.Spider):
    
    name = 'quotes'
    page_number = 2
    start_urls = ['http://quotes.toscrape.com/login']
    
    def parse(self, response):
        token = response.css('form input::attr(value)').extract_first()
        print(token)