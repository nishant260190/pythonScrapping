import requests
import re
import threading
from bs4 import BeautifulSoup

seed_link = "https://www.glamsham.com/o/music-lyrics?page="

words_array = set()

def save_in_file(word_arr):
    print("************* Going to save info  *************")
    with open("glamsham_words.txt", "a") as f :
        for word in word_arr :
            f.write(word + "\n")

def scrape_song_lyrics(surl):
    print("============================= Getting lyrics word of song : " + surl + " =============================")
    page = requests.get(surl)
    page.encoding= 'utf-8'
    soup = BeautifulSoup(page.text, 'html.parser')

    x = soup.select("div[class='col-md-12 pageCaption']")
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

# def scrape_movie_page(murl):
#     print("\n********************************** Getting lyrics word of movie : " + murl + " **********************************\n")
#     page = requests.get(murl)
#     page.encoding= 'utf-8'
#     soup = BeautifulSoup(page.text, 'html.parser')

#     x = soup.select("ul[class='lyrics-section-ul'] li a")
#     print("22222")
#     print(x)
#     for each in x :
#         song_link = "https://www.glamsham.com" + each.get("href")
#         scrape_song_lyrics(song_link)

def scrape_data(url):
    print(" ========= " + url)
    page = requests.get(url)
    page.encoding= 'utf-8'
    soup = BeautifulSoup(page.text, 'html.parser')
    x = soup.select("div[class='container-fluid'] div[class='row'] div[class='col-md-8'] div[class='col-md-12'] div[class='row'] div[class='row'] a ")
    # print(x)
    for each in x :
        link = each.get("href")
        if re.match("/o/music-lyrics/", link) is not None:
            link = "https://www.glamsham.com" + link
            print(link)
            scrape_song_lyrics(link)

start = 65
while (start < 91) :
    # print("Running page with charchter " + chr(start))
    link = seed_link + chr(start)
    print(link)
    scrape_data(link)
    start = start + 1