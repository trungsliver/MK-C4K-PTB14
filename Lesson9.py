# Quy tắc đặt tên file: [Tên lớp]_[Họ tên]_CP2.py
# VD: PTB14_BuiDucTrung_CP2.py

# Hạn nộp: 09:25 ngày 28/07/2024
# Lưu ý: khi gửi bài, gửi riêng qua zalo, không gửi bài vào nhóm

# Đánh dấu bài:
    # Khoa Nguyên: 2
    # Khải Hưng: chat gpt - chưa gửi BTVN
    # Minh Tâm:
    # Minh Đức:
    # Minh Hải:
    # Bảo Nam:

# Danh sách - Array/List
    # Thao tác CRUD: Create - Read - Update - Delete

    # Create - Tạo danh sách
        # Danh sách trống (không có phần tử nào)
arr = []
        # Danh sách có sẵn phần tử
ptb14 = ['Khoa Nguyên', 'Khải Hưng', 'Minh Tâm', 'Minh Đức', 'Hải meme']
        # Hàm len() - trả về độ dài danh sách
print(len(ptb14))

    # Read - Hiển thị, duyệt danh sách
        # Hiển thị 1 phần tử bằng chỉ số index (đếm từ 0)
print(ptb14[2])
        # Hiển thị phần tử cuối cùng: index = -1
print(ptb14[-1])

        # Các cách duyệt, hiển thị toàn bộ phần tử trong danh sách
            # Cách 1: lấy cả index và value
for i in range(len(ptb14)):
    print(f'[{i}] {ptb14[i]}')

            # Cách 2: chỉ lấy value
for item in ptb14:
    print(item)

            # Cách 3: để test chương trình
print(ptb14)
