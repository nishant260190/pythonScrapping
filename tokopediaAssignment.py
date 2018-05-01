import json
import requests
import codecs
from requests.packages.urllib3.exceptions import InsecureRequestWarning

def getShopDataForShopId(id) :
    sellerUrl = "https://shopee.co.id/api/v1/shops/";
    data = '{"shop_ids":[' + id + ']}';
    shopPageHeaders = {};
    shopPageHeaders["User-Agent"] = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36";
    shopPageHeaders["x-csrftoken"] = "pzzf4KfMeFHiX7ChS2hzKcd1YRHrYQwQ";
    shopPageHeaders["Cookie"] = """SPC_IA=-1; SPC_EC=-; SPC_F=EKb1yy2l3ah0IrMvElA0FPW1Rvd9MfOk; REC_T_ID=b7411b34-4713-11e8-a675-1866da566dbe; SPC_T_ID="ZDSomKMcmb7HVgFWMXaRqHp6OZilZnJbrqyhmNCkgtgUbUAKM9mw4RNVUPP70yjSGslD16hx/6xh727Hr10c2oKa3O/XbYGdRJbsYIbthOI="; SPC_SI=lxjigda2ckgo46xzrcr0fhkvym97j7pc; SPC_U=-; SPC_T_IV="7426+hQgq205sJbGWYwOcg=="; _ga=GA1.3.547673798.1524501064; _gid=GA1.3.475043293.1524501064; cto_lwid=cf9442ea-f0bd-4637-9593-0f1b8fec519c; csrftoken=pzzf4KfMeFHiX7ChS2hzKcd1YRHrYQwQ; SPC_SC_TK=; UYOMAPJWEMDGJ=; SPC_SC_UD=; _gat=1; _gat_gtm=1""";
    shopPageHeaders["referer"] = shopPageUrl;
 
    shopPageResponse =  requests.post(sellerUrl, data = data, headers = shopPageHeaders, verify=False);
    jsonResponse = json.loads(shopPageResponse.content);
    jsonDict = jsonResponse[0];
    shopDict = {};
    if "name" in jsonDict :
        shopDict["Shop Name"] = jsonDict["name"];
    if "portrait" in jsonDict :
        shopDict["Shop Logo"] = "https://cf.shopee.co.id/file/" + str(jsonDict["portrait"]) + "_tn";
    if "item_count" in jsonDict :
        shopDict["Number of Products"] = jsonDict["item_count"];
    if "description" in jsonDict :
        shopDict["Shop tagline"] = jsonDict["description"];
    if "sadas" in jsonDict :
        shopDict["XXXXX"] = jsonDict["sadas"];

    return shopDict;


def getshopProductsInfo(id):
    productPageHeaders = {}
    productPageHeaders["User-Agent"] = "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36";
    productPageUrl = 'https://shopee.co.id/api/v2/search_items/?by=pop&limit=30&match_id=' + id + '&newest=0&order=desc&page_type=shop'; 
    productPageApiUrlReq = requests.get(productPageUrl, headers=productPageHeaders);
    jsonResponse1 = json.loads(productPageApiUrlReq.content);
    productList = jsonResponse1["items"];

    productArray = [];
    for product in productList :
        productData = {};
        if "name" in product :
            productData["Name"] = product["name"];
        if "catid" in product :
            productData["Category"] = product["catid"];
        if "price" in product :
            productData["Price after discount"] = product["price"];
        if "price_before_discount" in product : 
            productData["Price before discount"] = product["price_before_discount"];
        if "stock" in product :
            productData["stock"] = product["stock"];
        i = 0;
        mainImage = "https://cf.shopee.co.id/file/" + product["image"] + "_tn";
        productData["image_" + str(i)] = mainImage;
        imageList = product["images"];
        for image in imageList:
            singleImage = "https://cf.shopee.co.id/file/" + image + "_tn";
            productData["image_" + str(i)] = singleImage;
            i = i+1;
        productArray.append(productData);
    return productArray;

def getShopId(shopname) :
    sellerUrl = "https://shopee.co.id/api/v1/shop_ids_by_username/";
    data = '{"usernames":["' + shopname + '"]}';
    shopPageHeaders = {};
    shopPageHeaders["User-Agent"] = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36";
    shopPageHeaders["x-csrftoken"] = "GVgOUC3F9CpAjL7cXOCqJee9GHAJ6X4y";
    shopPageHeaders["Cookie"] = """_ga=GA1.3.1616093984.1523889392; cto_lwid=4edc511c-0c14-4426-ba91-814034616f4a; csrftoken=GVgOUC3F9CpAjL7cXOCqJee9GHAJ6X4y; SPC_IA=-1; SPC_U=-; SPC_EC=-; bannerShown=true; SPC_F=dYFP59kk1pxINcije78e7YN9a0bx0PVd; REC_T_ID=91f07f54-4183-11e8-954d-1866daacb4e1; SPC_T_ID="Tu1yNFYkRMdekGVlMzbQIioDx6BxlHSbH1BYeIdIaDJI9LZMJtsvxYNl4MUJRp2T9STR+p/bpKt9C4cmQVeMmU7MfnMhNHYaIzia0opXyzY="; SPC_T_IV="1bbttgeWgmZ5dq5Ra+nzbQ=="; SPC_SC_TK=; UYOMAPJWEMDGJ=; SPC_SC_UD=; SPC_SI=cubchp2wu55asqyftobb0802vrv4mwk7; _gid=GA1.3.841685964.1524499549; _gat=1""";
    shopPageHeaders["referer"] = shopPageUrl;
    shopPageResponse =  requests.post(sellerUrl, data = data, headers = shopPageHeaders, verify=False);
    jsonResponse = json.loads(shopPageResponse.content);
    jsonDict = jsonResponse[0];
    return jsonDict[shopname];

requests.packages.urllib3.disable_warnings(InsecureRequestWarning)
shopPageUrl = input("Please enter shop page url like : https://shopee.co.id/jamoriginal88 \n");
pathComponents = shopPageUrl.split("/");
shopname = pathComponents[-1];
shopId = str(getShopId(shopname));
print("Scrapping...");
finalDict = {};
shopDict = getShopDataForShopId(shopId);
productInfoArray = getshopProductsInfo(shopId);
finalDict["shopInfo"] = shopDict;
finalDict["productsData"] = productInfoArray;
file2write = codecs.open("TokoPediaAssignment.txt", encoding='utf-8', mode='w+');
file2write.write(str(finalDict));
print("Data scrapped and written in TokoPediaAssignment text file");
file2write.close();
