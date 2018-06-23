import scrapy
import re

class jabongScrapy(scrapy.Spider):
    print("jabong scrapping ....");
    name = "jabong";
    page = 1;
    gurl = '';
    def start_requests(self):
        print("inside start req");
        urls = ["https://www.jabong.com/men/shoes/?source=topnav_men"];
        for url in urls:
            print(url);
            self.gurl = url;
            yield scrapy.Request(url = url, callback=self.parse);

    def parse(self, response):
        print("inside parse method");
        print(" page  >>>>>>>>>> " + str(self.page));
        dataFound = False;
        for prd in response.css('div.product-tile.img-responsive'):
            dataFound = True;
            brand = prd.css('div.h4::text').extract_first();
            name = prd.css('div.h4 span::text').extract_first();
            prd_name = brand + " " + name;
            
            url = prd.css('a::attr("href")').extract_first();
            url = "http://www.jabong.com" + url;
            
            finalPrice = prd.css('div.price span.standard-price::text').extract();
            if finalPrice and (len(finalPrice) > 0) :
                finalPrice = finalPrice[-1];

            listPrice = prd.css('div.price span.prev-price span.standard-price::text').extract_first();

            yield {
                'title' : prd_name,
                'url' : url,
                'final_price' : finalPrice,
                'list_price' : listPrice,
            }

            if dataFound:
                self.page = self.page + 1;
                print("url -------- " + str(self.gurl));
                next_url = re.match(r'(^https?://www.jabong.com/men/shoes/[?]source=topnav_men)(&page=[0-9]+)?', self.gurl);
                #print(next_url);
                if next_url :
                    next_url = next_url[1] + "&page=" + str(self.page);
                    print("**********************");
                    print(next_url);
                    self.gurl = next_url;
                    yield scrapy.Request(url = self.gurl, callback = self.parse);
                else :
                    print("//////////////////////// next_url check unsuccessful");
            else :
                print("///////////////////// data not found");


