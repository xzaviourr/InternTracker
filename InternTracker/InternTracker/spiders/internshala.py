import scrapy
from scrapy import Spider
from scrapy.selector import Selector
from scrapy.http import TextResponse as response
from InternTracker.items import InternshalaItem
from InternTracker.spiders.logger import normal_site_logger
import time

def dateformat(date) :

    date = date.replace("'","").split(" ")
    months = {'Jan':'01','Feb':'02','Mar':'03','Apr':'04','May':'05','Jun':'06','Jul':'07','Aug':'08','Sept':'09','Oct':'10','Nov':'11','Dec':'12'}
    if len(date[0]) == 1 :
        date[0] = '0' + date[0]
    correct = date[0] + '-' + months[date[1]] + '-20' + date[2]
    return correct

class Internshala(scrapy.Spider):
    
    name = "internshala_spy"
    # allowed_domains = ["https://internshala.com/internships/engineering-internship/"]
    start_urls = ["https://internshala.com/internships/engineering-internship/"]

    def parse(self,response) :

        try :
            number_of_pages = int(response.css("#total_pages::text").get())
            for i in range(1,number_of_pages + 1) :
                time.sleep(0.125)
                yield scrapy.Request(url = str(self.start_urls[0] + "page-" + str(i)),callback = self.parse_page)
        except :
            normal_site_logger.error("Error in getting pages")

    def parse_page(self, response) :

        try :
            roles = response.css(".heading_4_5 a::text").getall()

            companies = response.css(".heading_6 a::text").getall()
            companies = [x.replace('\n','').strip() for x in companies]

            locations = response.css(".location_link::text").getall()

            start_dates = response.css(".start_immediately_desktop::text").getall()

            duration_and_deadline = response.css(".item_body::text").getall()
            duration_and_deadline = [x.replace('\n','').strip() for x in duration_and_deadline]
            duration_and_deadline = [x for x in duration_and_deadline if x != '' and x != 'Part time allowed']    
            durations, deadlines = duration_and_deadline[0::2], duration_and_deadline[1::2]
        
            stipends = response.css(".stipend::text").getall()
            stipends = [x.strip() for x in stipends]

            link = response.css(".heading_4_5 a::attr(href)").getall()
        except :
            normal_site_logger.error("Error in getting data")

        try :
            for i in range(len(roles)):
                if durations[i].split(' ')[-1] not in ['Months','Month','Weeks','Week'] :
                    durations[i],deadlines[i] = deadlines[i],durations[i]
                posting = InternshalaItem()
                posting['role'] = roles[i]
                posting['company'] = companies[i]
                posting['location'] = locations[i]
                posting['start_date'] = start_dates[i]
                posting['duration'] = int(durations[i].split(' ')[0])
                posting['stipendmin'] = stipends[i].split(' ')[0].split('-')[0]
                posting['stipendmax'] = stipends[i].split(' ')[0].split('-')[-1]
                posting['deadline'] = dateformat(deadlines[i])
                posting['link'] = "https://internshala.com" + link[i]
                yield posting
        except :
            normal_site_logger.error("Error in storage item")