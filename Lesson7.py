# Vòng lặp vô hạn - while()
    # VD buổi trước:
# for i in range(6):
#     print(i)

    # Vòng lặp while
# i = 0
# while i <= 5:
#     print(i)
#     i =  i + 1  # i += 1

# Bài 1: Dùng vòng lặp while in ra màn hình các số nguyên từ 5 đến 10
# i = 5
# while i <= 10:
#     print(i)
#     i += 1

# Bài 2: Dùng vòng lặp while in ra màn hình các số chia hết cho 3 trong khoảng [5,25]
# i = 5
# while i <=25:
#     if i%3 == 0:
#         print(i)
#     i += 1

# Bài 3: Nhập số nguyên n trong khoảng [0,100]
    # Yêu cầu: nếu nhập sai (n<0 hoặc n>100) thì yêu cầu nhập lại
# n = int(input('Nhập số nguyên n trong khoảng [0,100]: '))
# while n<0 or n>100:
#     print('Bạn đã nhập sai, vui lòng nhập lại!')
#     n = int(input('\nNhập số nguyên n trong khoảng [0,100]: '))
# print('Nhập dữ liệu thành công!')

# Bài 4: Nhập vào số nguyên dương n. Tính tổng các chữ số của n.
n = int(input('Nhập số nguyên dương n: '))
sum = 0

while n > 0:
    sum = sum + n%10
    n = n // 10
print(f'Tổng các chữ số là: {sum}')