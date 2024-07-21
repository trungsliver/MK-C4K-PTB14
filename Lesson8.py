# Bài 1: Kiểm tra số nguyên tố
# n = int(input('Nhập 1 số nguyên: '))
# check = True
# if n < 2:
#     check = False
# elif n ==2:
#     check = True
# else:
#     for i in range(2,n):
#         if n%i == 0:
#             check = False

# if check == True:
#     print(n, 'là số nguyên tố')
# else:
#     print(n, 'không phải là số nguyên tố')

# Bài 2: Tính tổng các số chẵn trong khoảng [0,100]
# sum = 0
# for i in range(0,101):
#     if i%2 == 0:
#         sum = sum + i
# print('Tổng các số chẵn:', sum)

# Bài 3: Tính tổng số nguyên tố trong khoảng [10,20]
sum = 0
for i in range(10,21):
    check = True
    if i < 2: check = False
    elif i ==2: check = True
    else:
        for j in range(2,i):
            if i%j == 0:
                check = False
    if check == True:
        sum = sum + i
print('Tổng các số nguyên tố:', sum)