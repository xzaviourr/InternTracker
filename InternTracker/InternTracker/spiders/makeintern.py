import scrapy
from scrapy import Spider
from scrapy.selector import Selector
from scrapy.exceptions import CloseSpider
from scrapy.http import TextResponse as response
from InternTracker.items import InternshipPosting
from Logger.logger import normal_site_logger

class Makeintern(scrapy.Spider):
    name="makeintern"
    #different urls for different fields
    web_list=['https://www.makeintern.com/internships/search/web-design-and-development?page='+str(i) for i in range(1,30)]
    software_list=['https://www.makeintern.com/internships/search/software-development?page='+str(i) for i in range(1,30)]
    graphics_list=['https://www.makeintern.com/internships/search/graphic-design?page='+str(i) for i in range(1,30)]
    start_urls=web_list+software_list
    close_spider = False
    
    def parse(self,response):
        #scraping the url
        try:
            for i in range(len(self.start_urls)):
                yield scrapy.Request(url=str(self.start_urls[i]),callback=self.parse_jobs)
        except :
            normal_site_logger.error("Error in getting page")

    def parse_jobs(self,response):

        # Closes the spider if record already scraped before
        if self.close_spider :
            raise CloseSpider(reason = "ALREADY SCRAPED")
        #getting data of jobs
        try:
            roles = response.css('.intern_headings a::text').getall()
            companies = response.xpath('//*[@class="students-rank"]/li[1]/a[2]/text()').getall() 
            locations = response.xpath('//*[@class="students-rank"]/li[4]/a[2]/text()').getall()
            link = response.css('.intern_headings a::attr(href)').getall()
            posting_dates = response.xpath('//*[@id="internship-content"]/b[1]/text()').getall()
            deadlines = response.xpath('//*[@id="internship-content"]/b[2]/text()').getall()
            number_of_applicants = response.xpath('//*[@class="students-rank"]/li[2]/a[2]/text()').getall()
            stipend = response.xpath('//*[@class="students-rank"]/li[5]/a[2]/text()').getall()
        except:
            normal_site_logger.error("Error in getting data")

        #saving data of jobs in csv file
        try :
            for i in range(len(roles)):
                posting = InternshipPosting()
                posting['role'] = roles[i]
                posting['company_name'] = companies[i]
                posting['location'] = locations[i]
                posting['start_date'] = "-"

                #writing stipend in proper format
                if "Unpaid" in stipend[i]:
                    posting['stipendmin'] = 0
                    posting['stipendmax'] = 0
                else:
                    s=((stipend[i].split())[1]).split("-")
                    posting['stipendmin'] = s[0]
                    posting['stipendmax'] = s[-1]

                posting['deadline'] = deadlines[i]
                posting['link'] = link[i]+" "
                posting['number_of_applicants'] = number_of_applicants[i]
                posting['posting_date'] = posting_dates[i]
                posting['category_id'] = "0"
                yield posting
        except Exception as e :
            normal_site_logger.error(e)


