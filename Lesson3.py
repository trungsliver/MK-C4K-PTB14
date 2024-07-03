# Chưa làm BTVN: Khoa Nguyên, Khải Hưng
# Chữa bài
# 1B 2A 3C 4D 5C 6A
# 7. name = "john" 8.A

# # Bài tập 1
#     # Khai báo biến với 3 kiểu dữ liệu khác nhau
# name = "Duc Trung"
# age = 25
# score = 9.5
#     # In dữ liệu bằng 3 cách khác nhau
# print('Họ tên: ' + name)
# print('Tuổi:', age)
# print(f'Tên: {name}. Tuổi: {age}. Điểm: {score}')

# Lệnh input() - nhập dữ liệu từ bàn phím
    # Khi nhập dữ liệu, ép kiểu về đúng kiểu dữ liệu
# name = str(input('Hãy nhập tên của bạn: '))
# age = int(input('Hãy nhập tuổi của bạn: '))
# score = float(input('Hãy nhập điểm của bạn: '))
# male = bool(input('Bạn có phải là nam không: '))

# Kiểm tra kiểu dữ liệu của biến số - type()
# a = 'Khoa Nguyen'
# b = 666
# c = 3.14
# d = False
# print(type(a), type(b), type(c), type(d))

# Chuyển đổi giữa các kiểu dữ liệu
    # Lệnh int() có chức năng chuyển đối số thực hoặc chuỗi chứa số nguyên
    # Lệnh int() không thể chuyển đổi được chuỗi chứa số thực
    # Lệnh float() dùng để chuyển đổi số nguyên và chuỗi ký tự
    # Lệnh str() có thể chuyển đổi tất cả các kiểu dữ liệu khác
    # int() và float() không thể chuyển đổi chuỗi có công thức
    # str() có thể chuyển đổi cả công thức
# a = "123"
# print(type(a))
# b = int(a)
# print(type(b))

# Các phép toán trong lập trình
    # Cộng - Trừ - Nhân - Chia (Tổng - Hiệu - Tích - Thương)
    # Chia lấy dư (%) 
    # Chia lấy nguyên (//)
    # Lũy thừa (**)
    # Thứ tự thực hiện phép tính: Lũy thừa - Nhân/Chia - Cộng/Trừ
# a = 45
# b = 6
# calculator = 3**2 + 15//4 - 22%3 
# print('Kết quả: ', calculator)


# Bài tập 1:
# print('Chào mừng bạn đến với Curency Converter - chuyển đổi tiền tệ')
# dollar = float(input('Vui lòng nhập số tiền cần chuyển (đô la Mỹ): $'))
# print('Số tiền được quy đổi ra Việt Nam đồng (VND)')
# vnd = dollar * 25000
# print(f'${dollar} quy đổi ra được {vnd}đ')

# Bài tập 2: Viết chương trình nhập vào một số nguyên s là số giây cần xử lý. 
# Hãy đối số giây cho trước thành số giờ, phút, giây và in kết quả ra màn hình.
# Gợi ý: Sử dụng các phép toán chia lấy nguyên và chia lấy số dư với cách chuyển đổi sau:
#  - 1 giờ = 3 600 giây 
# - 1 phút = 60 giây



