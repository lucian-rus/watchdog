import scrapy


class MembersSpider(scrapy.Spider):
    name = "members"
    allowed_domains = ["www.senat.ro"]
    start_urls = []
    group_list = {}

    def __init__(self):
        file = open("../output/groups.csv", "r")

        content = file.read().split("\n")
        for line in content:
            line = line.split(",")

            self.start_urls.append(line[1])
            self.group_list[line[1]] = line[0]

        file.close()
        self.clear_output_file_contents()

    def clear_output_file_contents(self):
        # just open the file to overwrite it
        file = open("../output/members.csv", "w")
        file.close()

    def parse(self, response):
        file = open("../output/members.csv", "a")

        url_list = response.css(".mt-2 a").xpath("@href").getall()
        members_list = response.css(".mt-2 ::text").getall()

        if len(url_list) == len(members_list):
            # can use either as url
            for index in range(0, len(url_list)):
                # self.get_members(url_list[index])
                print(members_list[index].strip(), url_list[index])
                file.write(
                    self.group_list[response.request.url]
                    + ","
                    + members_list[index].strip()
                    + ",https://www.senat.ro/"
                    + url_list[index]
                    + "\n"
                )

        file.close()
