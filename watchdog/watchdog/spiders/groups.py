import scrapy


class GroupsSpider(scrapy.Spider):
    name = "groups"
    allowed_domains = ["www.senat.ro"]
    start_urls = ["https://www.senat.ro/EnumGrupuri.aspx"]

    # def get_members(self, url):
    #     print("================================================== 22")
    #     yield scrapy.Request(url = "https://www.senat.ro/" + url, callback = self.parse_member_list)

    # def parse_member_list(self, response):
    #     print("================================================== 11")
    #     member_list = response.css(".mt-2")

    def parse(self, response):
        url_list = response.css(".nsnt-group-card__name").xpath("@href").getall()
        group_list = response.css(".nsnt-group-card__name ::text").getall()

        if len(url_list) == len(group_list):
            # can use either as url
            for index in range(0, len(url_list)):
                # self.get_members(url_list[index])
                print(group_list[index], url_list[index])