# Скопировать в folder3  файлы из folder1, которых нет в папке folder2


import os

commands = ["dir", "calc"]

os.system("CHCP 65001")

# for cmd in commands:
#     os.system(cmd)

files1 = os.listdir("data/folder1")
files2 = os.listdir("data/folder2")

unique_files =list(set(files1).difference(set(files2)))
# print(unique_files)

for file in unique_files:
    # print(file) # copy <path1> <path2>
    pass
