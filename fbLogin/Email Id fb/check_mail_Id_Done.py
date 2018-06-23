import csv
import re
finaljson = {}
with open('K_Email/K_Email_final.csv', 'r', encoding='utf-8') as csvfile:
    textReader = csv.reader(csvfile, delimiter=' ', quotechar='|')
    for row in textReader:
        #print(row)
        if len(row) > 0 :
            p = re.search(r'([^,]+),(true|false|True|TRUE|FALSE|False|exists)', row[0])
            if p is not None :
                finaljson[p[1]]="YES"
print("Scraped : " + str(len(finaljson)))
notScraped = []
count = 0
with open('K_Email/Full_K_Email.csv', 'r', encoding='utf-8') as csvfile:
    #print("************")
    textReader = csv.reader(csvfile, delimiter=' ', quotechar='|')
    for row in textReader:
        count +=1
        #print(row[0])
        if row[0] in finaljson:
            pass
        else:
            #print(row[0])
            notScraped.append(row[0])

print("Total count : " + str(count))
print("Not scraped : " + str(len(notScraped)))

            
