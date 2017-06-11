# -*- coding: utf-8 -*-

import scrapy


class ProxyItem(scrapy.Item):
    protocol = scrapy.Field()
    address = scrapy.Field()
    port = scrapy.Field()


class AmazonItem(scrapy.Item):
    # define the fields for your item here like:
    product_name = scrapy.Field()
    product_sale_price = scrapy.Field()
    product_category = scrapy.Field()
    product_original_price = scrapy.Field()
    product_availability = scrapy.Field()
