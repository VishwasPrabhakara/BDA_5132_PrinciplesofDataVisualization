import scrapy
from ..items import AmazontutorialItem


class AmazonSpiderSpider(scrapy.Spider):
    name = 'amazon_spider'
    allowed_domains = ['amazon.in']
    start_urls = [
        'https://www.amazon.in/s?bbn=976389031&rh=n%3A976389031%2Cp_n_publication_date%3A2684820031&dc&fst=as%3Aoff&qid=1604714783&rnid=2684818031&ref=lp_976389031_nr_p_n_publication_date_1'
        ]

    def parse(self, response):
        items = AmazontutorialItem()
        
        book_name = response.css('.a-color-base.a-text-normal::text').extract()
        book_author = response.css('.a-color-secondary .a-size-base+ .a-size-base , .a-color-secondary .a-size-base.a-link-normal').css('::text').extract()
        book_price = response.css('.a-spacing-top-small .a-price-whole').css('::text').extract()
        book_imagelink = response.css('.s-image::attr(src)').extract()
        
        items['book_name'] = book_name
        items['book_author'] = book_author
        items['book_price'] = book_price
        items['book_imagelink'] = book_imagelink
        
        yield items