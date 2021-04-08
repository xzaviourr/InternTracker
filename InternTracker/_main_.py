import scrapy
from scrapy.crawler import CrawlerProcess
from InternTracker.spiders.internshala import *
from InternTracker.spiders.letsintern import *

process = CrawlerProcess()

process.crawl(Internshala)
process.start()

process.crawl(LetsIntern)
process.start()