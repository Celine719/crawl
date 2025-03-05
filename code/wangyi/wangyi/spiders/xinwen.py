import scrapy
from selenium import webdriver
from wangyi.items import WangyiItem
from selenium.webdriver.chrome.service import Service

class XinwenSpider(scrapy.Spider):
    name = "xinwen"
    # allowed_domains = ["news.163.com"]
    start_urls = ["http://news.163.com/"]
    model_urls = []
    # 解析五大板块详细页面url
    # 实例化浏览器对象
    def __init__(self):
        s = Service("E:/download/chromedriver-win64/chromedriver-win64/chromedriver.exe")
        self.bro = webdriver.Chrome()

    def parse(self, response):
        li_list = response.xpath("//*[@id='index2016_wrap']/div[3]/div[2]/div[2]/div[2]/div/ul/li")
        a_list = [1, 2]
        for index in a_list:
            model_url = li_list[index].xpath("./a/@href").extract_first()
            self.model_urls.append(model_url)


        for url in self.model_urls:
            yield scrapy.Request(url, callback=self.parse_model)

    def parse_model(self, response):  # 用来解析每一个板块的标题和对应url，注意是动态加载的
        div_list = response.xpath("/html/body/div/div[3]/div[3]/div[1]/div[1]/div/ul/li/div/div")
        for div in div_list:
            title = div.xpath("./div/div[1]/h3/a/text()").extract_first()
            new_info_url = div.xpath("./div/div[1]/h3/a/@href").extract_first()
            item = WangyiItem()
            item["title"] = title

            # 对新闻详细url发送请求
            yield scrapy.Request(new_info_url, callback=self.parse_info, meta={"item": item})

    def parse_info(self, response):  # 解析新闻内容
        content = response.xpath("//*[@id='content']/div[2]//text()").extract()  # 获取所有文本内容
        content = "".join(content)
        item = response.meta["item"]
        item["info"] = content
        yield item

    def close(self, spider):
        self.bro.quit()

