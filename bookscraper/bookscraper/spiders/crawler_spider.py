from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor

class spider(CrawlSpider):
  name = 'mySpider'
  allowed_domains = ['toscrape.com']
  start_urls = ['https://books.toscrape.com/']

  rules=(    
    Rule(LinkExtractor(allow= 'catalogue/category')),
    Rule(LinkExtractor(allow= 'catalogue', deny='category'), callback= 'get_items'),        
  )

  def get_items(self, response):
    yield{
      'name': response.css('.product_main h1::text').get(),
      'price': response.css('.price_color::text').get(),
      'rating ': response.css(' p.star-rating').attrib['class'],
      'category': response.css('.breadcrumb li a::text')[2].get()
    }

