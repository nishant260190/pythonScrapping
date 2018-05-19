import requests
import json
import re
import csv
import time
import threading
from random import randint
from requests.packages.urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

'''https_proxy = ["https://81.23.196.198:8080", "https://181.210.20.37:8080",
               "https://80.211.178.125:8080", "https://88.68.70.156:8080",
               "https://200.229.197.130:8080", "https://159.65.145.235:8080"
               "https://191.252.195.27:3128", "https://80.48.119.28:8080",
               "https://94.130.14.146:31288", "https://138.201.223.250:31288"];
'''
def userExists(identity):
    try:
        #index = randint(0, 10);
        time.sleep(2);
        headers = {};
        headers["accept-language"] = "en-GB,en-US;q=0.9,en;q=0.8"
        headers["content-type"] = "application/x-www-form-urlencoded"    
        headers["user-agent"] = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.139 Safari/537.36"

        formdata = {"email" : identity, "pass" : "dsaasdsa", "prefill_contact_point" : identity}
        #url = "https://m.facebook.com/login/async/?refsrc=https%3A%2F%2Fm.facebook.com%2F&lwv=100";
        url = 'https://www.facebook.com/login.php?login_attempt=1&lwv=120&lwc=1348028'
        #noofproxy = len(https_proxy);
        #proxy = https_proxy[index];
        #proxyDict = {};
        #proxyDict["https"] = proxy;
        #print(proxy);
        htmlResponse =  requests.post(url, data = formdata, headers = headers, verify=False);
        #htmlResponse =  requests.post(url, data = formdata, headers = headers, verify=False);
        print(htmlResponse);
        #with  open("response.txt", 'w') as txt:
#            txt.write(str(htmlResponse.content));
        
        exp = re.match(r'(?is).*(m_login_notice.*The password you entered is incorrect)' , str(htmlResponse.content));
    except Exception as ex:
        print("******* EXCEP *********")
        print(ex);
        return None;
    if exp :
        return True;
    else :
        return False;

def saveToFile(data):
    print("****************** Going to save data ***************");
    with open('fbthreading.csv', 'a') as csvfile:
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
threadList = [];
with open('Nishant_Mobile.csv', 'r') as csvfile:
    textReader = csv.reader(csvfile, delimiter=' ', quotechar='|')
    data = [];
    for row in textReader:
        data.append(row[0]);
        if (len(data) >= 5000) :
            print("creating thread");
            t = threading.Thread(target=scrapeInfo, args=data);
            t.start();
            threadList.append(t);
            data = [];

for thread in threadList:
    thread.join();
