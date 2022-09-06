# Скопировать в folder3  файлы из folder1, которых нет в папке folder2
# Инкапсуляция классом

import os
import shutil


class FileProcessing:

    def __init__(self):
        os.system("CHCP 65001")

    def copy_unique_files(self, folder1, folder2, folder3):

        files1 = os.listdir(folder1)
        files2 = os.listdir(folder2)

        unique_files =list(set(files1).difference(set(files2)))

        for file in unique_files:
            print(file) # copy <path1> <path2>
            # shutil.copy(f"data/folder1/{file}", f"data/folder3/{file}")
            src = f"{folder1}/{file}".replace("/", "\\")
            target = f"{folder3}/{file}".replace("/", "\\")
            command = f'copy "{src}" "{target}" '
            os.system(command)


if __name__ == "__main__":
    FileProcessing().copy_unique_files("data/folder1", "data/folder2", "data/folder3")
