import scrapy
import requests


class NetworthSpider(scrapy.Spider):
    name = "networth"
    allowed_domains = ["www.senat.ro"]
    # urls are "https://www.senat.ro/DeclaratieAvere.aspx?ParlamentarID=" + id
    start_urls = []
    group_list = {}

    def __init__(self):
        file = open("../output/members.csv", "r")

        content = file.read().split("\n")
        content = content[:-1]
        for line in content:
            line = line.split(",")
            print(line)
            self.start_urls.append("https://www.senat.ro/DeclaratieAvere.aspx?" + line[2].split("?")[1])
            self.group_list["https://www.senat.ro/DeclaratieAvere.aspx?" + line[2].split("?")[1]] = line[1]

        file.close()

    def parse(self, response):
        url = response.css("#Table1 a").xpath("@href").getall()[0]
        file_data = requests.get("https://www.senat.ro/" + url)
        open("../output/declaratii_avere/" + self.group_list[response.request.url] + ".pdf", "wb").write(file_data.content)
        