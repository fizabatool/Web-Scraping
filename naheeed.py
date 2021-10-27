import scrapy

from scrapy.spiders import Spider
class nah(scrapy.Spider):
    name="hehe"
    start_urls=['https://www.naheed.pk/phones-tablets/smartphones']

    def parse(self,response):
        for prod in response.css('.product.details.product-item-details.products-textlink'):
            yield{
                'name':prod.css('a.product-item-link::text').get(),
                'price':prod.css('span.price::text').get().replace('Rs.',""),
                'link': prod.css('a.product-item-link').attrib['href'],
            }