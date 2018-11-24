from urllib.request import urlopen
from collections import OrderedDict

url = "https://thesaurus.yourdictionary.com/eat"
from bs4 import BeautifulSoup

conn = urlopen(url)
raw_data = conn.read()
webpage_text = raw_data.decode("utf-8")
soup = BeautifulSoup(webpage_text, "html.parser")

div1        = soup.find("div",{'class': 'entry thes'})
div_list    = div1.find_all("div", {'class': 'text-info'})

symnomym_list = []
for div in div_list:
    symnonym = div.string
    symnomym_list.append(symnonym)

print(symnomym_list)