# Danh sách - Array/List: 
# CRUD: Create - Read - Update - Delete
    # Create - Khởi tạo danh sách
arr = []
ptb14 = ['Nam', 'Tâm', 'Đức', 'Hải', 'Nguyên']

    # Read - Duyệt danh sách
        # len() - trả về kích thước/độ dài
# print(len(ptb14))
        # Hiện 1 phần tử bằng index
# print(ptb14[3])
        # Hiện phần tử cuối dùng: index = -1
# print(ptb14[-1])  

        # Duyệt toàn bộ phần tử
            # Cách 1: lấy cả index và value
# for i in range(len(ptb14)):     
#     print(f'[{i}] {ptb14[i]}')

            # Cách 2: chỉ lấy value
# for item in ptb14:
#     print(item)

        # In toàn bộ danh sách (dùng để test)
# print(ptb14)

    # Update - Cập nhật/Chỉnh sửa danh sách
        # Thêm phần tử vào cuối danh sách - append()
# ptb14.append('Hưng')

        # Thêm phần tử vào vị trí chỉ định - insert()
# ptb14.insert(3, 'Imposter')

        # Chỉnh sửa phần tử thông qua index
# ptb14[4] = 'meme'

    # Delete - Xóa phần tử danh sách
        # Xóa phần tử bằng giá trị - remove()
# ptb14.remove('Hưng')

        # Xóa phần tử bằng index - pop()
# ptb14.pop(3)

        # Xóa toàn bộ phần tử danh sách - clear()
# ptb14.clear()
# print(ptb14)

# arr = [5, 2, 8, 4, 6, 9, 1, 3]

    # Sắp xếp các phần tử danh sách
        # Sắp xếp tăng dần: sort()
# arr.sort()

        # Sắp xếp giảm dần:
# arr.sort(reverse=True)
# print(arr)

    # Tìm phần tử lớn nhất của danh sách - max()
# print(max(arr))

    # Tìm phần tử nhỏ nhất của danh sách - min()
# print(min(arr))

# ------------------ LUYỆN TẬP ----------------------
# Bài 1: Cho danh sách gồm các số nguyên liên tiếp từ 1 đến 15
    # YC1: In ra toàn bộ các phần tử của danh sách
    # YC2: In ra màn hình tổng các số chẵn
    # YC3: In ra màn hình số lượng số lẻ
    # YC4: In ra màn hình vị trí và giá trị của phần tử lớn nhất
    # YC5: In ra màn hình vị trí và giá trị của phần tử nhỏ nhất
    # YC6: Sắp xếp danh sách theo thứ tự giảm dần
                    # BÀI LÀM
    # YC1: In ra toàn bộ các phần tử của danh sách
arr = []
for i in range(1,16):
    arr.append(i)
print(arr)

    # YC2: In ra màn hình tổng các số chẵn
sum = 0
for item in arr:
    if item%2 == 0:
        sum = sum + item
print('Tổng các phần tử chẵn là:', sum)

    # YC3: In ra màn hình số lượng số lẻ
count = 0
for item in arr:
    if item%2 == 1:
        count = count + 1
print('Số lượng các phần tử lẻ là:', count)

    # YC4: In ra màn hình vị trí và giá trị của phần tử lớn nhất
max_item = max(arr)
for i in range(len(arr)):
    if arr[i] == max(arr):
        max_index = i
print('Giá trị phần tử lớn nhất:', max_item)
print('Vị trí phần tử lớn nhất:', max_index)

    # YC5: In ra màn hình vị trí và giá trị của phần tử nhỏ nhất
min_item = min(arr)
for i in range(len(arr)):
    if arr[i] == min(arr):
        min_index = i
print('Giá trị phần tử nhỏ nhất:', min_item)
print('Vị trí phần tử nhỏ nhất:', min_index)

    # YC6: Sắp xếp danh sách theo thứ tự giảm dần
arr.sort(reverse=True)
print(arr)