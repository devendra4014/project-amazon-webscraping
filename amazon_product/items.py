# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class AmazonProductItem(scrapy.Item):
    # define the fields for your item here like:
    keyword = scrapy.Field()
    asin = scrapy.Field()
    url = scrapy.Field()
    title = scrapy.Field()
    price = scrapy.Field()
    rating = scrapy.Field()
    rating_count = scrapy.Field()
    thumbnail_url = scrapy.Field()
    
