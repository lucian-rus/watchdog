import scrapy


class MembersSpider(scrapy.Spider):
    name = "members"
    allowed_domains = ["www.senat.ro"]
    start_urls = ["https://www.senat.ro/ComponentaGrupuri.aspx?Zi&GrupID=6c0fa8ee-7660-446c-9185-0570d8cb9193"]

    def parse(self, response):
        url_list = response.css(".mt-2 a").xpath("@href").getall()
        members_list = response.css(".mt-2 ::text").getall()

        if len(url_list) == len(members_list):
            # can use either as url
            for index in range(0, len(url_list)):
                # self.get_members(url_list[index])
                print(members_list[index].strip(), url_list[index])