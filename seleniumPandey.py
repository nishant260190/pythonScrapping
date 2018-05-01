from selenium import webdriver
import re
import csv
import time
import lxml.html as lh
from selenium.webdriver.common.keys import Keys

output = csv.writer(open('opdnbindia.csv','wb'))
output.writerow(['Company Names', 'Search Company Name', 'Company Link'])
capabilities = {'chrome.binary': '/Users/devangpandey/Downloads/chromedriver'}
driver = webdriver.Remote("http://127.0.0.1:9515",  capabilities)
with open('/Users/devangpandey/Downloads/dnbsearch.csv') as csvfile:
    driver.get("https://www.google.co.in/")
    driver.refresh()
    raw_input("Press enter once you login.")
    readCSV = csv.reader(csvfile, delimiter=',')
    for row in readCSV:
        comp_name_search = ''
        comp_link = ''
        comp_name = row[0].decode('utf-8')
        driver.find_element_by_xpath('//*[@title="Search"]').send_keys(comp_name + Keys.ENTER)
        time.sleep(2)
        try:
            comp_link = driver.find_element_by_xpath('//*[@id="rso"]/div[1]/div/div/div/div//cite').text.encode('utf-8').strip()
            print (comp_link)
            comp_name_search = driver.find_element_by_xpath('//*[@id="rso"]/div[1]//div/div/h3').text.encode('utf-8').strip()
            print (comp_name_search)
        except:
            print ("no data")
        driver.find_element_by_xpath('//*[@title="Search"]').clear()
        output.writerow([comp_name,comp_name_search,comp_link])
