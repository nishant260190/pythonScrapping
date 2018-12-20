from urllib.request import urlopen
import urllib
import re
import csv
finalplinks =[]
furniture_data = []
def clean(x, loc=2):
    return str(x)[loc:][:-loc]

f = open('external_harddisk.txt', 'w')
for i in range(1,580,16):
    try:       
        #print("http://www.flipkart.com/lc/pr/pv1/spotList1/spot1/productList?sid=jek%2Cp31%2Ctrv&pincode=110003&filterNone=true&start=21")
        #http://www.flipkart.com/lc/pr/pv1/spotList1/spot1/productList?sid=6bo%2Cjdy%2Cnl6&pincode=110003&filterNone=true&start=16
        with urlopen("http://www.flipkart.com/lc/pr/pv1/spotList1/spot1/productList?sid=6bo%2Cjdy%2Cnl6&pincode=110003&filterNone=true&start="+str(i)+"") as response:
            abc = response.read();
            match = re.findall(r'(?is)prd_title".*?href=".*?"', str(abc));
            #print (match)
            for links in match:
                link = re.sub(r'(?is)prd_title".*?href="(.*?)"',r'http://www.flipkart.com\1',str(links));
                #print (link)
                #print (i)
                f.write(str(link) + '\n')
    except Exception as e:
          print("%s%s" % (str(e), str(i)))
print (i)     
f.close()
           
