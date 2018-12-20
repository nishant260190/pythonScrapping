import requests
import re
import threading
from bs4 import BeautifulSoup

seed_link = "https://www.lyricsbogie.com/category/movies"

words_array = set()

def save_in_file(word_arr):
    with open("final_words_data.txt", "a") as f :
        for word in word_arr :
            f.write(word.encode('utf-8') + "\n")

def scrape_song_lyrics(surl):
    # print("============================= Getting lyrics word of song : " + surl + " =============================")
    page = requests.get(surl)
    page.encoding= 'utf-8'
    soup = BeautifulSoup(page.text, 'html.parser')
    global words_array

    x = soup.select("div[id='lyricsDiv']")
    words = []
    for each in x :
        text = each.get_text().replace("\n", " ")
        word_arr = set(re.split('\W+', text))
        words_array = words_array.union(word_arr)
    if len(words_array) > 10000 :
        print("Saving 10000 words")
        save_in_file(words_array)
        words_array = set()

def scrape_movie_page(murl):
    print("\n********************************** Getting lyrics word of movie : " + murl + " **********************************\n")
    page = requests.get(murl)
    page.encoding= 'utf-8'
    soup = BeautifulSoup(page.text, 'html.parser')

    x = soup.select("ul[class='song_list'] h3[class='entry-title'] a")
    songslist = []
    for each in x :
        songslist.append(each.get('href'))

    for each_song in songslist :
        scrape_song_lyrics(each_song)
    #     t = threading.Thread(target=scrape_song_lyrics, args=(each_song,));
    #     t.start();
    #     threadList.append(t);
    # for thread in threadList:
    #     thread.join(); 

def scrape_data(url):
    page = requests.get(url)
    page.encoding= 'utf-8'
    soup = BeautifulSoup(page.text, 'html.parser')

    x = soup.select("ul[class='cat_list'] li a ")
    movies = []
    for each in x :
        movies.append(each.get("href"))

    threadList = [];    
    for each_movie in movies :
        # t = threading.Thread(target=scrape_movie_page, args=(each_movie,));
        # t.start();
        # threadList.append(t);
        scrape_movie_page(each_movie)

    # for thread in threadList:
    #     thread.join(); 

threadList = [];
start = 96
while (start < 123) :
    print("Running page with charchter " + chr(start))
    link = seed_link
    if start != 96 :
        link = seed_link + "/" + chr(start)
    # scrape_data(link)
    t = threading.Thread(target=scrape_data, args=(link,));
    t.start();
    threadList.append(t);
    start = start + 1

for thread in threadList:
    thread.join(); 
# print(words_array)

with open("final_words_data.txt", "a") as f :
    print("final left len of arr " + str(words_array))
    for word in words_array :
        f.write(word.encode('utf-8') + "\n")


# uniqueWords = []
# with open("final_2.txt", "r") as f :
#     content = f.readlines()
#     for x in content :
#         uniqueWords.append(x.strip())
# uniqueWords = list(set(uniqueWords))

# print("after final2 " + str(len(uniqueWords)))

# with open("final_1.txt", "r") as f :
#     content = f.readlines()
#     for x in content :
#         uniqueWords.append(x.strip())
# uniqueWords = list(set(uniqueWords))

# print("after final1 " + str(len(uniqueWords)))

# with open("final_words_data.txt", "r") as f :
#     content = f.readlines()
#     for x in content :
#         uniqueWords.append(x.strip())
# uniqueWords = list(set(uniqueWords))

# print("after final3 " + str(len(uniqueWords)))


# uniqueWords = list(set(uniqueWords))

# with open("unique_words_data.txt", "w") as f :
#     for word in uniqueWords :
#         f.write(word.encode('utf-8') + "\n")