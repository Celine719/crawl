# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter

import csv
class WangyiPipeline:
    def process_item(self, item, spider):
        with open("./news.csv", mode="a", newline='', encoding="utf-8") as f:  # 一次写一条   项目的根目录
            writer = csv.writer(f)
            writer.writerow([item['title'], item["info"]])
        print(item['title'])
        return item
