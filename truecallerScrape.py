import csv
import requests
import json
import random
import time
from requests.packages.urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

tagDict = {"1":"Education","2":"Entertainment & Arts","3":"Finance, Insurance & Legal","4":"Governmental & Public Services","5":"Health & Wellness","6":"Hotels & Accommodation","7":"Nightlife & Drinks","8":"Restaurants & CafÃ©s","9":"Services","10":"Shopping & Convenience Stores","11":"Transportation","12":"Travel & Tourism","16":"Art school","17":"Child care services","18":"College","19":"Courses","20":"Music school","21":"Private school","22":"School","23":"Supplementary education","24":"Training and seminars","25":"University","26":"Amusement park","27":"Art gallery","28":"Bowling","29":"Casino","30":"Cinema","31":"Circus","32":"Concert hall","33":"Exhibition center","34":"Library","35":"Museum","36":"Opera","37":"Theater","38":"Zoo","39":"Accounting","40":"Auditing","41":"Bank","42":"Bookkeeping","43":"Exchange","44":"Financial","45":"Insurance","46":"Legal","47":"Loans leasing","48":"Mortgage lending","49":"Pawn broker","50":"Real estate broker","51":"Embassy","52":"Emergency services","53":"Employment agency","54":"Immigration","55":"Legal","56":"Media","57":"Military","58":"Non-profit","59":"Police","60":"Political","61":"Religious","62":"Tax agency","63":"Transportation","64":"Salon","65":"Chiropractor","66":"Cosmetology","67":"Dentist","68":"Doctor","69":"Emergency care","70":"Optometrist","71":"Gym","72":"Barber","73":"Hospital","74":"Manicure and pedicure","75":"Massage","76":"Nail salon","77":"Nutrition","78":"Pharmacy","79":"Tattoo and piercing","80":"Cosmetic surgery","81":"Psychologist","82":"Spa","83":"Veterinarian","84":"Bed and breakfast","85":"Camp ground","86":"Apartment","87":"Hotel","88":"Motel","89":"Adult entertainment","90":"Pub","91":"Comedy club","92":"Dance club","93":"Jazz club","94":"Karaoke","95":"Night club","96":"American restaurant","97":"Bakery","98":"Cafe","99":"Catering","100":"Chinese restaurant","101":"Fast food","102":"French restaurant","103":"Grill restaurant","104":"Indian restaurant","105":"Italian restaurant","106":"Japanese restaurant","107":"Korean restaurant","108":"Mediterranean restaurant","109":"Asian restaurant","110":"Pizzeria","111":"Seafood restaurant","112":"Spanish restaurant","113":"Sushi restaurant","114":"Tea room","115":"Thai restaurant","116":"Vegetarian restaurant","117":"Car dealership","118":"Cleaning","119":"Construction","120":"Consulting","121":"Dry cleaning","122":"Employment services","123":"Event planning","124":"Funeral home","125":"Information technology","126":"Internet provider","127":"Marketing agency","128":"Mechanic","129":"Mobile operator","130":"Plumbing","131":"Security","132":"Tailor","133":"Telemarketing","134":"Convenience stores","135":"Baby store","136":"Book store","137":"Wedding attire","138":"Clothing store","139":"Computer store","140":"Cosmetics store","141":"Electronics store","142":"Florist","143":"Furniture store","144":"Grocery store","145":"Home appliances store","146":"Interior design","147":"Jewelry","148":"Kitchen design","149":"Lighting design","150":"Shopping mall","151":"Mobile phone store","152":"Online shopping","153":"Adult novelty store","154":"Shoe store","155":"Shopping center","156":"Souvenir store","157":"Toy store","158":"Warehouse","159":"Watch store","160":"Airline service","161":"Boat service","162":"Bus service","163":"Car rental","164":"Gas station","165":"Limousine service","166":"Moving company","167":"Delivery service","168":"Public transit","169":"Taxi service","170":"Towing service","171":"Train service","172":"Customs service","173":"Tourism","174":"Travel agency","175":"Visa center"}

