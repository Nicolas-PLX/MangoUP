import scrapy 
from WebReader.utils import get_urls

class ManganatoSpider(scrapy.Spider):
    site = "manganato"
    urls = []

    def get_url(self):
        urls = get_urls()
     
    def parse(self,response):
        pass 