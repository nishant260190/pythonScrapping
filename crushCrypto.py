# coding: utf-8

# import libraries
import requests
import re
from bs4 import BeautifulSoup

class crushCrypto:
    def scrapeInfo(self):
        print("crushCrypto")
        # specify the url
        page_url = 'https://crushcrypto.com/glossary/'
        # query the website and return the html to the variable ‘page’
        page = requests.get(page_url, headers={"cookie":"__cfduid=da35ef04850222012499907332c20519d1529734653; _ga=GA1.2.908457631.1529734666; _gid=GA1.2.1591639936.1529914473; cf_clearance=df6873f1ad3820f6b6ec7d0aa13dd1148b0df3d7-1529933723-1800","user-agent":"Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.87 Safari/537.36"})
        page.encoding= 'utf-8'
        # parse the html using beautiful soup and store in variable `soup`
        soup = BeautifulSoup(page.text, 'html.parser')
        term_list=soup.find_all('strong')
        term_def=soup.find_all(class_='thrv_wrapper thrv_text_element tve_empty_dropzone')
        data=[]
        i=0
        j=0 
        for tag in term_def:
             if tag.has_attr('id'):
                 finaljson= {}
                 finaljson["Terms"]= term_list[i].get_text().replace("\xa0","")
                 i=i+1
                 defin = re.sub(r'^[A-Za-z][^-]+-\s*',"", term_def[j].get_text())
                 finaljson["Definition"]= defin
                 data.append(finaljson)
                 j=j+1
        print(data)
        return data

#obj=crushCrypto()
#obj.getScrappedInfo()
