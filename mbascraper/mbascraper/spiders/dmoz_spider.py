import scrapy


from mbascraper.items import MbascraperItem


class DmozSpider(scrapy.Spider):
    name = "mba"
    allowed_domains = ["www.mountainbothies.org.uk"]
    start_urls = [
        "http://www.mountainbothies.org.uk/region.asp?region_id=1",
        "http://www.mountainbothies.org.uk/region.asp?region_id=2",
        "http://www.mountainbothies.org.uk/region.asp?region_id=3",
        "http://www.mountainbothies.org.uk/region.asp?region_id=4",
        "http://www.mountainbothies.org.uk/region.asp?region_id=5",
        "http://www.mountainbothies.org.uk/region.asp?region_id=6",
        "http://www.mountainbothies.org.uk/region.asp?region_id=7",
        "http://www.mountainbothies.org.uk/region.asp?region_id=8",
        "http://www.mountainbothies.org.uk/region.asp?region_id=9"
    ]

    def parse(self, response):
        for sel in response.xpath('//div[@id="content-left"]/ul/li'):
            
            item = MbascraperItem()
            
            item['link'] = sel.xpath('a/@href').extract()
            
            url = sel.xpath('a/@href').extract() 
            url = response.urljoin(url[0])

            yield scrapy.Request(url, meta = {'item': item}, callback=self.parse_bothy_page)

    def parse_bothy_page(self, response):

        item = response.meta['item']
        
        #item['name'] = response.xpath('//div[@id="content-left"]/h1/text()').extract()


        
        #item['gridref'] = response.xpath('//div[@id="content-left"]/p/strong[1]/text()').extract()
        #item['location'] = response.xpath('//div[@id="content-left"]/p/strong[2]/text()').extract()
        #print item['name'], item['link']
        #print response.Request.url

        item['name'] = response.xpath('//div[@id="content-left"]/h1/text()').extract()

        item['gridref'] = response.xpath('//div[@id="content-left"]/p/strong[1]/text()').extract()
        item['location'] = response.xpath('//div[@id="content-left"]/p/strong[2]/text()').extract()


        yield item
        #print item
        #print response.request.url