import scrapy
from scrapy.crawler import CrawlerProcess

from concurrent.futures import ProcessPoolExecutor
from concurrent.futures import as_completed

from InternTracker.spiders.internshala import *
from InternTracker.spiders.letsintern import *

process = CrawlerProcess()

process.crawl(Internshala)
process.crawl(LetsIntern)
process.start()