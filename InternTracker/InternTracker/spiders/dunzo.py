import scrapy
from scrapy import Spider
from scrapy.selector import Selector
from scrapy.http import TextResponse as response
from InternTracker.items import DunzoItem
from Logger.logger import normal_site_logger

class Dunzo(scrapy.Spider):
    name = "dunzo"
    #allowed_domains = ["https://dunzo.com","https://www.greenhouse.io/"]
    start_urls = ["https://boards.greenhouse.io/embed/job_board?for=dunzo13&b=https%3A%2F%2Fwww.dunzo.com%2Fcareers.html"]

    custom_settings={
        'ITEM_PIPELINES' : {
            'InternTracker.pipelines.InterntrackerPipeline': 300,
            'InternTracker.pipelines.CsvPipeline': 500,
        }
    }

    def parse(self, response):
        try:
            #getting role and job_link for that particular role, from the job_board
            roles = response.xpath('//*[@department_id="4043932002"]/a/text()').getall()
            link = response.xpath('//*[@department_id="4043932002"]/a/@href').getall()
        except:
            normal_site_logger.error("Error getting role or link")

        for i in range(len(roles)):
            posting = DunzoItem()
            posting['role'] = roles[i]
            posting['link'] = link[i]+" "
            job_id = link[i].split("=")[-1] #link is splitted here to extract job_id
            job_url="https://boards.greenhouse.io/embed/job_app?for=dunzo13&token="+job_id+"?gh_jid="+job_id+"&b=https%3A%2F%2Fwww.dunzo.com%2Fcareers.html"
            try:
                yield scrapy.Request(url=str(job_url), callback=self.parse_url, meta={'posting': posting})
                #parsing details of the job through the job_url
            except:
                normal_site_logger.error("Error in getting details of job_id:"+job_id)
    
    def parse_url(self, response):
        posting = response.meta['posting']
        try:
            if len(". ".join(response.xpath('//*[@id="content"]/ol[1]/li/span/text()').getall()))!=0:
                posting['responsibilities'] = (". ".join(response.xpath('//*[@id="content"]/ol[1]/li/span/text()').getall()))
            elif len(". ".join(response.xpath('//*[@id="content"]/ol[1]/li/text()').getall()))!=0:
                posting['responsibilities'] = (". ".join(response.xpath('//*[@id="content"]/ol[1]/li/text()').getall()))
            elif len(". ".join(response.xpath('//*[@id="content"]/ul[1]/li/span/text()').getall()))!=0:
                posting['responsibilities'] = (". ".join(response.xpath('//*[@id="content"]/ul[1]/li/span/text()').getall()))
            elif len(". ".join(response.xpath('//*[@id="content"]/ul[1]/li/text()').getall()))!=0:
                posting['responsibilities'] = (". ".join(response.xpath('//*[@id="content"]/ul[1]/li/text()').getall()))
        except:
            normal_site_logger.error("Error in getting responsibilities")

        try:
            if len(". ".join(response.xpath('//*[@id="content"]/ol[2]/li/span/text()').getall()))!=0:
                posting['requirements'] = (". ".join(response.xpath('//*[@id="content"]/ol[1]/li/span/text()').getall()))
            elif len(". ".join(response.xpath('//*[@id="content"]/ol[2]/li/text()').getall()))!=0:
                posting['requirements'] = (". ".join(response.xpath('//*[@id="content"]/ol[1]/li/text()').getall()))
            elif len(". ".join(response.xpath('//*[@id="content"]/ul[2]/li/span/text()').getall()))!=0:
                posting['requirements'] = (". ".join(response.xpath('//*[@id="content"]/ul[1]/li/span/text()').getall()))
            elif len(". ".join(response.xpath('//*[@id="content"]/ul[2]/li/text()').getall()))!=0:
                posting['requirements'] = (". ".join(response.xpath('//*[@id="content"]/ul[1]/li/text()').getall()))    
        except:
            normal_site_logger.error("Error in getting requirements of the job")  
        
        yield posting