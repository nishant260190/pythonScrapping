import requests
import re
import threading
from bs4 import BeautifulSoup

seed_link = ["http://www.lyricsmint.com/", "http://www.lyricsmint.com/punjabi/"]


song_page = []

def save_in_file(word_arr):
    with open("lyricsmint_words.txt", "a") as f :
        for word in word_arr :
            f.write(word + "\n")

def scrape_song_page(url) :
    print("========== " + url + " ============")
    page = requests.get(url)
    page.encoding= 'utf-8'
    soup = BeautifulSoup(page.text, 'html.parser')

    global song_page
    x = soup.select("div[id='lyric']")
    for each in x :
        text = each.get_text().replace("\n", " ")
        word_arr = set(re.split('\W+', text))

        temp_array = []
        for item in word_arr :
            if re.match('^[a-zA-z]+$', item) :
                temp_array.append(item)
            else :
                pass
        print(temp_array)
        word_arr = temp_array
        save_in_file(word_arr)

def scrape_data(url):
    page = requests.get(url)
    page.encoding= 'utf-8'
    soup = BeautifulSoup(page.text, 'html.parser')

    global song_page
    x = soup.select("h2[class='post-title entry-title'] a ")
    
    for each in x :
        # print(each.get("href") + " \n")
        song_page.append(each.get("href"))

    x = soup.select("li[class='next right'] a")
    for each in x :
        scrape_data(each.get("href"))



for i in range(len(seed_link)):
    scrape_data(seed_link[i])
    # print("\n\n ==================== \n\n")
    print(len(song_page))

for each in song_page :
    scrape_song_page(each)
