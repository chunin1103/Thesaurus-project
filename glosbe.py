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

symnomym_list = []

strong      = div1.find_all("strong")
for strr in strong:
    if strr is not None:
        symnomym_list.append(strr.string.capitalize())
print(symnomym_list)