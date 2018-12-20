from urllib.request import Request, urlopen
import urllib
import re
import ssl

gcontext = ssl.SSLContext(ssl.PROTOCOL_TLSv1)
print("******************");
req = urllib.request.Request("https://shopee.co.id/ayana_market")
abc = urlopen(req, context=gcontext).read()
#regexMatch = re.findall(r"<h1.*?</h1>", str(abc));
#print(regexMatch);
print(abc)   
