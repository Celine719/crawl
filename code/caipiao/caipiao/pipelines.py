# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
from pymongo import MongoClient
import csv
class CaipiaoPipeline:

    # def open_spider(self,spider):
    #     self.f = open("./双色球.csv",mode="a", encoding="utf-8")
    # def close_spider(self,spider):
    #     if self.f:
    #         self.f.close()
    def process_item(self, item, spider):
        with open("./双色球.csv", mode="a", newline='', encoding="utf-8") as f:  # 一次写一条   项目的根目录
            writer = csv.writer(f)
            writer.writerow([item['date'][0], '_'.join(item['red_ball']), item['blue_ball']])  #  红球列表需要拼接

        return item

# class CaipiaoPipeline_mongo:
#
#     def open_spider(self,spider):
#         self.client = MongoClient()
#         db = self.client['crawl']  # db.authenticate(用户名，密码) 资格认证
#         self.sheet = db["caipiao"]
#     def close_spider(self,spider):
#         self.client.close()
#
#     def process_item(self, item, spider):
#         # with open("./双色球.csv", mode= "a", encoding = "utf-8") as f:  一次写一条   项目的根目录
#         # f.write(f"{item['date']},{'_'.join(item[red_ball])},{item['red_ball']}) 红球列表需要拼接
#         self.sheet.insert_one({"qihao":item["date"],"red_ball": item["red_ball"],"blue_ball": item["blue_ball"]})
#         return item
