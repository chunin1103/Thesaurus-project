from poll import Poll
import mlab
from word import search_for
from crawl_data_Onelook import tu_dong_nghia
from translate import Translator
translator= Translator(to_lang="vi")
from crawl_data_Onelook import *
from glosbe import *
from crawl_thesaurus import*



def common_member(a, b, c): 
      
    a_set = set(a) 
    b_set = list(b) + list(c)
      
    if len(a_set.intersection(b_set)) > 0: 
        return(a_set.intersection(b_set))   
    else: 
        return("no common elements") 
tu_tuong_dong    = list(common_member(ds_tu_dong_nghia,symnomym_list,tu_dong_nghia))
merge_list       = ds_tu_dong_nghia + tu_dong_nghia + symnomym_list  
set_tu_lap_lai   = set([item for item in merge_list if merge_list.count(item) > 1])
tu_lap_lai       = list(set_tu_lap_lai)

final_list = []
for _1 in tu_tuong_dong:
    final_list.append(_1)
for _2 in tu_lap_lai:
    if _2 not in tu_tuong_dong:
        final_list.append(_2)
for _3 in merge_list:
    if _3 not in tu_tuong_dong and _3 not in tu_lap_lai:
        final_list.append(_3)

print(final_list)
    

mlab.connect()

u           = search_for
u_trans     = translator.translate(u).lower()
# url_list  = ini_url # + Translator

p = Poll(user_input=u, input_trans=u_trans, symnonyms=tu_dong_nghia, symnonyms_trans=final_list, url_list="Onelook, glosbe, thesaurus")

p.save()


