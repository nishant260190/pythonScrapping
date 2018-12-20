# import libraries
import requests
from bs4 import BeautifulSoup


class blockgeeks:
    def scrapeInfo(self):

        # specify the url
        page_url = 'https://blockgeeks.com/guides/blockchain-glossary-from-a-z/'
        
        # query the website and return the html to the variable ‘page’
        page = requests.get(page_url)
        page.encoding= 'utf-8'
        
        # parse the html using beautiful soup and store in variable `soup`
        soup = BeautifulSoup(page.text, 'html.parser')
        
        #search all instances of paragraph attribute in html
        term=soup.find_all('p')
        data=[]

        #manually checked the occurences of term and def and ran the loop accordingly from j=3
        j=3
         
        while (j<99):
            finaljson={}
            finaljson["Terms"]= term[j].get_text()
            finaljson["Definition"]= term[j+1].get_text()
            data.append(finaljson)
            j=j+2

        return data
            
#obj=blockgeeks()
#obj.getScrappedInfo()
   
