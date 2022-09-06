# Скопировать в folder3  файлы из folder1, которых нет в папке folder2
# Процедурная инкапсуляция

import os
import shutil


def copy_unique_files(folder1, folder2, folder3):

    # commands = ["dir", "calc"]

    os.system("CHCP 65001")

    # for cmd in commands:
    #     os.system(cmd)

    files1 = os.listdir(folder1)
    files2 = os.listdir(folder2)

    unique_files =list(set(files1).difference(set(files2)))
    # print(unique_files)

    for file in unique_files:
        print(file) # copy <path1> <path2>
        # shutil.copy(f"data/folder1/{file}", f"data/folder3/{file}")
        src = f"{folder1}/{file}".replace("/", "\\")
        target = f"{folder3}/{file}".replace("/", "\\")
        command = f'copy "{src}" "{target}" '
        os.system(command)


if __name__ == "__main__":
    copy_unique_files("data/folder1", "data/folder2", "data/folder3")


