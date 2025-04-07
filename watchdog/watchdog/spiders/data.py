import scrapy
import json
from scrapy.http import FormRequest


class DataSpider(scrapy.Spider):
    name = "data"
    allowed_domains = ["www.senat.ro"]
    start_urls = ["https://www.senat.ro/FisaSenator.aspx?ParlamentarID=F1658CFA-9AEA-415D-8EF2-EC0E6E4046FC"]
    # stores member list data
    member_list = {}

    def __init__(self):
        # file = open("../output/members.csv", "r")

        # content = file.read().split("\n")
        # # contains an additional newline, so just strip the last line of data
        # content = content[:-1]

        # for line in content:
        #     line = line.split(",")

        #     self.start_urls.append(line[2])
        #     self.member_list[line[2]] = line[1]
        #     print(line[2], line[1])

        # file.close()
        pass

    def parse(self, response):
        file = open("../output/get_data.txt", "w")
        file.write(response.text)
        file.close()
        
        # get a way to properly handle multiple pages
        return self.get_biography(response)

    def get_biography(self, response):
        post_request = {}

        post_request["ctl00$MyScriptManager"] = (
            "ctl00$B_Center$pnlUpd|ctl00$B_Center$Repeater14$ctl00$lnkBiog"
        )
        post_request["__EVENTTARGET"] = "ctl00$B_Center$Repeater14$ctl00$lnkBiog"
        post_request["__EVENTARGUMENT"] = ""
        post_request["__VIEWSTATE"] = response.css("#__VIEWSTATE").xpath("@value").getall()[0]
        post_request["__VIEWSTATEGENERATOR"] = "B2195F17"
        post_request["__SCROLLPOSITIONX"] = "0"
        post_request["__SCROLLPOSITIONY"] = "0"
        post_request["__VIEWSTATEENCRYPTED"] = ""
        post_request["__ASYNCPOST"] = "true"
        post_request[""] = ""

        # this is here just as a debug manner
        file = open("../output/request.json", "w")
        file.write(json.dumps(post_request))
        file.close()

        HEADERS = {
            "X-MicrosoftAjax": "Delta=true",
            "User-Agent": "Mozilla/5.0 (X11; Linux x86_64; rv:134.0) Gecko/20100101 Firefox/134.0",
            "X-Requested-With": "XMLHttpRequest",
        }

        return FormRequest(
            url=response.request.url,
            method="POST",
            callback=self.parse_post_data,
            formdata=post_request,
            meta={"page": 1},
            dont_filter=True,
            headers=HEADERS,
        )

    # in theory this should work
    def parse_post_data(self, response):
        file = open("../output/post_data.txt", "w")
        file.write(response.text)
        file.close()
