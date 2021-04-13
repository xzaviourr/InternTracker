# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy

# Unified item to be used for storing data in the database

class InternshipPosting(scrapy.Item) :

    company_name = scrapy.Field()
    start_date = scrapy.Field()
    deadline = scrapy.Field()
    stipendmin = scrapy.Field()
    stipendmax = scrapy.Field()
    number_of_applicants = scrapy.Field()
    posting_date = scrapy.Field()
    role = scrapy.Field()
    category_id = scrapy.Field()
    link = scrapy.Field()
    location = scrapy.Field()
    pass

class DunzoItem(scrapy.Item):
    link = scrapy.Field()
    role = scrapy.Field()
    requirements = scrapy.Field()
    responsibilities = scrapy.Field()
    pass