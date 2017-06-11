#!/usr/bin/python

import sys
import os.path
from twisted.internet import reactor, defer
from scrapy.crawler import CrawlerRunner
from scrapy.utils.log import configure_logging
from scrapy.utils.project import get_project_settings
from spiders.iptester import IPTesterSpider
from spiders.uatester import UATesterSpider
from spiders.amazonSpider import AmazonProductSpider
sys.path.append('/spiders/')

configure_logging()
# importing project settings for further usage
# mainly because of the middlewares
settings = get_project_settings()
runner = CrawlerRunner(settings)


# running spiders sequentially (non-distributed)
@defer.inlineCallbacks
def crawl():
    yield runner.crawl(IPTesterSpider)
    yield runner.crawl(UATesterSpider)
    yield runner.crawl(AmazonProductSpider)
    reactor.stop()


crawl()
reactor.run()  # block until the last call
