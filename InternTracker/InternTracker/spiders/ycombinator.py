import scrapy
from scrapy import Spider
from scrapy.selector import Selector
from scrapy.http import TextResponse as response
from InternTracker.items import InternshipPosting
from Logger.logger import normal_site_logger

class Ycombinator(scrapy.Spider):
    name="ycombinator"
    start_urls=['https://www.workatastartup.com/internships',]

    def parse(self,response):
        #scraping the url
        try:
            yield scrapy.Request(url=str(self.start_urls[0]),callback=self.parse_jobs)
        except :
            normal_site_logger.error("Error in getting page")

    def parse_jobs(self,response):
        #getting data of jobs
        try:
            roles = response.xpath('//*[@class="job-view-link job-detail job-name"]/text()').getall()
            companies = response.xpath('//*[@class="job-company-name"]/text()').getall() 
            locations = response.xpath('//*[@class="job-details"]/div[2]/text()').getall()
            link = response.css('.company-details a::attr(href)').getall()
        except:
            normal_site_logger.error("Error in getting data")

        #saving data of jobs in csv file
        try :
            for i in range(len(roles)):
                posting = InternshipPosting()
                posting['role'] = roles[i]
                posting['company_name'] = companies[i]
                posting['location'] = locations[i]+" "
                posting['start_date'] = "-"
                posting['stipendmin'] = "-"
                posting['stipendmax'] = "-"
                posting['deadline'] = "-"
                posting['link'] = link[i]
                posting['number_of_applicants'] = "-"
                posting['posting_date'] = ""
                posting['category_id'] = "-"
                yield posting
        except Exception as e :
            normal_site_logger.error(e)


