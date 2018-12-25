from urllib.request import urlopen
import pyexcel
from word import search_for

ini_url = "https://www.thesaurus.com/browse/"
user_input = search_for
url = ini_url + user_input
from bs4 import BeautifulSoup

conn = urlopen(url)
raw_data = conn.read()
webpage_text = raw_data.decode("utf-8")
soup = BeautifulSoup(webpage_text, "html.parser")

section = soup.find("section", {'class': "synonyms-container css-7jbvqm e1991neq0"})
ul      = section.find("ul")
li_list = ul.find_all("li")

symnonym_list = []
for ___ in range(0,8):
    span     = li_list[___].span
    a        = span.a

    symnonym = span.string
    symnonym_list.append(symnonym)


from translate import Translator
translator= Translator(to_lang="vi")


tu_dong_nghia = []
for symnonym in symnonym_list:
    translation = translator.translate(symnonym)
    if translation not in tu_dong_nghia and translation != symnonym:
        tu_dong_nghia.append(translation.capitalize())
print(tu_dong_nghia)