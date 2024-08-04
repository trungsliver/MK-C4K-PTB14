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

arr = [5, 2, 8, 4, 6, 9, 1, 3]

    # Sắp xếp các phần tử danh sách
        # Sắp xếp tăng dần: sort()
arr.sort()

        # Sắp xếp giảm dần:
arr.sort(reverse=True)
print(arr)
