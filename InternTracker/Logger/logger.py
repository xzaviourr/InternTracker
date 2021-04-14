import logging

#For normal_site
# Create a custom logger
# import sys
# sys.path.append(InternTracker\Logger\logger.py)

normal_site_logger = logging.getLogger(__name__)
# Create handlers
normal_site_handler = logging.FileHandler('Logger/normal_site_logger.log')
normal_site_handler.setLevel(logging.ERROR)
# Create formatters and add it to handlers
normal_site_format = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
normal_site_handler.setFormatter(normal_site_format)
# Add handlers to the logger
normal_site_logger.addHandler(normal_site_handler)

#For career_site
# Create a custom logger
career_site_logger = logging.getLogger(__name__)
# Create handlers for career_site
career_site_handler = logging.FileHandler('Logger/career_site_logger.log')
career_site_handler.setLevel(logging.ERROR)
# Create formatters and add it to handlers for career_site
career_site_format = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
career_site_handler.setFormatter(career_site_format)
# Add handlers to the logger for career_site
career_site_logger.addHandler(career_site_handler) 

#Database logger and handler
db_logger = logging.getLogger(__name__)
db_handler = logging.FileHandler('Logger/db_logger.log')
db_handler.setLevel(logging.ERROR)
db_format = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
db_handler.setFormatter(db_format)
db_logger.addHandler(db_handler)