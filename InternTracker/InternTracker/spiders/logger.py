import logging

#For LetsIntern
# Create a custom logger
letsintern_logger = logging.getLogger(__name__)
# Create handlers
letsintern_handler = logging.FileHandler('letsintern_logger.log')
letsintern_handler.setLevel(logging.ERROR)
# Create formatters and add it to handlers
letsintern_format = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
letsintern_handler.setFormatter(letsintern_format)
# Add handlers to the logger
letsintern_logger.addHandler(letsintern_handler)

#For InternShala
# Create a custom logger
internshala_logger = logging.getLogger(__name__)
# Create handlers for internshala
internshala_handler = logging.FileHandler('internshala_logger.log')
internshala_handler.setLevel(logging.ERROR)
# Create formatters and add it to handlers for internshala
internshala_format = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
internshala_handler.setFormatter(internshala_format)
# Add handlers to the logger for internshala
<<<<<<< HEAD
internshala_logger.addHandler(internshala_handler) 

# This logger has been currently moved to database/logger.py

# Database logger and handler
# db_logger = logging.getLogger(__name__)
# db_handler = logging.FileHandler('db_logger.log')
# db_handler.setLevel(logging.ERROR)
# db_format = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
# db_handler.setFormatter(db_format)
# db_logger.addHandler(db_handler)
=======
internshala_logger.addHandler(internshala_handler)

 
>>>>>>> ebe46b8b7bb200c40baf4c2f57d5c7102bf92877
