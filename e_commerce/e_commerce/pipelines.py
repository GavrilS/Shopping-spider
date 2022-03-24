# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
# from itemadapter import ItemAdapter
import psycopg2

class ECommercePipeline:

    def __init__(self) -> None:
        self.create_connection()

    def create_connection(self):
        try:
            self.conn = psycopg2.connect(
                database='',user='',password='',host='',port=''
            )
            self.cursor = self.conn.cursor()
        except Exception as e:
            print("Error connecting to db ^^^^^^^^^^^^^^^^^^^^")
            print(e)
            exit()

    def close_connection(self):
        self.conn.close()

    def process_item(self, item, spider):
        return item
