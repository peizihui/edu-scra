# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from eduscra.items import EduscraItem


class EduSpider(CrawlSpider):
    name = 'edu'
    allowed_domains = ['hao123.com']
    start_urls = ['http://www.hao123.com/edu/']

    rules = (
        Rule(LinkExtractor(allow=r'/eduhtm/'), callback='parse_item', follow=True),
    )

    def parse_item(self, response):
        p = response.xpath("//tr/td/font/text()").extract_first()
        ps = p.split()
        region = ps[0]
        kind = ps[1]
        links = response.xpath("//tr/td/p/a")
        print p, "get %d" % len(links)
        for link in links:
            url = link.xpath("@href").extract_first()
            name = link.xpath("text()").extract_first()
            yield EduscraItem(name=name, url=url, region=region, kind=kind)

