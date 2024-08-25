# Bài 1: Viết một hàm sum_odd(numbers) để tính tổng các số lẻ trong một danh sách numbers.
# 	YC1: Hàm nhận vào một danh sách các số nguyên.
# 	YC2: Hàm trả về tổng các số lẻ trong danh sách đó.
def sum_odd(numbers):
    sum = 0
    for item in numbers:
        if item % 2 != 0:
            sum = sum + item
    return sum

num_list = [1, 2, 3, 4, 5]
# print(sum_odd(num_list))  # Output: 9

# Bài 2: Viết một hàm is_prime(n) để kiểm tra xem một số nguyên dương n có phải là số nguyên tố hay không.
# 	YC1: Hàm nhận vào một số nguyên dương n.
# 	YC2: Hàm trả về True nếu n là số nguyên tố, ngược lại trả về False.

def is_prime(n):
    count = 0
    for i in range(1, n + 1):
        if n % i == 0:
            count = count + 1
    if count == 2:
        return True
    else:
        return False

# print(is_prime(1))
# print(is_prime(2))
# print(is_prime(3))
# print(is_prime(4))


# Bài 3: Viết một hàm count_words(s) để đếm số lượng từ trong một chuỗi s.
# 	YC1: Hàm nhận vào một chuỗi ký tự s.
# 	YC2: Hàm trả về số lượng từ trong chuỗi đó.
def count_words(s):
    word_list = s.split()
    return len(word_list)

str1 = 'Hải meme siêu cấp vip pro'
print(count_words(str1))

# Bài 4: Viết một hàm sum_of_digits(n) để tính tổng các chữ số của một số nguyên dương n.
# 	YC1: Hàm nhận vào một số nguyên dương n.
# 	YC2: Hàm trả về tổng các chữ số của n.
def sum_of_digits(n):
    sum = 0
    while n > 0:
        sum = sum + n % 10
        n = n // 10
    return sum

# Bài 5: Viết một hàm find_max(numbers) để tìm vị trí số lớn nhất trong một danh sách numbers.
# 	YC1: Hàm nhận vào một danh sách các số nguyên.
# 	YC2: Hàm trả về vị trí số lớn nhất trong danh sách đó.
def find_max(numbers):
    max_index = 0
    for i in range(1, len(numbers)):
        if numbers[i] > numbers[max_index]:
            max_index = i
    return max_index

# Bài 6: Viết một hàm sum_to_n(n) để tính tổng các số từ 1 đến n.
# 	YC1: Hàm nhận vào một số nguyên dương n.
# 	Yc2: Hàm trả về tổng các số từ 1 đến n.
def sum_to_n(n):
    sum = 0
    for i in range(1, n + 1):
        sum = sum + i
    return sum

# Ôn tập

# Bài 1: Nhập từ bàn phím điểm trung bình của học sinh. Hãy xếp hạng học lực của học sinh đó, biết rằng:
# Giỏi: [8,10], Khá: [6.5, 8), TB: [5, 6.5), Yếu: [0, 5)

# Bài 2: Nhập từ bàn phím số giây cần chuyển đổi. In ra màn hình thời gian sau chuyển đổi, định dạng: giờ - phút - giây
# VD: 3661s = 1h 1m 1s

# Bài 3: Nhập 2 số nguyên a và b từ bàn phím
# Yêu cầu 1: In ra tất cả các số trong khoảng [a, b] hoặc ngược lại
# Yêu cầu 2: Tính tổng các số chẵn trong khoảng vừa in
# Yêu cầu 3: Tính trung bình cộng các số nguyên trong khoảng trên

# Bài 4: Viết hàm/chương trình con kiểm tra 1 số có phải là số nguyên tố hay không, biết rằng: số nguyên tố là số chỉ chia hết cho 1 và chính nó.
# In ra số nguyên tố trong khoảng [10,100].

# Bài 5: Nhập vào từ bàn phím 1 chuỗi ký tự bao gồm các số nguyên, các số này cách nhau 1 khoảng trắng (hoặc dấu ,).
# Yêu cầu 1: Tách chuỗi và thêm vào danh sách có tên num_list
# Yêu cầu 2: Chuyển đổi toàn bộ phần tử trong danh sách num_list thành kiểu dữ liệu int.
# Yêu cầu 3: In ra màn hình số lượng số lẻ của num_list.
# Yêu cầu 4: Sắp xếp các phần tử trong danh sách num_list theo thứ tự từ lớn đến nhỏ.

# Bài 6: Dùng thư viên random để thêm ngẫu nhiên các số nguyên trong khoảng [20,50] vào 2 danh sách arr1 và arr2. 
# Yếu cầu 1: Hãy viết hàm/chương trình con in ra phần tử chung của 2 danh sách vừa tạo.
# Yêu cầu 2: In ra màn hình vị trí phần tử nhỏ nhất của danh sách arr1
# Yêu cầu 3: In ra màn hình vị trí phần tử lớn nhất của danh sách arr2

# Bài 7: Hãy nhập từ bàn phím họ tên của bạn.
# Yêu cầu 1: Chuyển đổi chuỗi ký tự tên thành chuỗi ký tự viết hoa
# Yêu cầu 2: Chuyển đổi chuỗi ký tự tên thành chuỗi ký tự viết thường
# Yêu cầu 3: Chuyển đổi chuỗi ký tự tên thành chuỗi ký tự viết hoa các chữ cái đầu
