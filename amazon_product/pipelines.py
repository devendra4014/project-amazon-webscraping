# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter


import mysql.connector

class SaveToMySQLPipeline:

    def __init__(self):
        self.conn = mysql.connector.connect(
            host = 'localhost',
            user = 'root',
            password = '', #add your password here if you have one set 
            database = 'amazon'
        )

        ## Create cursor, used to execute commands
        self.cur = self.conn.cursor()

        ## Create books table if none exists
        self.cur.execute("""
        CREATE TABLE IF NOT EXISTS product(
            id int NOT NULL auto_increment, 
            asin INTERGER,
            url VARCHAR(255),
            title text,
            keyword VARCHAR(255),
            price VARCHAR(10),
            rating_count INTEGER,
            rating INTEGER,
            thumbnail_url VARCHAR(255)
            PRIMARY KEY (id)
        )
        """)

    def process_item(self, item, spider):

        ## Define insert statement
        self.cur.execute(""" insert into product (
            id, 
            asin, 
            url,
            title, 
            keyword, 
            price,
            rating_count,
            rating,
            thumbnail_url
            ) values (
                %s,
                %s,
                %s,
                %s,
                %s,
                %s,
                %s,
                %s,
                %s,
                )""", (
            item["id"],
            item["asin"],
            item["url"],
            item["title"],
            item["keyword"],
            item["price"],
            item["rating_count"],
            item["rating"],
            item["thumbnail_url"],
            
        ))

        # ## Execute insert of data into database
        self.conn.commit()
        return item

    
    def close_spider(self, spider):

        ## Close cursor & connection to database 
        self.cur.close()
        self.conn.close()
