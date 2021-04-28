import scrapy
from scrapy import Spider
from scrapy.selector import Selector
from scrapy.http import TextResponse as response
from InternTracker.items import InternshipPosting
from Logger.logger import career_site_logger

class SimplyHired(scrapy.Spider) :

    name = "simplyhired_spy"
    # allowed_domains = []
    start_urls = [
        "https://www.simplyhired.co.in/search?q=software+engineer&jt=internship",
        "https://www.simplyhired.com.au/search?q=computer+science&jt=internship",
        "https://za.simplyhired.com/search?q=computer+science&jt=internship",
        "https://www.simplyhired.ie/search?q=computer+science&jt=internship",
        "https://www.simplyhired.co.uk/search?q=computer+science&jt=internship",
        "https://www.simplyhired.ca/search?q=computer+science&jt=internship",
        "https://www.simplyhired.com/search?q=computer+science&jt=internship"
        ]

    # Going on each url and getting each page
    def parse(self,response) :

        try :
            number_of_posts = len(response.css('.jobposting-title a::attr(href)').getall())
            if response.url == "https://www.simplyhired.com/search?q=computer+science&jt=internship" :
                number_of_pages = (int(response.css(".CategoryPath-total::text").get().replace(',','')) // int(number_of_posts)) + 1
            else :
                number_of_pages = (int(response.css(".posting-total::text").get().replace(',','')) // int(number_of_posts)) + 1
            for i in range(1,number_of_pages + 1) :
                yield scrapy.Request(url = f"{response.url}&pn={i}",callback = self.parse_page)
        except Exception as e :
            career_site_logger.error(e)

    # Going on each page and getting each post
    def parse_page(self,response) :

        try :
            posts = response.css('.jobposting-title a::attr(href)').getall()
            url = str(response.url.split('/')[2])
            for post in posts :
                yield scrapy.Request(url = f"https://{url}{post}",callback = self.parse_post)
        except Exception as e :
            career_site_logger.error(e)

    # Going on each post and getting the data from it
    def parse_post(self,response) :

        try :
            title = response.css('.viewjob-jobTitle::text').get()
            company_and_location = response.css('.viewjob-labelWithIcon::text').getall()
            company = company_and_location[0]
            location = company_and_location[-1]
            if '$' in location :
                location = company_and_location[-2]
            if ':' in location :
                location = company_and_location[-3]

            # Storing the data in internship item
            posting = InternshipPosting()
            posting['role'] = title.replace("'","")
            posting['company_name'] = company.replace("'","")
            posting['location'] = location
            posting['start_date'] = ""
            posting['stipendmin'] = 0
            posting['stipendmax'] = 0
            posting['deadline'] = ""
            posting['link'] = response.url
            posting['number_of_applicants'] = 0
            posting['posting_date'] = ""
            posting['category_id'] = 0
            yield posting
        except Exception as e :
            career_site_logger.error(e)