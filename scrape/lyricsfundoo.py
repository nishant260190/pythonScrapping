import requests
import re
import threading
from bs4 import BeautifulSoup


seed_link = "https://www.lyricsfundoo.in/"
words_array = set()


# def check_word_array(word_arr):
# 	global words_array
# 	temp_array = []
# 	for item in words_array :
# 		if re.match('^[a-zA-z]+$', item) :
# 			temp_array.append(item)
# 		else :
# 			pass
# 	words_array = temp_array



# def save_in_file(word_arr):
#     with open("hindimehelp_words.txt", "a") as f :
#         for word in word_arr :
#         	# print("????/?? " + word)
#         	f.write(word + "\n")

# def scrape_article_page(url):
# 	print("------- article page " + url) 
# 	page = requests.get(url)
# 	page.encoding= 'utf-8'
# 	soup = BeautifulSoup(page.text, 'html.parser')
# 	x = soup.select("div[class='td-post-content']")
# 	for each in x :
# 		text = each.get_text().replace("\n", " ")
# 		word_arr = set(re.split('\W+', text))

# 		temp_array = []
# 		for item in word_arr :
# 			if re.match('^[a-zA-z]+$', item) :
# 				temp_array.append(item)
# 			else :
# 				pass
# 		word_arr = temp_array
# 		save_in_file(word_arr)


# def scrape_list_page(url):
#     page = requests.get(url)
#     page.encoding= 'utf-8'
#     soup = BeautifulSoup(page.text, 'html.parser')

#     x = soup.select("h3[class='entry-title td-module-title'] a ")
#     detail_page = []
#     for each in x :
#         detail_page.append(each.get("href"))

#     threadList = [];    
#     for article in detail_page :
#         t = threading.Thread(target=scrape_article_page, args=(article,));
#         t.start();
#         threadList.append(t);

#     for thread in threadList:
#     	thread.join(); 

# count = 47
# for i in range(47):
# 	if i == 0 :
# 		link = seed_link
# 	else :
# 		link = seed_link + "page/" + str(i)
# 	scrape_list_page(link)


page = requests.get(seed_link)
page.encoding= 'utf-8'
soup = BeautifulSoup(page.text, 'html.parser')
print(page.text)
x = soup.select("span[class='showpage'] a ")
detail_page = []
for each in x :
    detail_page.append(each.get("href"))

print(detail_page)