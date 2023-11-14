import scrapy
from scrape_books.items import ScrapeBooksItem
from scrapy.crawler import CrawlerProcess


class Book(scrapy.Spider):
    name = 'Book'
    start_urls = ['https://www.kitapyurdu.com/index.php?route=product/category&page=1&filter_category_all=true&path=1&filter_in_stock=1&sort=purchased_365&order=DESC&limit=100']
    
    page_number = 1
    
    def parse(self, response):
        
        product_links = response.xpath("//div[@class='name ellipsis']/a/@href").getall()
        for product_link in product_links:
            yield scrapy.Request(product_link, callback=self.parse_item)

        next_page_url = response.xpath("//div[@class='links']/a[@class='next']/@href").get()
        print(next_page_url)
        
        
        if self.page_number < 5: 
           self.page_number += 1
           yield scrapy.Request(next_page_url, callback=self.parse)
        
        
        
    def parse_item(self, response):
        
        item = ScrapeBooksItem()
        item['title'] = response.xpath("//h1[@class='pr_header__heading']/text()").get()
        item['author'] = response.xpath("//div[@class='pr_producers__manufacturer']/div/a/text()").get()
        item['publisher'] = response.xpath("//div[@class='pr_producers__publisher']/div/a/text()").get()
        item['price'] = response.xpath("//div[@class='price__item']/text()").get() + response.xpath("//div[@class='price__item']/small/text()").get()
        item['comment_count'] = response.xpath('//p[@class="pr_view-review-text"]/span[2]/text()').get()
        yield item

if __name__ == "__main__":

    process = CrawlerProcess()
    process.crawl(BookSpider)
    process.start()
    