import scrapy
from scrapy import Spider
from scrapy.selector import Selector
from scrapy.http import TextResponse as response
from InternTracker.items import InternshipPosting
from Logger.logger import career_site_logger
import json
import requests
import csv

class GoldmanSachs(scrapy.Spider) :

    name = "goldmansachs_spy"
    # allowed_domains = []
    start_urls = ['https://www.goldmansachs.com/careers/students/programs/programs-list.json']

    def parse(self,response) :

        try :
            
            # Getting all the postings 
            r = requests.get(response.url).json()
            posts = r['programs']

            # Getting each post and extracting data from it
            for post in posts :
                title = post['title']
                location = post['region']['name']
                link = post['url']
                if ("Intern" in title or "Internship" in title) :

                    # Storing the data in internship item
                    posting = InternshipPosting()
                    posting['role'] = title
                    posting['company_name'] = "Goldman Sachs"
                    posting['location'] = location
                    posting['start_date'] = ""
                    posting['stipendmin'] = 0
                    posting['stipendmax'] = 0
                    posting['deadline'] = ""
                    posting['link'] = f"https://www.goldmansachs.com{link}"
                    posting['number_of_applicants'] = 0
                    posting['posting_date'] = ""
                    posting['category_id'] = 0
                    yield posting
        except Exception as e :
            career_site_logger.error(e)
            