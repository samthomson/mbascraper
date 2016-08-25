import scrapy


from mbascraper.items import MbascraperItem

def first_or_null(list):
    try:
        return list[0]
    except IndexError:
        return None

def substring_after(s, delim):
    return s.partition(delim)[2]

class DmozSpider(scrapy.Spider):
    name = "mba"
    allowed_domains = ["www.mountainbothies.org.uk"]
    
    '''
    start_urls = [
        "http://www.mountainbothies.org.uk/region.asp?region_id=1"
    ]
    '''
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
            
            item['link'] = first_or_null(sel.xpath('a/@href').extract())

            item['bothy_id'] = substring_after(item['link'], '=')
            
            url = sel.xpath('a/@href').extract() 
            url = response.urljoin(first_or_null(url))

            yield scrapy.Request(url, meta = {'item': item}, callback=self.parse_bothy_page)

    def parse_bothy_page(self, response):

        item = response.meta['item']
        
        #item['name'] = response.xpath('//div[@id="content-left"]/h1/text()').extract()


        
        #item['gridref'] = response.xpath('//div[@id="content-left"]/p/strong[1]/text()').extract()
        #item['location'] = response.xpath('//div[@id="content-left"]/p/strong[2]/text()').extract()
        #print item['name'], item['link']
        #print response.Request.url

        item['name'] = first_or_null(response.xpath('//div[@id="content-left"]/h1/text()').extract())

        

        s_gridref = first_or_null(response.xpath('//div[@id="content-left"]/p/strong[1]/text()').extract())
        if s_gridref is not None:
            # parse out what we want
            i_pos = s_gridref.find(":")
            i_start = i_pos + 1
            i_end = i_start + 10
            s_gridref = s_gridref[i_start:i_end].replace(" ", "")

        item['gridref'] = s_gridref

        item['region'] = first_or_null(response.xpath('//div[@id="content-left"]/p/strong[2]/text()').extract())

        item['description'] = first_or_null(response.xpath('//div[@id="content-left"]/p[2]/text()').extract())


        a_images = []

        for image in response.xpath('//div[@id="bothy-gallery"]/a'):

            img = first_or_null(image.xpath('img/@src').extract())

            if img is not None:
                a_images.append(img)

        item['images'] = a_images
        #item['images'] = 'images'#a_images

        yield item


