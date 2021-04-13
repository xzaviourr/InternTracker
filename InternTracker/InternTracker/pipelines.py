from itemadapter import ItemAdapter
from scrapy.exporters import CsvItemExporter
import psycopg2
from Database.connection import Database
from Logger.logger import db_logger
import time

class InterntrackerPipeline:
    def process_item(self, item, spider):
        return item

class CsvPipeline(object):
    """
    Stores each yielded item into csv file
    """
    def __init__(self):
        #self.file = open("InternTracker/spiders/csv_files/internship_data.csv", 'wb')
        self.file = open("internship_data.csv", 'wb')
        self.exporter = CsvItemExporter(self.file)
        self.exporter.start_exporting()

    def close_spider(self, spider):
        self.exporter.finish_exporting()
        self.file.close()

    def process_item(self, item, spider):
        self.exporter.export_item(item)
        return item

class DatabasePipeline(object) :

    def open_spider(self,spider) :
        
        self.obj = Database()
        while True:
            try:
                self.conn = self.obj.connect()
                break
            except Exception:
                db_logger.info("Waiting 2 seconds before retrying ...")
                time.sleep(2)
        self.cur = self.conn.cursor()
    
    def close_spider(self,spider) :

        self.cur.close()
        self.conn.close()
    
    def process_item(self,item,spider) :

        try:
            self.cur.execute(f"""INSERT INTO internships(internship_id,company_name,start_date,deadline,stipend_min,stipend_max,number_of_applicants,posting_date,role,category_id,link,location) VALUES (nextval('internships_internship_id_seq'),
            '{item['company_name']}',
            '{item['start_date']}',
            '{item['deadline']}',
            {int(item['stipendmin'])},
            {int(item['stipendmax'])},
            {int(item['number_of_applicants'])},
            '{item['posting_date']}',
            '{item['role']}',
            {int(item['category_id'])},
            '{item['link']}',
            '{item['location']}')""")
            self.conn.commit()
        except Exception as e:
            db_logger.error(e)
        
        return item