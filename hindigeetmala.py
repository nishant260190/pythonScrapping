import requests
import re
import threading
from bs4 import BeautifulSoup

seed_link = "https://www.hindigeetmala.net/movie/0-9.php"

words_array = set()

def save_in_file(word_arr):
    print("************* Going to save info  *************")
    with open("hindigeetmala_words_4.txt", "a") as f :
        for word in word_arr :
            f.write(word + "\n")

def scrape_song_lyrics(surl):
    try :
        print("============================= Getting lyrics word of song : " + surl + " =============================")
        page = requests.get(surl)
        page.encoding= 'utf-8'
        soup = BeautifulSoup(page.text, 'html.parser')

        x = soup.select("div[class='song'] span[itemprop='lyrics'] span[itemprop='text'] pre")
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

    except Exception as ex :
        print("Exception occured " + str(ex))

def scrape_movie_page(murl):
    try :
        print("\n********************************** Getting lyrics word of movie : " + murl + " **********************************\n")
        page = requests.get(murl)
        page.encoding= 'utf-8'
        soup = BeautifulSoup(page.text, 'html.parser')

        x = soup.select("table[class='b1 w760 pad2 allef'] a[itemprop='url']")
        # print("22222")
        # print(x)
        for each in x :
            song_link = "https://www.hindigeetmala.net" + each.get("href")
            scrape_song_lyrics(song_link)
    except Exception as ex :
        print("Exception occured " + str(ex))

def scrape_data(url):
    try :
        print(" ========= " + url)
        page = requests.get(url)
        page.encoding= 'utf-8'
        soup = BeautifulSoup(page.text, 'html.parser')
        x = soup.select("table[class='b1 w760 alcen'] td[class='w25p h150'] a[class='thumb']")
        # print("---------- movie page match " + str(x))
        threadList= []
        for each in x :
            link = each.get("href")
            # print(link)
            if link :
                link = "https://www.hindigeetmala.net" + link
                t = threading.Thread(target=scrape_movie_page, args=(link,));
                t.start();
                threadList.append(t);
                # scrape_movie_page(link)

        for thread in threadList:
            thread.join(); 

        next_link = soup.select("table[class='w784'] td[class='vatop w140'] a")
        # print("====== NEXT URL FOUND ======")
        # print(next_link)
        if next_link is not None :
            for next_page in next_link:
                if re.search("next page", str(next_page)) is not None:
                    print("\n\\\\\\\\\\\\\\\\\\\\\nGoing to scrape next URL  " + next_page.get("href"))
                    link = "https://www.hindigeetmala.net/movie/" + next_page.get("href")
                    scrape_data(link)
    except Exception as ex :
        print("Exception occured " + str(ex))


scrape_data(seed_link)

# threadList = []
# start = 64
# while (start < 91) :
#     print("Running page with charchter " + chr(start))
#     link = seed_link
#     if start != 64 :
#         link = seed_link.replace("0-9", chr(start))
#     # scrape_data(link)

#     t = threading.Thread(target=scrape_data, args=(link,));
#     t.start();
#     threadList.append(t);
#     start = start + 1


# for thread in threadList:
#     thread.join(); 