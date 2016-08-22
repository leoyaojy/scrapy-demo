# -*- coding: utf-8 -*-
from scrapy.spider import CrawlSpider
from scrapy.http import Request
from mzt.items import MztItem

class MeizituSpider(CrawlSpider):
    name = "meizitu"
    start_urls = ['http://www.mzitu.com/']

    def parse(self, response):
        exp = u'//div[@class="nav-links"]//a[text()="下一页»"]/@href'
        next_page = response.xpath(exp).extract_first()
        yield Request(next_page, callback=self.parse)
        for p in response.xpath('//ul[@id="pins"]//a/@href').extract():
            yield Request(p, callback=self.parse_item)

    def parse_item(self, response):
        item=MztItem()
        urls = response.xpath("//div[@class='main-image']//img/@src").extract()
        item['image_urls'] = urls
        return item