import scrapy
from scrapy import Spider
from scrapy.selector import Selector
from scrapy.exceptions import CloseSpider
from scrapy.http import TextResponse as response
from InternTracker.items import InternshipPosting
from Logger.logger import career_site_logger
import requests
import json
import requests
import csv
import scrapy_splash

class Adobe(scrapy.Spider) :

    name = 'adobe_spy'
    # allowed_domains = []
    close_spider = False

    # Sending initial request to render the page
    def start_requests(self) :

        try :
            url = 'https://adobe.wd5.myworkdayjobs.com/external_university/1/refreshFacet/318c8bb6f553100021d223d9780d30be'
            yield scrapy_splash.SplashRequest(url = url,callback = self.parse,args = {'wait' : 10})
        except Exception as e :
            career_site_logger.error(e)

    # Getting the total number of pages and then getting each page then getting each post
    def parse(self,response) :

        try :
            # number_of_pages sometimes gives error in that case hardcode it to 30 or similar depending on the total posting on the official page
            number_of_pages = (int(response.css('.WAUO span::text').get().strip().split(' ')[0]) // 50) + 1
            for i in range(number_of_pages) :
                r = requests.get(f'https://adobe.wd5.myworkdayjobs.com/external_university/1/searchPagination/318c8bb6f553100021d223d9780d30be/{i * 50}').json()
                for j in range(50) :
                    cur = r['body']['children'][0]['children'][0]['listItems'][j]['title']['commandLink']
                    yield scrapy_splash.SplashRequest(url = f'https://adobe.wd5.myworkdayjobs.com{str(cur)}',callback = self.parse_post,args = {'wait' : 5})
        except Exception as e :
            career_site_logger.error(e)

    # Going on each post and getting the data
    def parse_post(self,response) :

        # Closes the spider if record already scraped before
        if self.close_spider :
            raise CloseSpider(reason = "ALREADY SCRAPED")
        try :
            # CSS tags were not working in some pages so got info from post link iteself
            link = str(response.url)
            role = link.split('/')[-1].split('_')[0].replace('XMLNAME-','')
            location = link.split('/')[-2]
            if 'Intern' in role or 'Internship' in role :

                # Storing the data in internship item
                posting = InternshipPosting()
                posting['role'] = role
                posting['company_name'] = "Adobe"
                posting['location'] = location
                posting['start_date'] = ""
                posting['stipendmin'] = 0
                posting['stipendmax'] = 0
                posting['deadline'] = ""
                posting['link'] = link
                posting['number_of_applicants'] = 0
                posting['posting_date'] = ""
                posting['category_id'] = 0
                yield posting
        except Exception as e :
            career_site_logger.error(e)