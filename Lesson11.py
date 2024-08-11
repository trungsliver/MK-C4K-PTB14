# Cấu trúc xâu ký tự - chuỗi (string): tương tự như danh sách
name = 'Hai meme'
    # Độ dài xâu
print(len(name))
    # Duyệt các ký tự trong xâu (tương tự như danh sách)
        # Cách 1: có index và value
for i in range(len(name)):
    print(f'[{i}] {name[i]}')
        # Cách 2: chỉ có value
for item in name:
    print(item, end = ' ')

print('\n',name[0])