accessTokens = ["ya29.GlyyBa2pMRgrgvmQsXCefZ9p_A5xf8p9xkDy7ir3f3yyZsHrxj5scRlH6KaxSaZbTCv2ibA62WPPoZLmmHbj-mhga4le2IPwPchy0VsS4k_CLxR2miZoddwg4vUapA"]

authList = ["Bearer LBC0dhuB1F~baI48WkTO-fS2A40-c7PG"]

cookieList = ["OCAK=9SPCkJfMEL1Mb5HE3dW8rBY2YtbIr6TfE3CKlNWLnW8; HSID=AJnbns_rA1ses_voB; SSID=AE_25NBIBCig7MvdJ; APISID=isQ2tO1brTdZ_yG0/ALv7sRsLCIbUlslh0; SAPISID=bW48F2fYUZkZyAPn/AsPxeEa1Yzp1whpcO; ACCOUNT_CHOOSER=AFx_qI4yOwgEyyRTySdkROUepbW0ZpmpShV4AWRbHlaCB_UfFqhvZkM1u5jCdg7p-ij_e-KX1pYvRbb9Ot537XmoRLjZnWCR1HoBZHZTcvo12c9wgr4UEWkj3TRNeN630096duBBWlSmV4UEvPTNDNE4Rx-JxCtsc4TTQfka8gY-Y1EnKi-q8qKF_37MZk4KltN0D3o90w18yi98chDWp5qEw7kpFCmR6M5zsEe9ZI6nh9T3L1YLUGdV-QAjf62aLH5dq7lFGTkRkvggHr-gvcz6Cr_C8Hz81wjL_m4osL620i5Xx9fn9-TNaMPymtL8Cvd8xvgKy3CH0we56M0fAvBWkJtqn4ghECmkgXZnSXmNuTZnCzpqziOUJlMFDeDO0P3IQcNEfGzB; LSOLH=|||Azg1JU9M5sEQYPoZu2K3VdvMwb6cMhY:|||25423592:cf96; SID=FAb4ViQwBx6ho7lYf5A5Hm0o7-Lw32qh03oLaOton6_vK0IvsaUZ_eiNxrKkiDdndpu7rw.; LSID=ah|cl|doritos|mail|o.calendar.google.com|o.console.developers.google.com|o.mail.google.com|o.myaccount.google.com|o.notifications.google.com|s.IN|s.blogger|s.youtube|ss:FAb4Vo36WJcUZOX5DiOvxupzxorJV0mlEmH63qIzeSSjpRhGqM6TkWjAiZWjAHwEFCy3wQ.; 1P_JAR=2018-5-5-14; S=billing-ui-v3=Wtcqw_xDsC-schLKICCLZxWbsU3maGgi:billing-ui-v3-efe=Wtcqw_xDsC-schLKICCLZxWbsU3maGgi; NID=129=FemmKLP8sQT2NCcv7ccZNy94bnA-NKG9zfktvIXvpqfGdZebnD1JXTzjY8bZz1j_Ve4nJ-ZBWrA3pb5IVJWW9MBs8NSh2tza5ZvjoVFrcZhuM1VDmoz9vjdHlvksHF9yvbiu3auJtX55qPLtf5anstRqcMptyvGGX_Y2LDlVockDw_yv660hn5VPYS_CPfu-moZd1V3jE6ogNa-H7vGBOFf9o67LpvGLvWY-LSdK6V9VGa6rhsQ0JaLkC9A47p-g6i2NcRqsNRhoUHZSNVT5ZQmWVcU29vrFL-sG4llPUaQJPoHMs2P1Oj1zemIa8UOHvex80ILTxGpFeZ4VIWaNMZhb4v7t6xeLO_G75NkgsPFjutE2pa-Dj_jtvR_BAovZlR1sqy7wvFDeuCxhSTZ_iZx5tLiiDZlirGn4Tu6NcCBxPRF2eV40Nclj7SjbmxU; GAPS=1:3FO6y-6hKZxObxJcsDJmLZlL9URW05EouSBaGvVHml368Jkr7pDESQJOoNoBJPgCeYK3ioHA9nq7hPnPYK4vPoJ_c9uaPg:-2ubw1EP1-MZ9NS8; SIDCC=AEfoLebl1HzINB2mRW7SEHT1CsUlv_Y4x0ZDsoWFMEZhDKgK-RjiswflOdZkb06sIC_ru4MhYPQp"]


