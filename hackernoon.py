
# coding: utf-8

# import libraries
import requests
from bs4 import BeautifulSoup

class hackernoon:
    def scrapeInfo(self):
        print("hackernoon")
        # specify the url
        page_url = 'https://hackernoon.com/blockchain-dictionary-f4d098c9ef89'
        
        # query the website and return the html to the variable ‘page’
        page = requests.get(page_url)
        page.encoding= 'utf-8'
        
        # parse the html using beautiful soup and store in variable `soup`
        soup = BeautifulSoup(page.text, 'html.parser')
        
        term_def1=soup.find_all(class_='graf graf--li graf--leading')
        term_def2=soup.find_all(class_='graf graf--li graf-after--li')
        term_def=term_def1+term_def2
        term_list=[]
        i=0
        while(i<len(term_def)):
            term_list.append(term_def[i].find(class_='markup--strong markup--li-strong'))
            i=i+1
        
        j=0    
        data = []
        while (j<len(term_list)):
            finaljson= {}
            finaljson["Terms"]= term_list[j].get_text()
            finaljson["Definition"] = term_def[j].get_text()
            data.append(finaljson)
            j=j+1
        return data
#obj=hackernoon()
#obj.getScrappedInfo()
