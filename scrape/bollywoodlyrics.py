import requests
import re
import threading
from bs4 import BeautifulSoup

seed_link = "https://www.bollywoodlyrics.com/"

words_array = set()


def save_in_file(word_arr):
    with open("final_words_data.txt", "a") as f :
        print("Going to save 10000 records")
        for word in word_arr :
            count = 
            f.write(word + "\n")

def scrape_song_lyrics(surl):
    print("============================= Getting lyrics word of song : " + surl + " =============================")
    page = requests.get(surl)
    page.encoding= 'utf-8'
    soup = BeautifulSoup(page.text, 'html.parser')

    x = soup.select("div[class='lyric-text margint20 marginb20'] pre[class='genericFont'] ")
    words = set()
    for each in x :
        text = each.get_text().replace("\n", " ")
        word_arr = set(re.split('\W+', text))
        words = words.union(word_arr)
    save_in_file(words)
     
# def scrape_movie_page(murl):
#     #print("\n********************************** Getting lyrics word of movie : " + murl + " **********************************\n")
#     page = requests.get(murl)
#     page.encoding= 'utf-8'
#     soup = BeautifulSoup(page.text, 'html.parser')

#     x = soup.select("ul[class='song_list'] h3[class='entry-title'] a")
#     print(x)
#     songslist = []
#     for each in x :
#         songslist.append(each.get('href'))

#     for each_song in songslist :
#         scrape_song_lyrics(each_song)
#     #     t = threading.Thread(target=scrape_song_lyrics, args=(each_song,));
#     #     t.start();
    #     threadList.append(t);
    # for thread in threadList:
    #     thread.join(); 

def scrape_data(url):
    print("------------- " + url)
    page = requests.get(url)
    page.encoding= 'utf-8'
    soup = BeautifulSoup(page.text, 'html.parser')

    x = soup.select("div[class='col-lg-8 col-sm-8'] div[class='list-line margint10 clearfix'] div[class='col-lg-6 col-sm-6 col-xs-6'] a")
    # print(x)
    for each in x :
        scrape_song_lyrics(each.get("href"))

    y = soup.select("div[class='row margint40'] div[class='col-lg-12'] div[class='custom-pagination'] ul[class='clearfix'] li a ")
    # print("????")
    # print(y)
    for each in y :
        if each.get_text().strip().lower() == 'next' :
            scrape_data(each.get("href"))


    # threadList = [];    
    # for each_movie in movies :
        # t = threading.Thread(target=scrape_movie_page, args=(each_movie,));
        # t.start();
        # threadList.append(t);
        # scrape_movie_page(each_movie)
 


    #for thread in threadList:
    #     thread.join(); 

# threadList = [];
start = 64
while (start < 91) :
    # print("Running page with charchter " + chr(start))
    link = seed_link + "alphabet?letter=numx"
    if start != 64 :
        link = seed_link + "alphabet?letter=" + chr(start)
    scrape_data(link)
    # t = threading.Thread(target=scrape_data, args=(link,));
    # t.start();
    # threadList.append(t);
    start = start + 1

# for thread in threadList:	
#     thread.join(); 
# print(words_array)

# with open("final_words_data.txt", "a") as f :
#     print("final left len of arr " + str(len(words_array)))
#     for word in words_array :
#         f.write(word.encode('utf-8') + "\n")


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
