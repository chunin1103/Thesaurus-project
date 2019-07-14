from urllib.request import urlopen
# from word import search_for
from bs4 import BeautifulSoup
# from google.cloud import translate

# translate_client = translate.Client()
# target = 'vi'

def replaceMultiple(mainString, toBeReplaces, newString):
    # Iterate over the strings to be replaced
    for elem in toBeReplaces :
        # Check if string is in the main string
        if elem in mainString :
            # Replace the string
            mainString = mainString.replace(elem, newString)
    
    return  mainString


ini_url = "https://thesaurus.yourdictionary.com/"
# url = ini_url + search_for
url = ini_url + 'eat'

conn = urlopen(url)
raw_data = conn.read()
webpage_text = raw_data.decode("utf-8")
soup = BeautifulSoup(webpage_text, "html.parser")


p       = soup.find_all('p',{'class':'syn'})

sym_list = []
for p_item in p:
    a           = p_item.text
    list_p      = a.split(', ')
    for ____ in list_p:
        sym_list.append(____)

word_type = []
tu_loai_your_dict = soup.find_all('p', {'class':'pos'})
for __ in tu_loai_your_dict:
    a_1           = __.text
    for word in a_1:
        word_type = replaceMultiple(word, ['\r', '\n'] , "")
        word_type = ''.join(word_type)







print(tu_loai_your_dict)

print(sym_list)
    
print(word_type)

# ds_tu_dong_nghia = []
# for word in sym_list:
#         translation = translate_client.translate(
#         word,
#         target_language=target)
#         if translation != word.capitalize():
#                 ds_tu_dong_nghia.append(translation['translatedText'].capitalize())
# print(ds_tu_dong_nghia)