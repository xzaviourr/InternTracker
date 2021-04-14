import scrapy
from scrapy import Spider
from scrapy.selector import Selector
from scrapy.http import TextResponse as response
from InternTracker.items import InternshipPosting
from Logger.logger import career_site_logger
import time
import scrapy_splash

# 'wait' parameters need to be set in such a way as to optimize the scraping or the filter parameters need to be found

class Microsoft(scrapy.Spider) :

    name = "microsoft_spy"

    # Getting the first initial request from the site
    def start_requests(self) :

        try :
            url = "https://careers.microsoft.com/students/us/en/search-results"
            yield scrapy_splash.SplashRequest(url = url,callback = self.parse,args = {'wait' : 5})
        except Exception as e :
            career_site_logger.error(e)

    # Getting each page of the site
    def parse(self,response) :

        try :
            number_of_pages = (int(response.css(".total-jobs::text").get().strip()) // 20) + 1
            for i in range(number_of_pages) :
                yield scrapy_splash.SplashRequest(url = f"https://careers.microsoft.com/students/us/en/search-results?from={str(i * 20)}&s=1",callback = self.parse_page,args = {'wait' : 5})
        except Exception as e :
            career_site_logger.error(e)

    # Getting each post of every page
    def parse_page(self,response) :

        try :
            posts = response.css(".information h2 a::attr(href)").getall()
            for post in posts :
                yield scrapy_splash.SplashRequest(url = post,callback = self.parse_post,args = {'wait' : 5})
        except Exception as e :
            career_site_logger.error(e)

    # Processing the data from every post
    def parse_post(self,response) :

        try :
            post_details = response.css(".lable-text::text").getall()
            # location = ""
            # post_location = response.css(".job-other-info span::text").getall()
            post_role = response.css(".job-info h1::text").getall()
            if post_details[3] == 'Engineering' and post_details[5] == 'Internship' :
                post_id = post_details[0]

                # Storing the data from each post into an item
                posting = InternshipPosting()
                posting['role'] = post_role[0]
                posting['company_name'] = "Microsoft"
                posting['location'] = "" # str(location + post_location[0])
                posting['start_date'] = ""
                posting['stipendmin'] = 0
                posting['stipendmax'] = 0
                posting['deadline'] = ""
                posting['link'] = f"https://careers.microsoft.com/students/us/en/job/{post_id}"
                posting['number_of_applicants'] = 0
                posting['posting_date'] = post_details[1]
                posting['category_id'] = 0
                yield posting
        except Exception as e :
            career_site_logger.error(e)