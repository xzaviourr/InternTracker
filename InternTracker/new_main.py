import scrapy
from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings
from concurrent.futures import ProcessPoolExecutor
from concurrent.futures import as_completed
from scrapy import spiderloader
from scrapy.utils import project
from Database.database import create_database

# Create the database if not created
# create_database()

# Get all the spiders
settings = project.get_project_settings()
spider_loader = spiderloader.SpiderLoader.from_settings(settings)
spiders_list = spider_loader.list()
spiders = [spider_loader.load(spider) for spider in spiders_list]

# Run the spiders
process = CrawlerProcess(settings = settings)
for spider in spiders :
    process.crawl(spider)
process.start()