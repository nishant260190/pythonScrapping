# coding: utf-8

# import libraries
import requests
from bs4 import BeautifulSoup

class blockchainwtf:
    def scrapeInfo(self):
        print("blockchainwtf")
        # specify the url
        page_url = 'https://blockchain.wtf/blockchain-glossaries/beginners-glossary/'
        # query the website and return the html to the variable ‘page’
        page = requests.get(page_url)
        page.encoding= 'utf-8'
        # parse the html using beautiful soup and store in variable `soup`
        soup = BeautifulSoup(page.text, 'html.parser')
        term_list=[]
        for litag in soup.find_all('li'):
            for h4tag in litag.find_all('h4'):
                term_list.append(h4tag.text)
        term_def=soup.find_all('p', attrs={'style':'padding-left: 60px;'})
        j=0    
        data = []
        while (j<len(term_list)):
            finaljson= {}
            finaljson["Terms"]= term_list[j]
            finaljson["Definition"] = term_def[j].get_text()
            data.append(finaljson)
            j=j+1

        return data
        
#obj=blockchainwtf()
#obj.getScrappedInfo()
