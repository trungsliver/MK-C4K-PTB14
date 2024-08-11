# Cấu trúc xâu ký tự - chuỗi (string): tương tự như danh sách
name = 'Hai meme'
    # Độ dài xâu
# print(len(name))
    # Duyệt các ký tự trong xâu (tương tự như danh sách)
        # Cách 1: có index và value
# for i in range(len(name)):
#     print(f'[{i}] {name[i]}')
        # Cách 2: chỉ có value
# for item in name:
#     print(item, end = ' ')

# Xâu con
# str1 = 'Hai'
# str2 = 'meme hihi'
    # Kiểm tra xâu con: in()
# print(str1 in name)
# print(str2 in name)
    # Tìm vị trí xâu con - find()
# print(name.find(str1))      # Tìm thấy => trả về vị trí
# print(name.find(str2))      # Không tìm thấy => trả về -1

# Một số thao tác với chuỗi
# name = 'Duc Trung sieu cap VipPro'
# for i in range(len(name)):
#      print(f'[{i}] {name[i]}')

    # Slicing - cắt chuỗi
        # Hiện từ vị trí 10 đến 17
# print(name[10:18])
        # Hiện từ vị trí 0 đến 8
# print(name[:9])
        # Hiện từ vị trí 19 đến hết
# print(name[19:])

    # Strip() - Xóa khoảng trắng ở đầu và cuối
# str1 = '           Khoa nguyen         '
# print(str1.strip())

    # Replace() - thay thế
        # replace(old, new)
# name = 'Đức đanh đá'
# name2 = name.replace('đanh đá', 'đú đởn')
# print(name2)
        # replace(old, new, count)
# name = 'Đức đanh đá đanh đá đanh đá đanh đá'
# name2 = name.replace('đanh đá', 'đú đởn', 2)
# print(name2)   

    # join() - kết hợp chuỗi
# ptb14 = ['BN', 'MT', 'MD', 'MH', 'KH', 'KN']
# print(' '.join(ptb14))

    # split() - tách chuỗi
# a = '1 2 3 4 5 6 7 8 9'
# arr = a.split()
# print(arr)

# b = 'a,b,c,d,e,f,g'
# arr2 = b.split(',')
# print(arr2)

# Định dạng chữ hoa, chữ thường
# name = 'mAncHeSteR uNitED'
    # Viết in hoa toàn bộ: upper()
# print(name.upper())
    # Viết thường toàn bộ: lower()
# print(name.lower())
    # Viết hoa chữ cái đầu: capwords()
# import string
# print(string.capwords(name))

# Chuyển đổi kiểu dữ liệu trong danh sách
a = '1 2 3 4 5 6 7 8 9'
arr = a.split()
print(arr)
    # Cách 1:
arr2 = []
for item in arr:
    a = int(item)
    arr2.append(a)
print(arr2)

    # Cách 2:
arr3 = [int(item) for item in arr]
print(arr3)

# Tính tổng phần tử danh sách
tong = sum(item for item in arr2)
print('Tổng phẩn tử danh sách:', tong)

# Tính tổng phần tử chẵn
tong_chan = sum(item for item in arr2 if item%2 == 0)
print('Tổng phần tử chẵn:', tong_chan)

# Đếm phần tử lẻ trong danh sách
dem_le = sum(1 for item in arr2 if item%2 == 1)
print('Số phần tử lẻ:', dem_le)

# Bài 1: Nhập vào 1 xâu ký tự định dạng dd/mm/yyyy (11/08/2024)
    # Tách ngày, tháng, năm và hiển thị ra màn hình