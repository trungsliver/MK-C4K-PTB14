# Hàm - Chương trình con
    # Hàm không có giá trị trả về
def say_hello():
    print('Xin chào Đức Trung!')
    print('Xin chào Hải meme')
        # Cách sử dụng hàm:
# say_hello()

    # Hàm có giá trị trả về
def areaHCN():
    a = float(input('Nhập chiều dài: '))
    b = float(input('Nhập chiều rộng: '))
    return a * b
        # Hàm có giá trị trả về có thể sử dụng như biến
# print(areaHCN())

    # Hàm có giá trị truyền vào
def avg3(a, b, c):
    return (a + b + c) / 3
# print('TBC:', avg3(10, 20, 30))

    # Ép kiểu cho biến trong hàm
def abs_float(n:float):
    if n >= 0:
        return n
    else:
        return -n 
# print(abs_float(-5), abs_float(2), abs_float(-6.9696969))

# =============== BÀI TẬP ===============
# Bài 1: Viết một hàm sum_odd(numbers) để tính tổng các số lẻ trong một danh sách numbers.
# 	YC1: Hàm nhận vào một danh sách các số nguyên.
# 	YC2: Hàm trả về tổng các số lẻ trong danh sách đó.

# Bài 2: Viết một hàm is_prime(n) để kiểm tra xem một số nguyên dương n có phải là số nguyên tố hay không.
# 	YC1: Hàm nhận vào một số nguyên dương n.
# 	YC2: Hàm trả về True nếu n là số nguyên tố, ngược lại trả về False.

# Bài 3: Viết một hàm count_words(s) để đếm số lượng từ trong một chuỗi s.
# 	YC1: Hàm nhận vào một chuỗi ký tự s.
# 	YC2: Hàm trả về số lượng từ trong chuỗi đó.

# Bài 4: Viết một hàm sum_of_digits(n) để tính tổng các chữ số của một số nguyên dương n.
# 	YC1: Hàm nhận vào một số nguyên dương n.
# 	YC2: Hàm trả về tổng các chữ số của n.

# Bài 5: Viết một hàm find_max(numbers) để tìm vị trí số lớn nhất trong một danh sách numbers.
# 	YC1: Hàm nhận vào một danh sách các số nguyên.
# 	YC2: Hàm trả về vị trí số lớn nhất trong danh sách đó.

# Bài 6: Viết một hàm sum_to_n(n) để tính tổng các số từ 1 đến n.
# 	YC1: Hàm nhận vào một số nguyên dương n.
# 	Yc2: Hàm trả về tổng các số từ 1 đến n.

