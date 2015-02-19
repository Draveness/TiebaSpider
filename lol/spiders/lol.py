from __future__ import absolute_import
from scrapy.spider import Spider
from scrapy.selector import Selector

from lol.items import LolItem


class LolSpider(Spider):
    name = "lol"
    allowed_domains = ["tieba.baidu.com"]
    start_urls = [
        "http://tieba.baidu.com/f?kw=lol&fr=index",
    ]

    def parse(self, response):
        sel = Selector(response)
        sites = sel.xpath('//ul[@id="thread_list"]/li[@class="j_thread_list clearfix"]')
        items = []

        for site in sites:
            item = LolItem()
            item['author'] = site.xpath('div[@class="t_con cleafix"]/div[@class="threadlist_li_right j_threadlist_li_right"]/div[@class="threadlist_lz clearfix"]/div[@class="threadlist_author"]/span[@class="tb_icon_author "]/a/text()').extract()
            item['counts'] = site.xpath('div[1]/div[1]/div/text()').extract()
            item['title']  = site.xpath('div[@class="t_con cleafix"]/div[@class="threadlist_li_right j_threadlist_li_right"]/div[@class="threadlist_lz clearfix"]/div[@class="threadlist_text threadlist_title j_th_tit  "]/a/text()').extract()
            items.append(item)
        return items
