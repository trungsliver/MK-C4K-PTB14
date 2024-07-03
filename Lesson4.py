# Kiểm tra chẵn lẻ
# number = int(input('Hãy nhập 1 số nguyên: '))

# if number % 2 == 0:
#     print(number, 'là số chẵn.')
# else:
#     print(number, 'là số lẻ.')

# Câu điều kiện
    # Câu điều kiện dạng thiếu:
# age = int(input('Hãy nhập tuổi của bạn: '))
# if age >= 18:
#     print('bạn đã đủ 18 tuổi.')

    # Câu điều kiện dạng đủ
# age = int(input('Hãy nhập tuổi của bạn: '))
# if age >= 18:
#     print('Bạn đã đủ 18 tuổi.')
# else:
#     print('Bạn chưa đủ 18 tuổi.')

    # Câu điều kiện đa nhánh
        # 8-10: Giỏi, 6.5-8: Khá, 5-6.5: Trung Bình, 0-5: Yếu
diem = float(input('Hãy nhập điểm của bạn: '))

if diem >= 8 and diem <= 10:
    print('Bạn được học sinh giỏi.')
elif diem >= 6.5 and diem < 8.0:
    print('Bạn được học sinh khá.')
elif diem >= 5 and diem < 6.5:
    print('Bạn được học sinh trung bình.')
elif diem >= 0 and diem < 5:
    print('Bạn được học sinh yếu.')
else:
    print('Bạn nhập sai dữ liệu.')

# Tính tiền điện
    # Nhập số kW đã sử dụng:
    # Quy tắc tính tiền điện:
        # Giá điện kW 0-100: 1500đ/kW
        # Giá điện kW 101-200: 2000đ/kw
        # Giá điện kw lớn hơn 200: 4000đ/kw
    # VD: sử dụng 50kw => tiền điện = 50 * 1500
    #       sử dụng 150kw => tiền điện = 100*1500 + 50*2000
    #       sử dụng 500kW => tiền điện = 100*1500 + 100*2000 + 300*4000

kw = float(input('Nhập số kW điện đã sử dụng: '))
cash = 0

if kw < 0:
    print('Bạn đã nhập sai dữ liệu.')
elif kw >= 0 and kw <= 100:
    cash = kw * 1500
elif kw > 100 and kw <= 200:
    cash = 100 * 1500 + (kw-100) * 2000
else:
    cash = 100 * 1500 + 100 * 2000 + (kw-200) * 4000

print('Số tiền cần trả là:', cash)
