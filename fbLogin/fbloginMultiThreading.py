import requests
import json
import re
import csv
import time
import threading
from requests.packages.urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

https_proxy = ["https://88.147.142.25:8080",
               "https://179.219.96.199:8080", "https://94.130.14.146:3128",
               "https://181.210.20.37:8080", "https://182.48.84.178:8080"
               "https://41.190.33.162:8080", "https://159.89.192.39:3128",
               "https://177.67.83.134:3128", "https://185.93.3.123:8080"];
index = 0;
def userExists(identity):
    global index;
    try:
        index = index + 1;
        time.sleep(1);
        headers = {};
        headers["accept-language"] = "en-GB,en-US;q=0.9,en;q=0.8"
        headers["content-type"] = "application/x-www-form-urlencoded"    
        headers["user-agent"] = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.139 Safari/537.36"

        formdata = {"email" : identity, "pass" : "dsaasdsa", "prefill_contact_point" : identity}
        #url = "https://m.facebook.com/login/async/?refsrc=https%3A%2F%2Fm.facebook.com%2F&lwv=100";
        url = 'https://www.facebook.com/login.php?login_attempt=1&lwv=120&lwc=1348028'
        proxy = https_proxy[index%9];
        proxyDict = {};
        proxyDict["https"] = proxy;
        print(proxy);
        #htmlResponse =  requests.post(url, data = formdata, headers = headers, proxies=proxyDict, verify=False);
        htmlResponse =  requests.post(url, data = formdata, headers = headers, verify=False);
        print(str(htmlResponse.content));
        with  open("response.txt", 'w') as txt:
            txt.write(str(htmlResponse.content));
        
        exp = re.match(r'(?is).*(m_login_notice.*The password you entered is incorrect)' , str(htmlResponse.content));
    except Exception as ex:
        print(ex);
        return None;
    if exp :
        return True;
    else :
        return False;

def saveToFile(data):
    print("****************** Going to save data ***************");
    with open('fbUserData.csv', 'a') as csvfile:
        fieldnames =['user', 'exists'];
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        for entries in data:
            writer.writerow(entries)

def scrapeInfo(*userList):
    #print(userList);
    finalData = [];
    for no in userList:
        exists = userExists(no);
        print(no);
        print(exists);
        userInfo = {};
        userInfo["user"] = row[0];
        if exists == None:
            continue;

        userInfo['exists'] = exists;
        finalData.append(userInfo);
        if (len(finalData) > 10):
            print("\n************************* Going to write in csv file **************")
            saveToFile(finalData);
            finalData= [];

    print("\n************************* Going to write in csv file **************")
    print(finalData);
    saveToFile(finalData);


print("START");
finalData = [];
with open('Nishant_Mobile.csv', 'r') as csvfile:
    textReader = csv.reader(csvfile, delimiter=' ', quotechar='|')
    data = [];
    for row in textReader:
        data.append(row[0]);
        #data.append("9811683344");
        scrapeInfo([row[0]]);
        break;
        #if (len(data) >= 2500) :
#            print("starting thread");
#            t1 = threading.Thread(target=scrapeInfo, args=data);
#            t1.start()
#            data = [];

            #print("Thread work completed!")
