# Vòng lặp hữu hạn - Vòng lặp for

    # Hàm range(n): lặp từ 0 cho đến n-1
# for i in range(5):
#     print(i)

    # Hàm range(start, stop, step)
        # start: số bắt đầu (không bắt buộc, mặc định = 0)
        # stop: số kết thúc (bắt buộc)
        # step: bước nhảy (không bắt buộc, mặc định = 1)
# for i in range(1, 11, 2):
#     print(i)

# Ex1: range(stop)
# for i in range(5):
#     print(i)

# Ex2: range(start, stop)
# for i in range(2, 6):
#     print(i)

# Ex3: range(start, stop, step)
# for i in range(10, 21, 2):
#     print(i)

# Bài 1: Nhập 2 số nguyên a và b từ bàn phím
    # Yêu cầu: in ra tất cả các số nguyên trong khoảng [a, b] hoặc ngược lại
# a = int(input('Nhập a: '))
# b = int(input('Nhập b: '))

# if b >= a:
#     for i in range(a, b+1):
#         print(i)
# else:
#     for i in range(b, a+1):
#         print(i)

# Bài 2: Nhập 2 số nguyên a và b từ bàn phím
    # Yêu cầu: in ra tất cả các số chẵn trong khoảng [a, b] 
# a = int(input('Nhập a: '))
# b = int(input('Nhập b: '))

#     # Cách 1:
# for i in range(a, b+1):
#     if i%2 == 0:
#         print(i)

#     # Cách 2:
# if a%2 == 1:
#     a = a + 1
# for i in range(a, b+1, 2):
#     print(i)

# Sử dụng random
    # Khai báo thư viện
import random
    # Cú pháp sử dụng hàm trong thư viện: [Tên thư viện].[Tên hàm]
rd = random.randint(1,10)

# Yêu cầu: In ra màn hình bảng cửu chương của số vừa random: 5 * 1 = 5
for i in range(1, 11):
    print(f'{rd} * {i} = {rd*i}')

# Thứu tự index trong vòng for: i, j, k

# Bài tập: In bảng cửu chương từ 2 đến 9
for i in range(2,10):
    print('\nBảng cửu chương', i)
    for j in range(1, 11):
        print(f'{i} * {j} = {i*j}')