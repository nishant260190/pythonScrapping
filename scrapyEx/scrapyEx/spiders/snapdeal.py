import scrapy
import re

class snapdeal(scrapy.Spider):
    name = "snapdeal"
    print("inside snapdeal");
    globalUrl = ''
    def start_requests(self):
        global globalUrl;
        urls = ["https://www.snapdeal.com/acors/json/product/get/search/18/0/20"];
        for url in urls:
            print(url);
            globalUrl = url;
            yield scrapy.Request(url = url, callback = self.parse);

    def parse(self, response):
        global globalUrl;
        print(globalUrl);
        print("**************** parsing *********");
        dataFound = 'NO';
        #print(response.xpath('//div[@class="product-tuple-description "]').extract())
        for prd in response.xpath('//div[@class="product-tuple-description "]'):
            dataFound = 'YES';
            print("\n\n-----------------------");
            yield {
                'title' : prd.css('p.product-title::text').extract_first(),
                'url' : prd.css('a.dp-widget-link::attr("href")').extract_first(),
                'list_price' : prd.css('span.lfloat.product-price::text').extract_first(),
                'final_price' : prd.css('span.lfloat.product-desc-price.strike::text').extract_first(),
            
            }
            #print(prd.css('a.dp-widget-link::attr("href")').extract_first());
            #print(prd.css('p.product-title::text').extract_first());
            #print(prd.css('span.product-price::text').extract_first());
            #print(prd.css('span.product-desc-price::text').extract_first());
            #print("???????");
            #print(prd.css('span.lfloat.product-price::text').extract_first())
            #print(prd.css('span.lfloat.product-desc-price.strike::text').extract_first());
            #print(prd.xpath('//span[contains(@class, "lfloat") and contains(@class, "product-desc-price") and contains(@class, "strike")]').extract_first());
        
        if dataFound == 'YES':
            print("<<<<<<<<>>>>>>>>>")
            next_page = re.match(r'(https://www.snapdeal.com/acors/json/product/get/search/[0-9]+/)([0-9]+)(/20)', globalUrl);
            #print(next_page);
            #print(next_page[0]);
            #print(next_page[1]);
            #print(next_page[2]);
            pagecount = int(next_page[2]) + 20;
            next_url = next_page[1] + str(pagecount) + next_page[3];
            globalUrl = next_url;
            print(next_url);
            yield scrapy.Request(next_url, callback= self.parse);



