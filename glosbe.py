from urllib.request import urlopen
from collections import OrderedDict
from word import search_for

ini_url = "https://vi.glosbe.com/en/vi/"
url     = ini_url + search_for
from bs4 import BeautifulSoup

conn = urlopen(url)
raw_data = conn.read()
webpage_text = raw_data.decode("utf-8")
soup = BeautifulSoup(webpage_text, "html.parser")

div1        = soup.find("div",{'id': 'phraseTranslation'})
div_list    = div1.find_all("div", {'class': 'text-info'})

symnomym_list = []
for div in div_list:
    symnonym = div.string
    if symnonym is not None:
        symnomym_list.append(symnonym.capitalize())

print(symnomym_list)