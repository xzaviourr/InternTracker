# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class InternshalaItem(scrapy.Item):
    role = scrapy.Field()
    company = scrapy.Field()
    location = scrapy.Field()
    start_date = scrapy.Field()
    duration = scrapy.Field()
    stipendmin = scrapy.Field()
    stipendmax = scrapy.Field()
    deadline = scrapy.Field()
    link = scrapy.Field()
    pass

class LetsInternItem(scrapy.Item):
    job_no=scrapy.Field()
    role = scrapy.Field()
    company = scrapy.Field()
    location = scrapy.Field()
    start_date = scrapy.Field()
    end_date=scrapy.Field()
    deadline=scrapy.Field()
    stipendmin = scrapy.Field()
    stipendmax = scrapy.Field()
    link=scrapy.Field()
    pass

# Unified item to be used for storing data instead of the previous created ones

class DatabaseItem(scrapy.Item) :

    internship_id = scrapy.Field()
    company_id = scrapy.Field()
    start_date = scrapy.Field()
    deadline = scrapy.Field()
    stipend = scrapy.Field()
    number_of_applicants = scrapy.Field()
    posting_date = scrapy.Field()
    role = scrapy.Field()
    category_id = scrapy.Field()
    pass