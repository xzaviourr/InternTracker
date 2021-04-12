import scrapy
from scrapy import Spider
from scrapy.selector import Selector
from scrapy.http import TextResponse as response
from InternTracker.items import InternshipPosting
from Logger.logger import career_site_logger
import json
import requests
import csv

class Google(scrapy.Spider) :

    name = "google_spy"
    # allowed_domains = []
    start_urls = ["https://careers.google.com/api/v2/jobs/search/?degree=BACHELORS&distance=50&employment_type=INTERN&q="]

    def parse(self,response) :

        url = "https://careers.google.com/api/v2/jobs/search/?degree=BACHELORS&distance=50&employment_type=INTERN&q="

        try :
            r = requests.get(url).json()

            # Getting total number of pages
            number_of_pages = (int(r['count']) // int(r['page_size'])) + 1
            
            # Going on each of the pages and getting the postings on each page
            for i in range(1,number_of_pages + 1) :
                page = requests.get(f"https://careers.google.com/api/v2/jobs/search/?degree=BACHELORS&distance=50&employment_type=INTERN&page={str(i)}&q=").json()
                
                # Getting each post and then processing the data from it
                for j in range(int(page['page_size'])) :
                    job_id = page['jobs'][j]['job_id'].split('/')[-1]
                    post = requests.get(f"https://careers.google.com/api/v2/jobs/get/?job_name=jobs%2F{job_id}").json()
                    location = ""
                    for k in range(len(post['locations'])) :
                        # country_code or country (codes are consistent,country tags are not)
                        location += (str(post['locations'][k]['country']) + ",")
                    posting_date = post['created'][0:10].split('-')

                    # Storing all the data in internship item
                    posting = InternshipPosting()
                    posting['role'] = post['title']
                    posting['company_name'] = post['company_name']
                    posting['location'] = "" # location[:-1] UNEXPECTED CHARACTER ENCOUNTERED
                    posting['start_date'] = ""
                    posting['stipendmin'] = 0
                    posting['stipendmax'] = 0
                    posting['deadline'] = ""
                    posting['link'] = f"https://careers.google.com/jobs/results/{str(job_id)}/?degree=BACHELORS&distance=50&employment_type=INTERN"
                    posting['number_of_applicants'] = 0
                    posting['posting_date'] = posting_date[2] + "-" + posting_date[1] + "-" + posting_date[0]
                    posting['category_id'] = 0
                    yield posting
        except Exception as e :
            career_site_logger.error(e)