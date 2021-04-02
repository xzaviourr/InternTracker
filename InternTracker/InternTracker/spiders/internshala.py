import scrapy
from scrapy import Spider
from scrapy.selector import Selector
from scrapy.http import TextResponse as response
from InternTracker.items import InternshalaItem


class Internshala(scrapy.Spider):
    name = "internshala_spy"
    allowed_domains = ["https://internshala.com/internships/engineering-internship/"]
    number_of_pages = 60
    start_urls = [str("https://internshala.com/internships/engineering-internship/page-" + str(x)) for x in range(1, number_of_pages+1)]

    def parse(self, response):
        roles = response.css(".heading_4_5 a::text").getall()

        companies = response.css(".heading_6 a::text").getall()
        companies = [x.replace('\n','').strip() for x in companies]

        locations = response.css(".location_link::text").getall()

        start_dates = response.css(".start_immediately_desktop::text").getall()

        duration_and_deadline = response.css(".item_body::text").getall()
        duration_and_deadline = [x.replace('\n','').strip() for x in duration_and_deadline]
        duration_and_deadline = [x for x in duration_and_deadline if x != '']    
        durations, deadlines = duration_and_deadline[0::2], duration_and_deadline[1::2]
    
        stipends = response.css(".stipend::text").getall()
        stipends = [x.strip() for x in stipends]

        for i in range(len(roles)):
            posting = InternshalaItem()
            posting['role'] = roles[i]
            posting['company'] = companies[i]
            posting['location'] = locations[i]
            posting['start_date'] = start_dates[i]
            posting['duration'] = durations[i]
            posting['stipend'] = stipends[i]
            posting['deadline'] = deadlines[i]
            yield posting