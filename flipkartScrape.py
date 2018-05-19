import scrapy

class flipkartScrapy(scrapy.Spider):
    name = "quotes"
    print("inside flipkartScrapy");
    def start_requests(self):
        urls = ["https://www.flipkart.com/men/tshirts/pr?sid=2oq,s9b,j9y&otracker=undefined_footer_footer"];
        for url in urls:
            print(url);
            yield scrapy.Request(url = url, callback=self.parse);


    def parse(self, response):
        print("inside parse method");
        print(response.css('title'));


print("start")
x = flipkartScrapy();
x.start_requests();
