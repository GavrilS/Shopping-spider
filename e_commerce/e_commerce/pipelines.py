# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
# from itemadapter import ItemAdapter
import os
from dotenv import load_dotenv
import psycopg2

class ECommercePipeline:

    def __init__(self) -> None:
        load_dotenv()
        self.db_user = os.getenv('DB_USER')
        self.db_pass = os.getenv('DB_PASS')
        self.db_host = os.getenv('DB_HOST')
        self.db_port = os.getenv('DB_PORT')
        self.db_name = os.getenv('DB_NAME')
        self.create_connection()

    def create_connection(self):
        try:
            self.conn = psycopg2.connect(
                database=self.db_name,user=self.db_user,password=self.db_pass,host=self.db_host,port=self.db_port
            )
            self.cursor = self.conn.cursor()
        except Exception as e:
            print("Error connecting to db ^^^^^^^^^^^^^^^^^^^^")
            print(e)
            exit()

    def close_connection(self):
        try:
            self.cursor.close()
            self.conn.close()
        except Exception as e:
            print("Closing connection exception ^^^^^^^^^^^^^^^^^^^^")
            print(e)

    def save_db_item(self, elem):
        user_id = elem['user']
        search_term = elem['search']
        product_name = elem['product_name']
        product_link = elem['product_link']
        product_price = elem['product_price']
        date = elem['date']
        brand = elem['brand']
        site = elem['site']
        query = f"""INSERT INTO items(user_id, search_term, product_name, product_link, product_price, date, brand, site)
            VALUES({user_id}, {search_term}, {product_name}, {product_link}, {product_price}, {date}, {brand}, {site}) RETURNING item_id;"""
        
        self.cursor.execute(query)
        item_id = self.cursor.fetchone()[0]
        
        print(item_id)

    def process_item(self, item, spider):
        for elem in item:
            self.save_db_item(elem)
        
        self.conn.commit()
        self.close_connection()
