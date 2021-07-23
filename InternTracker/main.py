# Use this main.py for testing purposes only otherwise use new_main.py

import scrapy
import sys,os
from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings

from concurrent.futures import ProcessPoolExecutor
from concurrent.futures import as_completed

from InternTracker.spiders.internshala import *
from InternTracker.spiders.letsintern import *
from InternTracker.spiders.google import *
# from InternTracker.spiders.microsoft import *
# from InternTracker.spiders.hellointern import *
# from InternTracker.spiders.apple import *
# from InternTracker.spiders.uber import *
# from InternTracker.spiders.qualcomm import *
# from InternTracker.spiders.indeed import *
# from InternTracker.spiders.wayup import *
# from InternTracker.spiders.ycombinator import *
# from InternTracker.spiders.makeintern import *
# from InternTracker.spiders.simplyhired import *
from Database.database import create_database

#create_database()
print("****************PATH ****************")
PATH = os.path.dirname(os.path.abspath(__file__))
if PATH not in sys.path:
    sys.path.append(PATH)
print(os.path.dirname(os.path.abspath(__file__)))
process = CrawlerProcess(settings=get_project_settings())
# process.crawl(Internshala)
# process.crawl(LetsIntern)
# process.crawl(Google)
# process.crawl(Microsoft)
# process.crawl(Hellointern)
# process.crawl(Apple)
# process.crawl(Uber)
# process.crawl(Qualcomm)
# process.crawl(Indeed)
# process.crawl(Wayup)
# process.crawl(Ycombinator)
# process.crawl(Makeintern)
# process.crawl(SimplyHired)
process.start()
