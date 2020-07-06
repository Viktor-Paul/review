# file_object = open("笔记", 'r', encoding="utf-8")
# print(file_object)
# print(file_object.fileno())
# # data = file_object.read()
# # print(data)
# for item in file_object:
#     print(item)
# file_object.close()

# with open("笔记", 'r', encoding="utf-8") as f:
#     print(f.fileno())
#     # print(f.tell())
#     # f.seek(20)
#     print(f.tell())
#     data = f.read()
#     print(data)
#     # print(f.tell())
#     print(f.fileno())

import os

# 1.查看文件列表
list01 = os.listdir(r"/review_2020_07")
print(list01)

# 2.获取文件的大小
size = os.path.getsize('file_operate.py')
print(size)

# 3.查看文件类型
temp = os.path.isdir(r"E:\python\review_2020_07")
print(temp)

# 4.查看文件是否存在
os.path.exists("")

# 5.删除文件
# os.remove(fil)
