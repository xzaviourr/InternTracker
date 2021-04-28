import scrapy
from scrapy import Spider
from scrapy.selector import Selector
from scrapy.http import TextResponse as response
from InternTracker.items import InternshipPosting
from Logger.logger import career_site_logger

class Uber(scrapy.Spider) :

    name = "uber_spy"
    # allowed_domains = []
    start_urls = ['https://www.uber.com/us/en/careers/list/?department=University&team=Engineering']

    # Getting total pages and going to each page
    def parse(self,response) :

        try :
            # URL doesn't change with clicking on load more need to look into as API is blocked, currently at max 10 posts can be extracted
            number_of_pages = (int(response.css('.kk div div div p::text').get().split()[0]) // 10) + 1
            for i in range(number_of_pages) :
                yield scrapy.Request(url = 'https://www.uber.com/us/en/careers/list/?department=University&team=Engineering',callback = self.parse_page)
        except Exception as e :
            career_site_logger.error(e)

    # Getting the posting data all at once from each main page and processing it
    def parse_page(self,response) :

        try :
            # Extracting data form posting page is causing problems probably splash needs to be used, currently data is taken from main page all at once
            roles = response.css('.l1 a::text').getall()
            links = response.css('.l1 a::attr(href)').getall()
            locations = response.css('.pz.q0 div span::text').getall()

            for i in range(len(roles)) :
                post_id = links[i].split('/')[-1]

                # Storing the data in internship item
                posting = InternshipPosting()
                posting['role'] = roles[i]
                posting['company_name'] = 'Uber'
                posting['location'] = locations[i]
                posting['start_date'] = ''
                posting['stipendmin'] = 0
                posting['stipendmax'] = 0
                posting['deadline'] = ''
                posting['link'] = f'https://university-uber.icims.com/jobs/{str(post_id)}/job'
                posting['number_of_applicants'] = 0
                posting['posting_date'] = ""
                posting['category_id'] = 0
                yield posting
        except Exception as e :
            career_site_logger.error(e)
