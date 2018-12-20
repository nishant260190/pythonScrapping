from urllib.request import Request, urlopen
import urllib.parse
import urllib
import re
import csv
import ssl
import json

print("******")
payload = {"usernames":["ayana_market"]};
params = urllib.parse.urlencode(payload)
print(params)
params = params.encode('utf-8')
print(params)
headers = {'authority' : 'shopee.co.id',
           'method' : 'POST',
           'path' : '/api/v1/shop_ids_by_username/',
           'scheme' : 'https',
           'accept' : 'application/json',
           'accept-encoding' : 'gzip, deflate, br',
           'accept-language' : 'en-GB,en-US;q=0.9,en;q=0.8',
           'content-length' :  30,
           'content-type' : 'application/json',
           'if-none-match' : '55b03-b89f7b4886c3728f8f6fc1dc5f6ef8f1',
           'origin' : 'https://shopee.co.id',
           'x-requested-with' : 'XMLHttpRequest',
           'x-csrftoken': 'GVgOUC3F9CpAjL7cXOCqJee9GHAJ6X4y',
           'x-api-source' : 'pc',
           'referer' : 'https://shopee.co.id/ayana_market',
           'user-agent' : 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36',
           'Cookie' : '_ga=GA1.3.1616093984.1523889392; cto_lwid=4edc511c-0c14-4426-ba91-814034616f4a; csrftoken=GVgOUC3F9CpAjL7cXOCqJee9GHAJ6X4y; SPC_IA=-1; SPC_U=-; SPC_EC=-; bannerShown=true; SPC_F=dYFP59kk1pxINcije78e7YN9a0bx0PVd; REC_T_ID=91f07f54-4183-11e8-954d-1866daacb4e1; SPC_T_ID="Tu1yNFYkRMdekGVlMzbQIioDx6BxlHSbH1BYeIdIaDJI9LZMJtsvxYNl4MUJRp2T9STR+p/bpKt9C4cmQVeMmU7MfnMhNHYaIzia0opXyzY="; SPC_T_IV="1bbttgeWgmZ5dq5Ra+nzbQ=="; SPC_SC_TK=; UYOMAPJWEMDGJ=; SPC_SC_UD=; SPC_SI=cubchp2wu55asqyftobb0802vrv4mwk7; _gid=GA1.3.841685964.1524499549; _gat=1'
}
try:
    print("1");
    req = urllib.request.Request("https://shopee.co.id/api/v1/shop_ids_by_username/", params, headers=headers)
    print("2");
    gcontext = ssl.SSLContext(ssl.PROTOCOL_TLSv1) 
    print("3")
    abc = urlopen(req, context=gcontext).read()
    print("ddddddddddd");
    print(abc);
    print("dasdsadasdasdasd");
    print(str(abc))
except Exception as e:
    print("exception :", e);
