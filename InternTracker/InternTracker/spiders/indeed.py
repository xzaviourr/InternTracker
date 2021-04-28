import scrapy
from scrapy import Spider
from scrapy.selector import Selector
from scrapy.http import TextResponse as response
from InternTracker.items import InternshipPosting
from Logger.logger import normal_site_logger
import time

# def dateformat(date) :

#     date = date.replace("'","").split(" ")
#     months = {'Jan':'01','Feb':'02','Mar':'03','Apr':'04','May':'05','Jun':'06','Jul':'07','Aug':'08','Sept':'09','Oct':'10','Nov':'11','Dec':'12'}
#     if len(date[0]) == 1 :
#         date[0] = '0' + date[0]
#     correct = date[0] + '-' + months[date[1]] + '-20' + date[2]
#     return correct

class Indeed(scrapy.Spider):
    
    name = "indeed"
    # allowed_domains = ["https://indeed.com"]
    start_urls = ["https://in.indeed.com/jobs?q=internship+web+development&start="]

    def parse(self,response) :
    
        try :
            for i in range(100) :
                time.sleep(0.5)
                yield scrapy.Request(url = str(self.start_urls[0] + str(i*10)),callback = self.parse_page)
        except :
            normal_site_logger.error("Error in getting pages")
    def parse_page(self, response) :

        try :
            roles = response.css(".title a::attr(title)").getall()
            companies = response.css(".sjcl div span::text").getall()
            # companies = [x.replace('\n','').replace("'","").strip() for x in companies]
            locations=[]
            locations = response.xpath('//*[@class="location accessible-contrast-color-location"]/text()').getall()
            stipends = response.css(".salaryText::text").getall()
            link = response.css(".title a::attr(href)").getall()
            posted_before=response.css(".date::text").getall()
        except :
            normal_site_logger.error("Error in getting data")

        try :
            for i in range(len(roles)):
                posting = InternshipPosting()
                posting['role'] = roles[i]
                posting['company_name'] = companies[i]
                posting['location'] = locations[i]
                posting['start_date'] = '-'
                # posting['duration'] = int(durations[i].split(' ')[0])
                stipend=stipends[i].split()
                if "-" in stipend:
                    posting['stipendmin'] = int("".join((stipend[0][1:]).split(",")))
                    posting['stipendmax'] = int("".join((stipend[2][1:]).split(",")))
                else:
                    posting['stipendmin'] = 0
                    posting['stipendmax'] = int("".join((stipend[0][1:]).split(",")))
                posting['deadline'] = "-"
                posting['link'] = "https://indeed.com" + link[i]
                posting['number_of_applicants'] = 0
                posting['posting_date'] = posted_before[i]
                posting['category_id'] = 0
                yield posting
        except Exception as e :
            normal_site_logger.error(e)