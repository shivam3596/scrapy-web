import scrapy
from scrapy.crawler import CrawlerProcess
from scrapy.spiders import Spider
from scrapy.selector import Selector
from scrapy.http import HtmlResponse
from twisted.internet import reactor

class letsbegin(Spider):
    name="letsbegin"
    allowed_domains=['http://apuzz.com']
    start_urls=[
            "http://apuzz.com/category/off-campus/",
        ]

    def parse(self,response):
        target= response.xpath('//div[@class="td-ss-main-content"]')
        fo= open( "apuzz.com.csv", "wb")
        for p in target.xpath('.//text()'):
            fo.write(p.extract())
            
class secondspider(Spider):
    name="second spider"
    allowed_domains=['https://www.fresherslive.com']
    start_urls=[
            "https://www.fresherslive.com/off-campus-jobs-in-india",
        ]

    def parse(self,response):
        target= response.xpath('//div[@class="datagrid"]')
        fo1= open( "fresherslive.com.csv", "wb")
        for p in target.xpath('.//text()'):
            fo1.write(p.extract())

			
process = CrawlerProcess()
process.crawl(letsbegin)
process.crawl(secondspider)
process.start()

