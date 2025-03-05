import scrapy
from caipiao.items import CaipiaoItem

class SsqSpider(scrapy.Spider):
    name = "ssq"
    allowed_domains = ["500.com"]
    start_urls = ["https://datachart.500.com/ssq/"]

    def parse(self, resp):
        trs = resp.xpath("//tbody[@id='tdata']/tr")

        for tr in trs:  # 支持xpath和css混合使用
            if tr.xpath("./@class").extract_first() == "tdbck":
                continue
            red_ball = tr.xpath("./td[@class='chartBall01']/text()").extract()
            blue_ball = tr.xpath("./td[@class='chartBall02']/text()").extract_first()
            date = tr.xpath("./td[@align='center']/text()").extract()
            cai = CaipiaoItem()  # 定义了一个字典
            cai["date"] = date
            cai["red_ball"] = red_ball
            cai["blue_ball"] = blue_ball
            yield cai
        # all_data = []
        # for tr in trs:  # 支持xpath和css混合使用
        #     if tr.xpath("./@class").extract_first() == "tdbck":
        #         continue
        #     red_ball = tr.xpath("./td[@class='chartBall01']/text()").extract()
        #     blue_ball = tr.xpath("./td[@class='chartBall02']/text()").extract_first()
        #     date = tr.xpath("./td[@align='center/text()']").extract()
        #     dic = {
        #         "red_ball": red_ball,
        #         "blue_ball": blue_ball,
        #         "date": date}
        #     all_data.append(dic)
        # return
