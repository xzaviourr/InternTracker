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
    role = scrapy.Field()
    company = scrapy.Field()
    location = scrapy.Field()
    start_date = scrapy.Field()
    stipend = scrapy.Field()
    pass