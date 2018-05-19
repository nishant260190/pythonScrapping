import scrapy

class flipkartScrapy(scrapy.Spider):
    name = "flipkart"
    print("inside flipkartScrapy");
    def start_requests(self):
        urls = ["https://www.flipkart.com/men/tshirts/pr?sid=2oq,s9b,j9y&otracker=undefined_footer_footer"];
        for url in urls:
            print(url);
            yield scrapy.Request(url = url, callback=self.parse);


    def parse(self, response):
        print("inside parse method");
        for product in response.xpath('//div[@class="MP_3W3 _31eJXZ"]'):
            yield {
                'title' : product.css('a._2cLu-l::attr(title)').extract_first(),
                'url' : product.css('a._2cLu-l::attr(href)').extract_first(),
                'list_price' : product.css('div._1vC4OE::text').extract_first(),
                'final_price' : product.css('div._3auQ3N').extract_first(),
            }
                
        print("------------ next page ------------------");
        next_page = response.css('div._2kUstJ a::attr(href)').extract();
        print(next_page[-1]);
        if next_page is not None:
            next_page = response.urljoin(next_page[-1])
            yield scrapy.Request(next_page, callback=self.parse)


print("start")
#x = flipkartScrapy();
#x.start_requests();
