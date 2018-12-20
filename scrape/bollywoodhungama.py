import requests
import re
import threading
from bs4 import BeautifulSoup

seed_link = "http://www.bollywoodhungama.com/song-lyrics/char/NUM"

words_array = set()

def save_in_file(word_arr):
    print("************* Going to save info  *************")
    with open("bollywoodhungama_words.txt", "a") as f :
        for word in word_arr :
            f.write(word + "\n")

def scrape_song_lyrics(surl):
    # print("============================= Getting lyrics word of song : " + surl + " =============================")
    page = requests.get(surl)
    page.encoding= 'utf-8'
    soup = BeautifulSoup(page.text, 'html.parser')

    x = soup.select("div[class='song-lyrics-content entry-content post-content']")
    for each in x :
        text = each.get_text().replace("\n", " ")
        word_arr = set(re.split('\W+', text))

        temp_array = []
        for item in word_arr :
            if re.match('^[a-zA-z]+$', item) :
                temp_array.append(item)
            else :
                pass
        # print("333333")
        print(temp_array)
        word_arr = temp_array
        save_in_file(word_arr)

def scrape_movie_page(murl):
    # print("\n********************************** Getting lyrics word of movie : " + murl + " **********************************\n")
    page = requests.get(murl)
    page.encoding= 'utf-8'
    soup = BeautifulSoup(page.text, 'html.parser')

    x = soup.select("h3[itemprop='name'] a")
    # print("22222")
    # print(x)
    for each in x :
        song_link = each.get("href")
        scrape_song_lyrics(song_link)

def scrape_data(url):
    # print(" ========= " + url)
    page = requests.get(url)
    page.encoding= 'utf-8'
    soup = BeautifulSoup(page.text, 'html.parser')
    x = soup.select("li[role='listitem'] a ")
    # print(x)
    for each in x :
        link = each.get("href")
        # print(link)
        scrape_movie_page(link)

    next_link = soup.select("nav[class='bh-pagination clearfix right '] a[class='next page-numbers'] ")
    print("====== NEXT URL FOUND ======")
    if next_link is not None :
        for next_page in next_link:
            print("Going to scrape next URL  " + next_page.get("href"))
            scrape_data(next_page.get("href"))

start = 64
while (start < 91) :
    print("Running page with charchter " + chr(start))
    link = seed_link
    if start != 64 :
        link = seed_link.replace("NUM", chr(start))
    scrape_data(link)
    start = start + 1