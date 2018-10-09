import requests
import re
import threading
from bs4 import BeautifulSoup

seed_link = "http://smriti.com/hindi-songs/movies-"

words_array = set()

def save_in_file(word_arr):
    with open("smriti_words.txt", "a") as f :
        for word in word_arr :
            f.write(word.encode('utf-8') + "\n")

def get_headers():
    headers = {
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
        "Accept-Encoding": "gzip, deflate",
        "Accept-Language": "en-GB,en-US;q=0.9,en;q=0.8",
        "Cache-Control": "max-age=0",
        "Connection": "keep-alive",
        "Cookie": "__utmc=137418162; __utmz=137418162.1538491313.1.1.utmcsr=google|utmccn=(organic)|utmcmd=organic|utmctr=(not%20provided); __utma=137418162.1172821933.1538491313.1538491313.1538491313.1; __utmt=1; __utmb=137418162.29.10.1538491313",
        "Host": "smriti.com",
        "Upgrade-Insecure-Requests": "1",
        "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.75 Safari/537.36"
    }
    return headers


def save_in_file(word_arr):
    with open("smriti_words.txt", "a") as f :
        for word in word_arr :
            f.write(word + "\n")

def scrape_song_lyrics(surl):
    print("============================= Getting lyrics word of song : " + surl + " =============================")
    page = requests.get(surl)
    page.encoding= 'utf-8'
    soup = BeautifulSoup(page.text, 'html.parser')
    # print(page.text)
    x = soup.select("div[class='songbody']")
    # print(x)
    for each in x :
        text = each.get_text().replace("\n", " ")
        word_arr = set(re.split('\W+', text))

        temp_array = []
        for item in word_arr :
            if re.match('^[a-zA-z]+$', item) :
                temp_array.append(item)
            else :
                pass
        # print(temp_array)
        word_arr = temp_array
        save_in_file(word_arr)
    

def scrape_movie_page(murl):
    # print("\n********************************** Getting lyrics word of movie : " + murl + " **********************************\n")
    page = requests.get(murl)
    page.encoding= 'utf-8'
    soup = BeautifulSoup(page.text, 'html.parser')

    x = soup.select("div[class='onesong'] a")
    for each in x :
        text = each.get_text().strip()
        if text == "text" :
            song_link = "http://smriti.com" + each.get('href')
            # print(":::::::::::::::: " + song_link)
            scrape_song_lyrics(song_link)
        else :
            pass
            # print(" ????? url recvd is : " + each.get('href'))

def scrape_data(url):
    # print("============ url : " + url)
    page = requests.get(url)
    page.encoding= 'utf-8'
    soup = BeautifulSoup(page.text, 'html.parser')

    x = soup.select("div[class='latest'] a ")
    movies = []
    for each in x :
        link = each.get("href")
        if re.search("/hindi-songs/movie", link) is not None :    
            movie_link = "http://smriti.com" + link
            scrape_movie_page(movie_link)
            # print("<<<<< " + movie_link)
        else :
            pass
            # print("????? " + link)

    # threadList = [];    
    # for each_movie in movies :
    #     # t = threading.Thread(target=scrape_movie_page, args=(each_movie,));
    #     # t.start();
    #     # threadList.append(t);
    #     scrape_movie_page(each_movie)

    # # for thread in threadList:
    # #     thread.join(); 

threadList = [];
start = 96
while (start < 123) :
    print("Running page with charchter " + chr(start))
    link = seed_link + "1"
    if start != 96 :
        link = seed_link + chr(start)
    t = threading.Thread(target=scrape_data, args=(link,));
    t.start();
    threadList.append(t);
    start = start + 1

for thread in threadList:
    thread.join(); 

# with open("final_words_data.txt", "a") as f :
#     print("final left len of arr " + str(words_array))
#     for word in words_array :
#         f.write(word.encode('utf-8') + "\n")
