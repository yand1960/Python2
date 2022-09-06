# Скопировать в folder3  файлы из folder1, которых нет в папке folder2

import os
import shutil

# ------------  Укажите адреса трех папок -----------------
FOLDER1 = "data/folder1"
FOLDER2 = "data/folder2"
FOLDER3 = "data/folder3"
# -----------------------------------------------------------------

# commands = ["dir", "calc"]

os.system("CHCP 65001")

# for cmd in commands:
#     os.system(cmd)

files1 = os.listdir(FOLDER1)
files2 = os.listdir(FOLDER2)

unique_files =list(set(files1).difference(set(files2)))
# print(unique_files)

for file in unique_files:
    print(file) # copy <path1> <path2>
    # shutil.copy(f"data/folder1/{file}", f"data/folder3/{file}")
    src = f"{FOLDER1}/{file}".replace("/", "\\")
    target = f"{FOLDER3}/{file}".replace("/", "\\")
    command = f'copy "{src}" "{target}" '
    # print(command)
    os.system(command)
