import scrapy


class GroupsSpider(scrapy.Spider):
    name = "groups"
    allowed_domains = ["www.senat.ro"]
    start_urls = ["https://www.senat.ro/EnumGrupuri.aspx"]

    def parse(self, response):
        # this is relative to dir from which the script is ran
        file = open("../output/groups.csv", "w")

        url_list = response.css(".nsnt-group-card__name").xpath("@href").getall()
        group_list = response.css(".nsnt-group-card__name ::text").getall()

        if len(url_list) == len(group_list):
            # can use either as url
            for index in range(0, len(url_list)):
                # do this to get the proper link in the CSV
                file.write(
                    group_list[index] + ",https://www.senat.ro/" + url_list[index]
                )
                if index < len(url_list) - 1:
                    file.write("\n")

        file.close()
