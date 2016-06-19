from scrapy.spiders import Spider
from scrapy.selector import Selector

class letsbegin(Spider):
    name="letsbegin"
    allowed_domains=['https://www.fresherslive.com']
    start_urls=[
            "https://www.fresherslive.com/off-campus-jobs-in-india",
        ]

    def parse(self,response):
        filename = response.url.split("/")[-2] + '.html'
        with open(filename, 'wb') as f:
            f.write(response.body)
