    
import requests
from bs4 import BeautifulSoup

class Upfolio:
    def scrapeInfo(self):
        print("Upfolio")
        # specify the url
        page_url = 'https://www.upfolio.com/glossary'
        # query the website and return the html to the variable ‘page’
        page = requests.get(page_url)
        page.encoding= 'utf-8'
        # parse the html using beautiful soup and store in variable `soup`
        soup = BeautifulSoup(page.text, 'html.parser')
        term_list=soup.find_all(class_='glossarytermname')
        term_def=soup.find_all(class_='glossarytermdescription')
        j=0    
        data = []
        while (j<len(term_list)):
            finaljson= {}
            finaljson["Terms"]= term_list[j].get_text()
            finaljson["Definition"] = term_def[j].get_text()
            data.append(finaljson)
            j=j+1
        return data
#obj=Upfolio()
#obj.getScrappedInfo()