fetchedDataArray = [];
dataNotFound = [];
index = 0;
sleepIndex = -1;

def getgmailToken():
    global index;
    print("getting gmail token");
    headers = {};
    headers["User-Agent"] = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.139 Safari/537.36";
    headers["Referer"] = "https://accounts.google.com/o/oauth2/iframe";
    headers["x-client-data"] = "CIq2yQEIorbJAQjBtskBCKmdygEIqKPKAQ==";
    headers["x-requested-with"] = "XmlHttpRequest";
    headers["cookie"] = cookieList[index];
    headers["scheme"] = 'https';
    url = "https://accounts.google.com/o/oauth2/iframerpc?action=issueToken&response_type=token%20id_token&login_hint=AJDLj6Ix4XTwMTzY1_40OcMqSboXl1DnNAxBQNIS4HiwQKfuA3HJxKYHlUz10MLe43nGA-MnIpuGjRQazBJoyHzFG3IIU2mtUqEQI7shC86jsFG0gXCQ0Hg&client_id=22378802832-klpcj5dosalhnu0vshg3hjm9qgidmp8j.apps.googleusercontent.com&origin=https%3A%2F%2Fwww.truecaller.com&scope=openid%20profile%20email&ss_domain=https%3A%2F%2Fwww.truecaller.com";
    
    print("gmail token headers");
    print(headers);
    htmlResponse =  requests.get(url, headers = headers, verify=False);
    jsonResponse = json.loads(htmlResponse.content);
    print("<<<<<<< GMAIL TOKEN >>>>>>>>");
    print(jsonResponse);
    print("accessTokens before");
    print(accessTokens);
    if "access_token" in jsonResponse :
        accessTokens[index] = jsonResponse["access_token"];

    print("after");
    print(accessTokens);


def saveToFile(data):
    with open('phoneNumberInfo.csv', 'a') as csvfile:
        fieldnames =['phone_no', 'id', 'name', 'score', 'gender', 'carrier', 'address', 'city', 'countrycode', 'email', 'cat'];
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        for entries in data:
            writer.writerow(entries)

def updateAuthList() :
    global tokenX;
    global index;
    payload = '''{"accessToken": "''' + accessTokens[index] + '''"}''';
    print("update auth list");
    print(payload);
    htmlResponse =  requests.post("https://www.truecaller.com/api/auth/google?clientId=4", data = payload, verify=False);
    jsonResponse = json.loads(htmlResponse.content);
    print("new token got it");
    print(jsonResponse);
    if 'accessToken' in jsonResponse :
        tokenX = 'Bearer ' + jsonResponse['accessToken'];
        print(tokenX);
        #print(index);
        authList[index] = tokenX;
    else :
        print("accesstoken not found");
        getgmailToken();
        updateAuthList();

def getHeaders() :
    global index;
    headers = {};
    headers["User-Agent"] = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36';
    headers["Authorization"] = authList[index];
    index +=1;
    #headers["Authorization"] = tokenX;
    if index == len(authList)-1 :
        index = 0;
    return headers;

def replaceComma(text):
    text = text.strip();
    text = text.replace(",", " ");
    return text;

def makeRequest(url):
    truecallerHeader = getHeaders();
    #print(truecallerHeader);
    htmlResponse =  requests.get(url, headers = truecallerHeader, verify=False);
    jsonResponse = json.loads(htmlResponse.content);
    return jsonResponse;

def makeRequestWithoutIncreasingHeaders(url):
    global index;
    headers = {};
    headers["User-Agent"] = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36';
    headers["Authorization"] = authList[index];
    index +=1;
    #headers["Authorization"] = tokenX;
    if index == len(authList)-1 :
        index = 0;
    
    #truecallerHeader = getHeaders();
    #print(truecallerHeader);
    htmlResponse =  requests.get(url, headers = headers, verify=False);
    jsonResponse = json.loads(htmlResponse.content);
    return jsonResponse;


