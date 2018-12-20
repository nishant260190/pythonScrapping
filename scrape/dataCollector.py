import csv
#import hackernoon
import edureka, allthingscrypto, blockchainwtf, blockgeeks, crushCrypto, hackernoon, Upfolio

finalData = []
at = allthingscrypto.allthingscrypto().scrapeInfo()
ed = edureka.edureka().scrapeInfo()
bc = blockchainwtf.blockchainwtf().scrapeInfo()
bg = blockgeeks.blockgeeks().scrapeInfo()
cc = crushCrypto.crushCrypto().scrapeInfo()
hn = hackernoon.hackernoon().scrapeInfo()
uf = Upfolio.Upfolio().scrapeInfo()

if len(at) > 0 :
    finalData.extend(at)
else :
    print("something is wrong with allthingscrypto plz check")
    
if len(ed) > 0 :
    finalData.extend(ed)
else :
    print("something is wrong with edureka plz check")
    
if len(bc) > 0 :
    finalData.extend(bc)
else :
    print("something is wrong with blockchainwtf plz check")
    
if len(bg) > 0 :
    finalData.extend(bg)
else :
    print("something is wrong with blockgeeks plz check")
    
if len(cc) > 0 :
    finalData.extend(cc)
else :
    print("something is wrong with crushCrypto plz check")
    
if len(hn) > 0 :
    finalData.extend(hn)
else :
    print("something is wrong with hackernoon plz check")
    
if len(uf) > 0 :
    finalData.extend(uf)
else :
    print("something is wrong with Upfolio plz check")
print("Total definitions extracted : " + str(len(finalData)))




with open("extractedInfo.csv", 'a', encoding='utf-8') as f:
    fieldnames =['Terms', 'Definition'];
    writer = csv.DictWriter(f, fieldnames=fieldnames)
    for entry in finalData:
        writer.writerow(entry)
