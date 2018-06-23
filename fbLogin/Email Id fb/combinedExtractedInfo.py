import csv
import re

finaljson = {}
extractdata = []

with open('Man_Email_final.csv', 'r', encoding='utf-8') as csvfile:
    textReader = csv.reader(csvfile, delimiter=' ', quotechar='|')
    for row in textReader:
        if len(row) > 0 :
            p = re.search(r'([^,]+),(true|false|exists)', row[0])
            if p != None :
                finaljson[p[1].strip()]=p[2].strip().lower()


print(len(finaljson))

with open('Man_Email_fbUserInfo.csv', 'r', encoding='utf-8') as csvfile:
    textReader = csv.reader(csvfile, delimiter=' ', quotechar='|')
    for row in textReader:
        if len(row) > 0 :
            p = re.search(r'([^,]+),(true|false|exists)', row[0])
            if p is not None :
                emailId = p[1].strip()
                value = p[2].strip().lower()
                if emailId in finaljson:
                    if finaljson[emailId].strip().lower() != value :
                        '''print("-------")
                        print(finaljson[emailId].strip().lower())
                        print(value)'''
                        if finaljson[emailId].lower() == 'true':
                            finaljson[emailId]= 'true'
                        if value == 'true':
                            finaljson[emailId]= 'true'
                        #print("something is wrong for " + emailId + " e_mail_final value is : " +finaljson[emailId] + " and second : " + value)
                else :    
                    finaljson[emailId]=value


print(len(finaljson))

with open('K_Email_Extractedinfo.csv', 'a') as csvfile:
        fieldnames =['user', 'exists'];
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        for k,v in finaljson.items():
            info = {"user":k.encode('utf-8'), "exists":v}
            writer.writerow(info)
