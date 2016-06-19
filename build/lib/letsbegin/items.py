# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy
from letsbegin import settings
import csv

class LetsbeginItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
        title  = scrapy.Field()
    body = scrapy.Field()
    link = scrapy.Field()
    desc = scrapy.Field()
    pass


def write_to_csv(item):
        writer = csv.writer(open(settings.csv_file_path, 'a'), lineterminator='\n')
        writer.writerow([item[key] for key in item.keys()])

class WriteToCsv(object):
        def process_item(self, item, spider):
                write_to_csv(item)
                return item
