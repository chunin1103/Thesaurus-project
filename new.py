string = '''Ngoài ra, theo ông Nguyễn Tuấn Anh, các vấn đề về kiểm soát cán bộ, công chức, đặc biệt là tài sản, thu nhập đã được đổi mới căn bản trong Luật. "Luật trước đây đã đề cập đến nội dung về minh bạch tài sản, thu nhập nhưng trên thực tế chưa thực sự quy củ và việc xác minh tài sản còn bị động. Với Luật mới, việc xác minh tài sản, thu nhập sẽ chủ động hơn", ông nói.

Cơ quan thanh tra được chủ động yêu cầu xác minh với những cá nhân, lãnh đạo có biến động tài sản bất thường khi kê khai; sử dụng cơ sở dữ liệu để theo dõi biến động tài sản, thu nhập.

"Trường hợp xác minh được những bất thường, cơ quan thanh tra, kiểm toán... sẽ làm rõ dấu hiệu vi phạm và chuyển sang cơ quan thuế hoặc cơ quan điều tra xử lý", ông Tuấn Anh nhấn mạnh.

Để phục vụ việc này

Theo ông, điều quan trọng là tích hợp cơ sở dữ liệu này với các hệ thống khác, như hệ thống tài khoản ở ngân hàng để chủ động đối soát khi cần thiết.

Cùng với đó, trong Luật đã quy định rõ trách nhiệm quản lý, khai thác dữ liệu và cơ quan nào được khai thác thông tin, đảm bảo chế độ bảo mật để tránh trường hợp dữ liệu bị lợi dụng. Hiện Thanh tra Chính phủ đang xây dựng các nghị định, thông tư để hướng dẫn cụ thể nội dung này.

Xây dựng lực lượng chuyên trách rà soát biến động tài sản, thu nhập

Thông tin về nội dung Luật giao Thanh tra Chính phủ kiểm soát tài sản, thu nhập của người giữ chức vụ từ Giám đốc sở và tương đương trở lên, ông Nguyễn Tuấn Anh nói, "nếu như trước đây Luật hoạt động theo cơ chế là các cơ quan tự quản lý và xử lý bản kê khai tài sản, thu nhập thì Luật này quy định rộng hơn".

Theo đó, Thanh tra Chính phủ, thanh tra tỉnh được quyền kiểm soát tài sản, thu nhập của cán bộ theo từng cấp. Các cơ quan này sẽ xây dựng đội ngũ chuyên trách làm nhiệm vụ rà soát thông tin, thu thập dữ liệu về biến động tài sản từ đó đề xuất cơ quan có thẩm quyền xác minh, xử lý.'''

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
        print(y)


