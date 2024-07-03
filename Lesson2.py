# Variables - Biến số
    # Cách khai báo biến: [Tên biến] = [Giá trị]
x = 10
y = 21
    # Cách khai báo nhiều biến 1 lúc
a, b, c = 5, 6, 7

# Data Types - Kiểu dữ liệu
    # String: chuỗi ký tự, được đặt trong dấu nháy
name = 'Bui Duc Trung'
    # Int: số nguyên - số không có phần thập phân
age = 25
    # Float: số thực - số có phần thập phân
score = 2.5
    # Bool/Boolean: True/False - Đúng/Sai
male = True
# wear glasses = True

# Quy tắc đặt tên biến
    # - Chỉ gồm chữ cái tiếng anh, số, dấu gạch dưới
    # - Không bắt đầu bằng số, không chứa dấu cách/khoảng trắng
    # - Phân biệt chữ hoa và chữ thường
    # - Không dùng từ khóa để đặt tên biến

    # Ví dụ: đặt tên biến
        # Đúng: duck, pen, pin, khoa, sai, dung, name
        # Sai: wear glasses, cái, 123hung, nguyên, s a i, đúng, if

# Xác định kiểu dữ liệu - type()
# print(type(name))
# print(type(age))
# print(type(score))
# print(type(male))

# Xác định kiểu dữ liệu khi nhập vào 
# name = str(input('Hãy nhập tên của bạn: '))
# age = int(input('Hãy nhập tuổi của bạn: '))
# score = float(input('hãy nhập điểm của bạn: '))
# male = bool(input('Bạn có phải làm nam không (True/False): '))

# Hiển thị dữ liệu ra màn hình
# print(f'Họ tên: {name}')
# print('Tuổi:', age)
# print('Điểm: ' + str(score))
# print('Giới tính nam:', male)

# Bài tập 1: Nhập chiều cao và độ dài đáy của tam giác. Tính diện tích tam giác.
print('\nTính diện tích tam giác')
a = float(input('Nhập độ dài đáy: '))
h = float(input('Nhập Chiều cao: '))

s = (a*h)/2         # Công thức tính diện tích tam giác
print('\nDiện tích tam giác:', s)

# Bài tập 2: Nhập chiều dài và chiều rộng của HCN. Tính chu vi và diện tích HCN.
print('\nTính diện tích hình chữ nhật')
a = float(input('Nhập chiều dài: '))
b = float(input('Nhập chiều rộng: '))

p = (a+b)*2         # Công thức tính chu vi HCN
s = a*b         # Công thức tính diện tích HCN
print('\nChu vi HCN:', p)
print('Diện tích HCN:', s)
