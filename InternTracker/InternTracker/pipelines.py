# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
from scrapy.exporters import CsvItemExporter
import psycopg2
from connection import obj

class InterntrackerPipeline:
    def process_item(self, item, spider):
        return item

# class CsvPipeline(object):
#     """
#     Stores each yielded item into csv file
#     """
#     def __init__(self):
#         self.file = open("internship_data.csv", 'wb')
#         self.exporter = CsvItemExporter(self.file)
#         self.exporter.start_exporting()

#     def close_spider(self, spider):
#         self.exporter.finish_exporting()
#         self.file.close()

#     def process_item(self, item, spider):
#         self.exporter.export_item(item)
#         return item

class DatabasePipeline(object) :

    def open_spider(self,spider) :

        self.conn = obj.connect()
        self.cur = self.conn.cursor()
    
    def close_spider(self,spider) :

        self.cur.close()
        self.conn.close()
    
    def process_item(self,item,spider) :

        self.cur.execute("""INSERT INTO Internships VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)""",("nextval('internships_internship_id_seq')",item['company_name'],item['start_date'],item['deadline'],item['stipendmin'],item['stipendmax'],item['number_of_applicants'],item['posting_date'],item['role'],item['category_id'],item['link'],item['location']))
        self.conn.commit()
        return item