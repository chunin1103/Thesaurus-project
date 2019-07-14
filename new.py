string = '''Ngoài ra, theo ông Nguyễn Tuấn Anh, các vấn đề về kiểm soát cán bộ, công chức, đặc biệt là tài sản, thu nhập đã được đổi mới căn bản trong Luật. "Luật trước đây đã đề cập đến nội dung về minh bạch tài sản, thu nhập nhưng trên thực tế chưa thực sự quy củ và việc xác minh tài sản còn bị động. Với Luật mới, việc xác minh tài sản, thu nhập sẽ chủ động hơn", ông n'''

sentence = (string.split())

phrase = []
for word in range(0,len(sentence)-1):
    phrase.append(sentence[word])
    phrase.append(sentence[word+1])

phrase_2 =[]
for i in range(0, len(phrase)-1,2):
    a = phrase[i] + ' ' + phrase[i+1]
    phrase_2.append(a)


for y in phrase_2:
    if phrase_2.count(y) > 2:
        print(y, end="                  ")


