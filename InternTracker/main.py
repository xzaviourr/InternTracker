import scrapy
from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings

from concurrent.futures import ProcessPoolExecutor
from concurrent.futures import as_completed

from InternTracker.spiders.internshala import *
from InternTracker.spiders.letsintern import *
from InternTracker.spiders.google import *
from InternTracker.spiders.microsoft import *

from Database.database import create_database

create_database()

process = CrawlerProcess(settings=get_project_settings())
process.crawl(Internshala)
process.crawl(LetsIntern)
process.crawl(Google)
process.crawl(Microsoft)
process.start()
