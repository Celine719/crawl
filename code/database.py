from pymongo import MongoClient
from lxml import etree   # 正则表达式，进行文字匹配`
import requests

# MongoDB是一个高性能，开源，**无模式的文档型数据库 **:简单讲就是可以直接存json,list
# MongoDB 将数据存储为一个文档，数据结构由键值(key=>value)对组成
# MongoDB 是一个基于分布式文件存储的数据库是一个介于关系数据库和非关系数据库之间的产品，是非关系数据库当中功能最丰富，最像关系数据库的。


def get_page(url, headers):
    response = requests.get(url=url, headers=headers)
    if response.status_code == 200:
        # print(response.text)
        return response.text
    return None


url_data = "https://movie.douban.com/top250?start="
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 "
                  "Safari/537.36 Edg/112.0.1722.34"
}
tree = etree.HTML(get_page(url_data, headers))
li_data = tree.xpath("//ol[@class = 'grid_view']/li")
id = li_data[0].xpath("//div[@class = 'pic']/em/text()")
print(id)
name = li_data[0].xpath("//div[@class = 'hd']/a/span[@class = 'title'][1]/text()")
print(name)  # 中文名字
# 连接数据库，为空默认IP为localhost，端口为27017
# client = MongoClient() / client = MongoClient("localhost", 27107) / client = MongoClient("mongodb://localhost:27017/")

# client = MongoClient()
# db = client.test  # 连接test数据库，没有则自动创建(选择数据库)
# my_set = db["set"]  # 使用set集合，没有则自动创建(选择集合)
# my_set.insert_one({'name': 'Robin', 'age': '24'})  # 插入一条数据

client = MongoClient()
db = client.movice
my_set = db["set"]
for i in range(25):
    my_set.insert_one({'id': id[i], "name": name[i]})