try :
    with open('Nishant_Mobile.csv', 'r') as csvfile:
        textReader = csv.reader(csvfile, delimiter=' ', quotechar='|')
        for row in textReader:
            userInfo = {};
            userInfo["phone_no"] = row[0].encode('utf-8');
            userInfo['id'] = 'NF';
            userInfo['name'] = 'NF';
            userInfo['score'] = 'NF';
            userInfo['gender'] = 'NF';
            userInfo['carrier'] = 'NF';
            userInfo['address'] = 'NF';
            userInfo['city'] = 'NF';
            userInfo['countrycode'] = 'NF';
            userInfo['email'] = 'NF';
            userInfo['cat'] = 'NF';
            fetchUrl = 'https://www.truecaller.com/api/search?type=4&countryCode=in&q='+row[0];
            jsonResponse = makeRequest(fetchUrl);
            if "data" not in jsonResponse :
                print(str(row[0]) + " ---- index: " + str(index) + "----" +str(jsonResponse));
                updateAuthList();
                jsonResponse = makeRequestWithoutIncreasingHeaders(fetchUrl);
                if "data" not in jsonResponse :
                    dataNotFound.append(row[0]);
                    continue;
        
            #print("----------------------- GOT IT ----------------");
            try :
                print("************ response recvd no : " + str(sleepIndex) + " **************");
                sleepIndex +=1;
                #if sleepIndex%5== 0:
                #time.sleep(2);
                if len(jsonResponse["data"]) > 0 :
                    data = jsonResponse["data"][0];
                    
                    if "id" in data :
                        userInfo["id"] = data["id"].strip().encode('utf-8');
                    
                    if "name" in data :
                        name = replaceComma(data["name"]);
                        userInfo["name"] = name.encode('utf-8');
                    
                    if "score" in data :
                        userInfo["score"] = data["score"];
                    
                    if "gender" in data :
                        userInfo["gender"] = data["gender"].strip().encode('utf-8');
                    
                    if "phones" in data :
                        phoneInfo = data["phones"];
                        if len(phoneInfo) > 0 :
                            phonedetails = data["phones"][0];
                            if "carrier" in phonedetails :
                                carr = replaceComma(phonedetails["carrier"]);
                                userInfo["carrier"] = carr.encode('utf-8');
                    
                    if "addresses" in data :
                        if len(data["addresses"]) > 0 :
                            addressDetails = data["addresses"][0];
                            if "address" in addressDetails:
                                addr = replaceComma(addressDetails["address"]);
                                userInfo["address"] = addr.encode('utf-8');
                            if "city" in addressDetails:
                                city = replaceComma(addressDetails["city"]);
                                userInfo["city"] = city.encode('utf-8');
                            if "countrycode" in addressDetails:
                                userInfo["countrycode"] = addressDetails["countrycode"].strip().encode('utf-8');
                
                    if "internetAddresses" in data :
                        if len(data["internetAddresses"]) > 0:
                            iAddr = data["internetAddresses"][0];
                            if "service" in iAddr :
                                if iAddr["service"] == "email":
                                    userInfo["email"] = iAddr["id"].strip().encode('utf-8');
            
            if "tags" in data :
                if len(data["tags"]) > 0:
                    tags = data["tags"];
                    categories = tagDict[tags[0]].strip();
                    for i in range(1, len(tags)) :
                        categories = categories + "|" + tagDict[tags[i]].strip();
                            userInfo["cat"] = categories.encode('utf-8');
                
                    fetchedDataArray.append(userInfo);
                    if len(fetchedDataArray) > 50 :
                        print("\n\n************************* Going to write in csv file **************")
                        saveToFile(fetchedDataArray);
                        fetchedDataArray = [];
except Exception as ex:
    print("some encoding issue " + str(ex));
    print(str(row[0]) + " ---- " +str(jsonResponse));
    dataNotFound.append(row[0]);
except Exception as ex:
    print("------- EXCEPTION ------------" + str(ex));
    print(dataNotFound);

