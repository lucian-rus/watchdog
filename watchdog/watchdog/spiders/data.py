import scrapy


class DataSpider(scrapy.Spider):
    name = "data"
    allowed_domains = ["www.senat.ro"]
    start_urls = ["https://www.senat.ro/FisaSenator.aspx?ParlamentarID=4ECEF3DD-1F70-4433-82BA-54975207C4A1"]

    def parse(self, response):
        print(response)
