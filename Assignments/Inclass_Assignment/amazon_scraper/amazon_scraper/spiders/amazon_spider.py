import scrapy

class AmazonSpider(scrapy.Spider):
    name = 'amazon_spider'
    start_urls = ['https://www.amazon.in/Adidas-Mens-Regular-T-Shirt-H13881_Red/dp/B09NYKPR58/ref=sr_1_6?keywords=manchester+united+jersey&sr=8-6']

    def parse(self, response):
        # Your scraping logic here
        title = response.css('span#productTitle::text').get()
        price = response.css('span.a-price-whole::text').get()
        description = response.xpath('//span[contains(text(), "Product Dimensions")]/following-sibling::span/text()').get()

        yield {
            'title': title.strip() if title else None,
            'price': price.strip() if price else None,
            'description': description.strip() if description else None,
        }
