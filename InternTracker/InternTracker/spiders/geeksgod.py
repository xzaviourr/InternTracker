import scrapy
from scrapy import Spider
from scrapy.selector import Selector
from scrapy.http import TextResponse as response
from InternTracker.items import InternshipPosting
from Logger.logger import normal_site_logger

class GeeksGod(scrapy.Spider) :

    name = "geeksgod_spy"
    # allowed_domains = []
    start_urls = ["https://geeksgod.com/category/internships"]

    # Getting total number of pages and going on each page
    def parse(self,response) :

        try :
            number_of_pages = int(response.css('.pages::text').get().split(' ')[-1])
            for i in range(1,number_of_pages + 1) :
                yield scrapy.Request(url = f"https://geeksgod.com/category/internships/page/{i}",callback = self.parse_page)
        except Exception as e :
            normal_site_logger.error(e)

    # Going on each page and getting each post
    def parse_page(self,response) :

        try :
            posts = response.css('.item-details h3 a::attr(href)').getall()
            for post in posts :
                yield scrapy.Request(url = f"{post}",callback = self.parse_post)
        except Exception as e :
            normal_site_logger.error(e)

    # Getting on each post and getting the data
    def parse_post(self,response) :

        try :
            info = response.css('.vk_jobInfo_table tbody tr td::text').getall()
            if (len(info) != 0) :
                title = info[0]
                location = info[-2]
                company = response.css('.entry-thumb::attr(title)').get()
                post = response.url.split('/')[-2]
                yield scrapy.Request(url = f"https://geeksgod.com/link-page/{post}",callback = self.parse_link,meta = {'title' : title,'location' : location,'company' : company})
        except Exception as e :
            normal_site_logger.error(e)

    # Getting the link which is on different page
    def parse_link(self,response) :

        try :
            title = response.meta['title']
            location = response.meta['location']
            company = response.meta['company']
            link = response.css('.elementor-button-wrapper a::attr(href)').getall()[-1]

            # Storing the data in internship item
            posting = InternshipPosting()
            posting['role'] = title.replace("'","")
            posting['company_name'] = company.replace("'","")
            posting['location'] = location.replace('-','')
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
            normal_site_logger.error(e)