import requests
from bs4 import BeautifulSoup

seed_link = "https://stockx.com/"
cat = "handbags"
sort_by = 'most-popular'

final_url = seed_link + cat + "/" + sort_by
detail_page_url_list = set()


def get_network_data(url):
    # print("Fetching data for URL : " + str(url))
    headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.130 Safari/537.36'}
    page = requests.get(url, headers=headers)
    page.encoding = 'utf-8'
    return page.text


def get_detail_page_url_from_listing_page(url):
    global detail_page_url_list
    data = get_network_data(url)
    soup = BeautifulSoup(data, 'html.parser')
    x = soup.select("div[class='tile browse-tile'] a")
    for each in x:
        detail_page_url_list.add('https://stockx.com' + each.attrs['href'])
    if len(detail_page_url_list) < 200:
        next_page = soup.select("a[class='pointer NavButton__NavigationButton-hkt558-0 dyMfjb']")
        if next_page is not None:
            for np in reversed(next_page):
                np = np.attrs['href']
                np_url = 'https://stockx.com' + np
                # print(np_url)
                get_detail_page_url_from_listing_page(np_url)
                break


get_detail_page_url_from_listing_page(final_url)
# print(detail_page_url_list)
# print(">>>>>>>>>>>>>")


def get_details_from_product_page(url):
    text_data = get_network_data(url)
    final_json = {}
    final_json["url"] = url
    soup = BeautifulSoup(text_data, 'html.parser')
    x = soup.select("ul[data-testid='product-breadcrumbs'] li")
    if x is not None and len(x) > 2:
        brand = x[2].text
        final_json["brand"] = brand
    price_tag = soup.select("ul[class='collapsible-table'] li span[class='inner-row']")
    for x in price_tag:
        labels = x.select("p[class='label']")
        for label in labels:
            if label.text.strip().lower() == 'retail':
                values = x.select("p[class='value']")
                for value in values:
                    final_json["retail_price"] = value.text

    lowest_ask = soup.select("div[class='bid bid-button-b'] a[class='button-container-b bid-button en-us'] div[class='en-us stat-value stat-small']")
    if lowest_ask is not None:
        for z in lowest_ask:
            final_json["ask"] = z.text
            break

    highest_bid = soup.select("div[class='ask ask-button-b'] a[class='button-container-b ask-button en-us'] div[class='en-us stat-value stat-small']")
    if highest_bid is not None:
        for z in highest_bid:
            final_json["bid_highest"] = z.text
            break

    gauges = soup.select("div[class='gauges'] div[class='gauge-container']")
    if gauges is not None:
        for gauge in gauges:
            title = gauge.select("div[class='gauge-title']")
            value = gauge.select("div[class='gauge-value']")
            if len(value) == 0:
                value = gauge.select("div[class='gauge-value-negative']")
            if title is not None and value is not None and len(title) > 0 and len(value) > 0:
                final_json[title[0].text] = value[0].text
    return final_json


final_output = []
counter = 1
for detail_page in detail_page_url_list:
    print("Fetching data for product " + str(counter) + " url is : " + detail_page)
    data = get_details_from_product_page(detail_page)
    final_output.append(data)
    counter = counter + 1
print(final_output)
