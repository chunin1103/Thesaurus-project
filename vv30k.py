with open("vv30K.dict", encoding="utf8") as f:
    data = f.readlines()
# contents = myfile.read() 

tudien_tuloai ={
}
countttttt = 0          #đếm số từ có thể detect từ loại
count_word    = 0       #đếm số từ retrieved được
word_types  = {
    ' dt.'      : 'danh_tu!',
    ' d.'       : 'danh_tu!',
    ' đg.'      : 'dong_tu!',
    ' đgt.'     : 'dong_tu!',
    ' dg.'      : 'dong_tu!',
    ' Nh.'      : 'tu_long!',
    ' t.'       : 'tinh_tu!',
    ' tt.'      : 'tinh_tu!',
    ' c.'       : 'cam_than!',
    ' ph.'      : 'pho_tu!',
    ' đt.'      : 'dai_tu!',
    ' trt.'     : 'trang_tu',
    ' thgt.'    : 'thong_tuc',
    ' gt.'      : 'gioi_tu',
    ' st.'      : 'so_tu'    
}

for line in data:
    if '@' in line:
        word_process = line.split('@')          
        word = word_process[1].strip()          #2 steps to filter out clusters from the actual word
        count_word += 1
        tu_loai =[]

    # if count_word < 8:
    for i in word_types:
        if i in line:
            tu_loai.append(i)
            tudien_tuloai[word] = tu_loai    #cho từ loại tương ứng
            countttttt += 1

    # else:
    #     print('',end="")


print(tudien_tuloai)
f.close()
# print(contents) 
print(countttttt)
print(tudien_tuloai['a dua'])
