# -*- coding: utf-8 -*-
"""
Created on Wed Oct 21 14:07:45 2020

@author: MAHE-MIT-00
"""

import scrapy
from ..items import QuotetutorialItem  #describe when items are explained


class QuotesSpider(scrapy.Spider):
    '''
 Dont change the variable names: 
     1. name and 2. start_url as scrapy expects this name
    '''
    name = 'quotes'
    start_urls = ['http://quotes.toscrape.com']

#response has source code of the website to scrape
#We shall scrape the title of the website inspect the website


    def parse(self, response):
        
        
        items = QuotetutorialItem()   #describe when items are explained
        

        
        '''
        selector: it is a condition using which data can be extracted from any website.
        
        selector are of two types 1. CSS (common) and 2. XPath (not so/that common).
        
        XPath: used in next page buttons (view quotes html code)
        
        selecting a particular HTML tag or a particular CSS or an ID inside the
        source code is known as a CSS selector.
        we do this by typing in resonse dot CSS and then typing in the if condition inside
        the CSS function. 
        This idea of writing a CSS condition kind of an if condition is known as a CSS selector.
        
        Use scrapy shell (Anaconda power shell: scrapy shell "website name") to effective use the CSS selector.
        '''
        
        #Below will scrape title with HTML element
        #title = response.css('title').extract()
        
        #Below will scrape title only
        #title = response.css('title::text').extract()
        
        
        '''
        yield is a keyword similar to return keyword used
        inside a function. The need to use  yield keyword 
        instead of return statement is that yield is usually 
        used with a generator and this generator is being 
        used by scrappy behind the scene
        '''
        #yield{'titletext':title}

#-------------Show output untill this and explain css and xpath in shell -------------
        
        # #all_div_quotes = response.css('div.quote')[0]  # here no extract as we req items in the class like quote, author
        # all_div_quotes = response.css('div.quote')     # run 2
        # title = all_div_quotes.css('span.text::text').extract()
        # author = all_div_quotes.css('.author::text').extract()
        # tag = all_div_quotes.css('.tag::text').extract()
        # yield{
        #     'Title' : title,
        #     'Author' : author,
        #     'Tag' : tag
        #     }

#----------- execute and demonstrate uptohere: scrapy crawl quotes (TAT1 and tat2.png)--------------------
        
#Below code is to scrape one after the another
        # all_div_quotes = response.css('div.quote')     # run 2
        
        # for quotes in all_div_quotes:
            
        #     title = quotes.css('span.text::text').extract()
        #     author = quotes.css('.author::text').extract()
        #     tag = quotes.css('.tag::text').extract()
            
        #     yield{
        #         'Title' : title,
        #         'Author' : author,
        #         'Tag' : tag
        #         }


#----------- execute and demonstrate uptohere: scrapy crawl quotes (TAT3.png)--------------------


        '''
        Item Containers: 
        Need: To handle Typo and missing values
        Extracted data --> temporary containers (items) --> store in database
        Go to items.py and enter field values in # name = scrapy.Field()
        
        Below code is to scrape one after the another with item(comtainers)
        
        '''

        all_div_quotes = response.css('div.quote')     # run 3
        
        for quotes in all_div_quotes:
            
            title = quotes.css('span.text::text').extract()
            author = quotes.css('.author::text').extract()
            tag = quotes.css('.tag::text').extract()
            
            items['title'] = title
            items['author'] = author
            items['tag'] = tag
            
            
            yield items
        
        next_page = response.css('li.next a::attr(href)').get()
        
        if next_page is not None:
            yield response.follow(next_page, callback= self.parse)
            
            



#---------------------execute and demonstrate uptohere for storing in items containers -----
        '''
            Now to store the data on to file: JSON, CSV, and XML
            
            In Anaconda terminal type following commands
            
            JSON: scrapy crawl quotes -o items.json
            
            CSV: scrapy crawl quotes -o items.csv
            
            XML: scrapy crawl quotes -o items.xml
            
        '''
#---------------execute and demonstrate uptohere for storing on JSON ect-----------------

        '''
            Demonstration of storing data on to SQLite database 
            
            changes needed to make in pipeline file 
            
            
        '''
