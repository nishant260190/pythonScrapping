import scrapy
import requests
import json
import re
import datetime
import time
from elasticsearch import Elasticsearch

class flipkartScrapy(scrapy.Spider):
    name = "flipkart"
    print("inside flipkartScrapy");
    #pageNo = 100
    def start_requests(self):
        '''urls = ["https://www.flipkart.com/mobiles/pr?sid=tyy%2F4io&p%5B%5D=facets.brand%255B%255D%3DApple&p%5B%5D=facets.availability%255B%255D%3DExclude%2BOut%2Bof%2BStock&otracker=clp_metro_expandable_1_apple-categ-94e9d_iPhone_apple-products-store_90ff40fd-a46b-4a40-9440-fbe783136afb_DesktopSite_wp1&fm=neo/merchandising&iid=M_46e2e661-7e82-4e38-8fa1-719afb9068e8_1.90ff40fd-a46b-4a40-9440-fbe783136afb_DesktopSite&ppt=CLP&ppn=CLP:apple-products-store&ssid=40rf1pkdcg0000001528192884561",
                "https://www.flipkart.com/mobiles/samsung~brand/pr?count=40&p%5B%5D=sort%3Drecency_desc&sid=tyy%2F4io&wid=1.productCard.PMU_V2",
                "https://www.flipkart.com/mobiles/mi~brand/pr?sid=tyy,4io&otracker=nmenu_sub_Electronics_0_Mi"];
        '''
        '''urls = ["https://www.flipkart.com/mobiles-accessories/pr?sid=tyy",
                "https://www.flipkart.com/computers/pr?sid=6bo",
                "https://www.flipkart.com/cameras-accessories/pr?sid=jek"]'''
        urls = ["https://www.flipkart.com/search?p[]=facets.type%255B%255D%3DInverter&sid=j9e%2Fabm%2Fc54&otracker=CLP_filters&otracker=nmenu_sub_TVs%20and%20Appliances_0_Inverter%20AC",
                "https://www.flipkart.com/air-conditioners/split~type/pr?sid=j9e%2Cabm%2Cc54&otracker=nmenu_sub_TVs%20and%20Appliances_0_Split%20ACs",
                "https://www.flipkart.com/search?count=40&otracker=CLP_filters&p%5B%5D=facets.brand%255B%255D%3DSamsung&sid=ckf%2Fczl&otracker=nmenu_sub_TVs%20and%20Appliances_0_Samsung",
                "https://www.flipkart.com/refrigerators/single-door~type/pr?sid=j9e%2Cabm%2Chzg&otracker=nmenu_sub_TVs%20and%20Appliances_0_Single%20Door",
                "https://www.flipkart.com/refrigerators/double-door~type/pr?sid=j9e%2Cabm%2Chzg&otracker=nmenu_sub_TVs%20and%20Appliances_0_Double%20Door",
                "https://www.flipkart.com/refrigerators/triple-door~type/pr?sid=j9e%2Cabm%2Chzg&otracker=nmenu_sub_TVs%20and%20Appliances_0_Triple%20door",
                "https://www.flipkart.com/refrigerators/pr?otracker=categorytree&otracker=nmenu_sub_TVs%20and%20Appliances_0_Side%20by%20Side&p=facets.type%255B%255D%3DSide%2Bby%2BSide&sid=j9e%2Cabm%2Chzg",
                "https://www.flipkart.com/washing-machines/fully-automatic-front-load~function/pr?sid=j9e%2Cabm%2C8qx&otracker=nmenu_sub_TVs%20and%20Appliances_0_Fully%20Automatic%20Front%20Load",
                "https://www.flipkart.com/washing-machines/semi-automatic-top-load~function/pr?sid=j9e%2Cabm%2C8qx&otracker=nmenu_sub_TVs%20and%20Appliances_0_Semi%20Automatic%20Top%20Load",
                "https://www.flipkart.com/washing-machines/fully-automatic-top-load~function/pr?sid=j9e%2Cabm%2C8qx&otracker=nmenu_sub_TVs%20and%20Appliances_0_Fully%20Automatic%20Top%20Load"]
        for url in urls:
            print(url);
            yield scrapy.Request(url = url, callback=self.parse);

    def addInEs(self, doc):
        print("////")
        print(doc)
        #self.pageNo = self.pageNo + 1
        #es = Elasticsearch()
        es = Elasticsearch(['localhost'], http_auth=('elastic', 'NU0Qv6JxEBU2qQZaHfPm'), scheme="http", port=9200)
        pid = doc['productid']
        res = es.index(index="productanalysis", doc_type='electronics', body=doc, id = pid)
        print(res['result'])

    '''def insertInES(self, jsonData):
        headers = {};
        headers["User-Agent"] = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36'
        headers["Content-Type"] = 'application/json' 
        print("*********************** INSERTING IN ES ***********************")
        url = "http://localhost:9200/productanalysis/electronics/" + str(self.pageNo);
        print(url)
        self.pageNo = self.pageNo + 1
        htmlResponse = requests.put(url, headers=headers, data=jsonData ,verify=False);
        jsonResponse = json.loads(htmlResponse.content);
        print(jsonResponse)'''
        
    def parse(self, response):
        print("inside parse method");
        for product in response.xpath('//div[@class="_1UoZlX"]'):
            prdJson = {};
            #prdJson['title'] = product.css('a._2cLu-l::attr(title)').extract_first()
            prdJson['name'] = product.css('div._3wU53n::text').extract_first()
            url = product.css('a._31qSD5::attr(href)').extract_first()
            pid = re.search(r'/p/(itm[^?]+)[?].*?pid=([^&?]+)(&|$|[?])', url)
            product_id = pid[1] + "_" + pid[2]
            prdJson['productid'] = product_id
            prdJson['price'] = product.css('div._1vC4OE._2rQ-NK::text').extract_first()
            #prdJson['final_price'] = product.css('div._3auQ3N').extract_first()
            desc = " ".join(product.css('li.tVe95H::text').extract())
            desc = desc.replace("'","")
            desc = desc.replace('"',"")
            print(desc)
            prdJson['description'] = " ".join(product.css('li.tVe95H::text').extract())
            prdJson['rating'] = product.css('div.hGSR34._2beYZw::text').extract_first()
            currenttime = datetime.datetime.now()
            prdJson['timestamp'] = datetime.datetime.now()
            prdJson['year'] = currenttime.year
            prdJson['month'] = currenttime.month
            prdJson['day'] = currenttime.day
            prdJson['hour'] = currenttime.hour
            prdJson['minute'] = currenttime.minute
            prdJson['second'] = currenttime.second
            
            print(prdJson)
            time.sleep(1)
            #self.insertInES(prdJson)
            self.addInEs(prdJson)
        
        for product in response.xpath('//div[@class="_3liAhj _1R0K0g"]'):
            prdJson = {};
            #prdJson['title'] = product.css('a._2cLu-l::attr(title)').extract_first()
            prdJson['name'] = product.css('a._2cLu-l::text').extract_first()
            url = product.css('a._2cLu-l::attr(href)').extract_first()
            pid = re.search(r'/p/(itm[^?]+)[?].*?pid=([^&?]+)(&|$|[?])', url)
            product_id = pid[1] + "_" + pid[2]
            prdJson['productid'] = product_id
            prdJson['price'] = product.css('div._1vC4OE::text').extract_first()
            #desc = " ".join(product.css('li.tVe95H::text').extract())
            #desc = desc.replace("'","")
            #desc = desc.replace('"',"")
            #print(desc)
            #prdJson['description'] = " ".join(product.css('li.tVe95H::text').extract())
            prdJson['rating'] = product.css('div.hGSR34._2beYZw::text').extract_first()
            currenttime = datetime.datetime.now()
            prdJson['timestamp'] = datetime.datetime.now()
            prdJson['year'] = currenttime.year
            prdJson['month'] = currenttime.month
            prdJson['day'] = currenttime.day
            prdJson['hour'] = currenttime.hour
            prdJson['minute'] = currenttime.minute
            prdJson['second'] = currenttime.second
            
            print(prdJson)
            #time.sleep(1)
            #self.insertInES(prdJson)
            self.addInEs(prdJson)
                
        print("------------ next page ------------------");
        time.sleep(.5)
        next_page = response.css('a._3fVaIS::attr(href)').extract()
        print(next_page)
        if (next_page is not None) and (len(next_page) > 0):
            print(next_page[-1]);
            next_page = response.urljoin(next_page[-1])
            yield scrapy.Request(next_page, callback=self.parse)

    


print("start")
#x = flipkartScrapy();
#x.start_requests();


