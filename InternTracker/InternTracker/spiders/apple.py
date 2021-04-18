import scrapy
from scrapy import Spider
from scrapy.selector import Selector
from scrapy.http import TextResponse as response
from InternTracker.items import InternshipPosting
from Logger.logger import career_site_logger

def dateformat(date) :

    date = date.replace(",","").split(" ")
    months = {'Jan':'01','Feb':'02','Mar':'03','Apr':'04','May':'05','Jun':'06','Jul':'07','Aug':'08','Sept':'09','Oct':'10','Nov':'11','Dec':'12'}
    if len(date[1]) == 1 :
        date[1] = '0' + date[1]
    correct = date[1] + '-' + months[date[0]] + '-' + date[2]
    return correct

class Apple(scrapy.Spider) :

    name = "apple_spy"
    # allowed_domains = []
    start_urls = ['https://jobs.apple.com/en-us/search?sort=relevance&key=engineering&team=internships-STDNT-INTRN']

    # Getting total number of pages and then going on each page
    def parse(self,response) :
        
        try :
            number_of_pages = (int(response.css('#resultCount span::text').get().split()[0]) // 20) + 1
            for i in range(1,number_of_pages + 1) :
                yield scrapy.Request(url = f"https://jobs.apple.com/en-us/search?sort=relevance&key=engineering&team=internships-STDNT-INTRN&page={str(i)}",callback = self.parse_page)
        except Exception as e :
            career_site_logger.error(e)

    # Getting each posting on every page
    def parse_page(self,response) :
        
        try :
            posts = response.css('.table--advanced-search__title::attr(href)').getall()
            for post in posts :
                yield scrapy.Request(url = f"https://jobs.apple.com{str(post)}",callback = self.parse_post)
        except Exception as e :
            career_site_logger.error(e)

    # Going into every post and then processing the data from it
    def parse_post(self,response) :

        try :
            role = response.css('#jdPostingTitle::text').get()
            locations = response.css('#job-location-name span::text').getall()
            location = ""
            for loc in locations :
                location += loc
            posting_date = response.css('#jobPostDate::text').get()
            post_id = response.css('#jobNumber::text').get()
            
            # Storing all the data in internship item
            posting = InternshipPosting()
            posting['role'] = role.strip()
            posting['company_name'] = "Apple"
            posting['location'] = location
            posting['start_date'] = ""
            posting['stipendmin'] = 0
            posting['stipendmax'] = 0
            posting['deadline'] = ""
            posting['link'] = f"https://jobs.apple.com/en-us/details/{str(post_id)}"
            posting['number_of_applicants'] = 0
            posting['posting_date'] = dateformat(posting_date)
            posting['category_id'] = 0
            yield posting
        except Exception as e :
            career_site_logger.error(e)