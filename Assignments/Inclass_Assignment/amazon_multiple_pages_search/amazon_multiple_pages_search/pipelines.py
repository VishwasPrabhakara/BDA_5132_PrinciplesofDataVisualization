# amazon_multiple_pages_search/pipelines.py 

import json
from scrapy.exporters import JsonItemExporter

class AmazonMultiplePagesSearchPipeline:
    def __init__(self):
        self.file = open('amazon_data.json', 'wb')
        self.exporter = JsonItemExporter(self.file, encoding='utf-8', ensure_ascii=False, indent=4)
        self.exporter.start_exporting()

    def process_item(self, item, spider):
        self.exporter.export_item(item)
        return item

    def close_spider(self, spider):
        self.exporter.finish_exporting()
        self.file.close()
        
