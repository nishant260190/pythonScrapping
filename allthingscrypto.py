# import libraries
import requests
import re

class allthingscrypto:
    def __init__(self):
        pass
    def scrapeInfo(self):
        print("allthingscrypto")
        # specify the url
        page_url = 'https://allthingscrypto.tech/blockchain-glossary/'

        # query the website and return the html to the variable ‘page’
        page = requests.get(page_url)
        page.encoding= 'utf-8'
        term=re.findall(r'(<h2>[^<]+<\/h2>)(\n|\s)*(<p>[^<]+<\/p>(\s*|\n*))+',page.text)
        data = []
        for t in term:
            term = t[0]
            term = re.sub(r'(<[^>]+>|\n|\r)', "", term)

            text = ""
            for i in range(1,len(t)):
                text += t[i]

            text = re.sub(r'(<[^>]+>|\n|\r)', "", text)

            datajson = {}
            datajson["Terms"] = term
            datajson["Definition"] = text
            data.append(datajson)
        return data
#atc = allthingscrypto()
#atc.scrapeInfo()        
