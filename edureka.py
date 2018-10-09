import requests
import re


class edureka:
    def scrapeInfo(self):
        print("edureka")
        l='https://www.edureka.co/blog/interview-questions/blockchain-interview-questions/'
        req= requests.get(l)
        req.encoding= 'utf-8'
        mac = re.findall(r'(<h3[^>]*>\s*|<p[^>]*>\s*|<span[^>]*>\s*|<strong[^>]*>\s*){3,4}(Q\s*[0-9]+[^<]+)(<\/h3>[^<]*\s*|<\/p>[^<]*\s*|<\/span>[^<]*\s*|<\/strong>[^<]*\s*){3,4}\s*<p[^>]*>.*?<span[^>]+>(.*?)<\/span>',req.text)
        data = []   
        for item in mac:
            f_json = {} 
            f_json['Terms'] = re.sub(r'<[^>]+>|Â','',item[1])
            f_json['Definition'] = re.sub(r'<[^>]+>|Â', "", item[3])
            data.append(f_json)
        return data
#edu = edureka()
#edu.scarpeInfo()
