import os, os.path, shutil
from tqdm import tqdm

path_jpg = input("Введите путь каталога с jpg: ")
path_raw = input("Введите путь каталога с raw: ")
new_path = input("Введите путь к папке куда будем копировать : ")

file_list_jpg = os.listdir(path_jpg)
new_list_jpg = [item[:-4] for item in file_list_jpg]

path_plus_file = f"{path_raw}\{new_list_jpg[10]}"
coped_cr2 = 0
coped_xmp = 0
for i in tqdm(new_list_jpg, dynamic_ncols=True):
    path_plus_file_cr2 = f"{path_raw}\{i}.cr2"
    path_plus_file_xmp = f"{path_raw}\{i}.xmp"
    path_final_file_cr2 = f"{new_path}\{i}.cr2"
    path_final_file_xmp = f"{new_path}\{i}.xmp"
    if os.path.isfile(path_plus_file_cr2):
        shutil.copy(path_plus_file_cr2, path_final_file_cr2)
        coped_cr2 += 1
    if os.path.isfile(path_plus_file_xmp):
        shutil.copy(path_plus_file_xmp, path_final_file_xmp)
        coped_xmp += 1

print(f"\nСкопировано {coped_cr2} .cr2 файлов и {coped_xmp} .xmp файлов")
print(f"Всего скопировано {coped_cr2 + coped_xmp} файла")