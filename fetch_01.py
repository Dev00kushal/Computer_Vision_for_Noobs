import requests
import json
from bs4 import BeautifulSoup
        
def fetch_data_file(url,path):
     r = requests.get(url)
     with open(path, "w") as f:
        f.write(r.text)

url = "https://www.wlv.ac.uk/"

fetch_data_file(url,"Data/wlv.html")    