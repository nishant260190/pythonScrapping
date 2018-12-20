import requests
import json
from pymongo import MongoClient
import csv
import threading
import os
import re
from bs4 import BeautifulSoup

seed_link = "https://9gag.com/v1/group-posts/group/"

cats = ["funny", "cute", "anime-manga", "ask9gag", "awesome", "basketball", "car", "comic", "cosplay", "country", "classicalartmemes", "imadedis", "drawing", "animefanart", "food", "football", "fortnite", "gaming", "girl", "girly", "guy", "history", "horror", "home", "kpop", "leagueoflegends", "lego", "movie-tv", "music", "overwatch", "pcmr", "photography", "pokemon", "politics", "relationship", "pubg", "roastme", "savage", "satisfying", "school", "science", "halloween", "starwars", "superhero", "surrealmemes", "sport", "travel", "timely", "warhammer", "wallpaper", "wtf", "darkhumor"]

tags_url = set()

try :
    # client = MongoClient("mongodb://admin:fgdnhg7tvkjchatbot@18.224.67.254:27017/")
    client = MongoClient("mongodb://18.224.67.254:27017/")
    db = client.abhinay
except Exception as ex :
    print(ex)

def save_in_text_file(data):
    print("****************** GOING TO SAVE IN FILE **********************")
    print(len(data))
    print("\n\n")
    with open("haha", "a") as f :
        for each in data :
            f.write(each + "\n")


def insert_data_in_mongo(arr):
    try :
        print("\n\n ****************** MONGO ************* \n\n")
        # print(arr)
        db.memdata.insert_many(arr, bypass_document_validation=True)
    except Exception as bwe:
        print(bwe)
        print(bwe.details)


def get_data_for_url(base_url, url):
    try :
        # print(base_url, url)
        print("hitting req for " + url)
        global tags_url
        page = requests.get(url)
        page.encoding= 'utf-8'
        # print("\n **************************** \n")
        # print(page.text)
        json_data = json.loads(page.text)
        # print(json_data)
        # print("111111111111111")
        if "data" in json_data:
            # print("22222222222222222222")
            if "posts" in json_data["data"] :
                # print("33333333333333333333333333333")
                posts_info = json_data["data"]["posts"]
                data = []
                for item in posts_info:
                    if "id" in item :
                        item_json = {}
                        item_json["id"] = item["id"]
                        item_json["9gag_url"] = item["url"]
                        item_json["title"] = item["title"]
                        item_json["category"] = item["type"]
                        item_json["upVoteCount"] = item["upVoteCount"]
                        item_json["ctime"] = item["creationTs"]
                        if "postSection" in item :
                            if item["postSection"]["imageUrl"] :
                                item_json["category_image"] = item["postSection"]["imageUrl"]
                        if "images" in item :
                            item_json["images"] = item["images"]

                        if "tags" in item:
                            for each in item["tags"]:
                                if "url" in each :
                                    # link = "https://9gag.com" + each["url"]
                                    cur_url = each["url"]
                                    if re.match("\/tag\/", cur_url) :
                                        # print("\n\n 1111111111111111111111\n\n")
                                        cur_url = "https://9gag.com/v1/tag-posts" + cur_url
                                        # print(cur_url)
                                    elif re.match("https?:\/\/9gag[.]com\/tag\/", cur_url) :
                                        # print("\n\n 2222222222222222222222222 \n\n")
                                        cur_url = cur_url.replace("https://9gag.com/tag/", "https://9gag.com/v1/tag-posts/tag/")
                                        # print(cur_url)
                                    else :
                                        cur_url = "https://9gag.com" + each["url"]
                                    tags_url.add(cur_url)

                    data.append(item_json)
                if len(data) > 0 :  
                    # print(data)       
                    insert_data_in_mongo(data)
            if "tags" in json_data["data"] :
                for each in json_data["data"]["tags"] :
                    if "url" in each :
                        cur_url = each["url"]

                        # print("<<<<<<<<<<<<<<<<<<< " + cur_url + " >>>>>>>>>>>>>>>>>>>>>>")
                        if re.match("\/tag\/", cur_url) :
                            # print("\n\n 1111111111111111111111\n\n")
                            cur_url = "https://9gag.com/v1/tag-posts" + cur_url
                            # print(cur_url)
                        elif re.match("https?:\/\/9gag[.]com\/tag\/", cur_url) :
                            # print("\n\n 2222222222222222222222222 \n\n")
                            cur_url = cur_url.replace("https://9gag.com/tag/", "https://9gag.com/v1/tag-posts/tag/")
                            # print(cur_url)
                        tags_url.add(cur_url)
            # print(len(tags_url))
            if len(tags_url) > 10 :
                save_in_text_file(tags_url)
                tags_url = set()

            if "nextCursor" in json_data["data"] :
                next_link = base_url.strip() + "?" + json_data["data"]["nextCursor"]
                # print("----")
                # print(next_link)
                get_data_for_url(base_url, next_link)
    except Exception as ex :
        print(ex)

def scrape_tags(thread_no, arr):
    for each in arr :
        print("Thread : " + str(thread_no) + " url is : " + each)
        get_data_for_url(each, each)

def read_tag_file():
    file_tag_urls = set()
    files = ["new_tags"]

    for fname in files :
        with open(fname, 'r') as f :
            content = f.readlines()
            for each in content:
                file_tag_urls.add(each)

            print("total tag links are : " + str(len(file_tag_urls)))

    # with open("tags4", 'w') as f:
    #     for each in file_tag_urls :
    #         f.write(each + "\n")


    file_tag_urls = list(file_tag_urls)
    start_threads(file_tag_urls, 20)

def start_threads(urls_arr, no_of_threads):
    start = 0
    end = 0
    per_thread_tags = int(len(urls_arr)/no_of_threads)
    print(per_thread_tags)
    thread_list = []
    for each in range(no_of_threads) :
        end = end + per_thread_tags
        # get_data_for_url(each, each)
        # print("--------------------///")
        # print(start)
        # print(end)
        # print(file_tag_urls[start : end])
        t = threading.Thread(target=scrape_tags, args=(each, urls_arr[start : end]));
        t.start();
        thread_list.append(t);
        start = end

    for thread in thread_list :
        thread.join()

def get_category():
    page = requests.get("https://9gag.com/")
    page.encoding= 'utf-8'
    soup = BeautifulSoup(page.text, 'html.parser')
    # print(page.text)
    x = soup.select("ul[class='section-picker'] li div[class='badge-upload-section-list-item-selector selector']")
    # print(x)
    urls = []
    for each in x:
        print(each.attrs['data-url'])
        hot_url = "https://9gag.com/v1/group-posts/group/" + each.attrs['data-url'] + "/type/hot"
        fresh_url = "https://9gag.com/v1/group-posts/group/" + each.attrs['data-url'] + "/type/fresh"
        urls.append(hot_url)
        urls.append(fresh_url)

    start_threads(urls, 20)

# read_tag_file()
get_category()