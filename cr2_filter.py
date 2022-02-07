# Модуль по копированию оригинальных cr2 файлов в новую директорию, если аналогичные файлы jpg есть в целевом каталоге
# С начала указывается путь где лежат jpg файлы
# Потом указывается путь где лежат cr2 файлы
# Потом указывается путь куда будут копироваться cr2 файлы (каталог должен быть создан)
import os, os.path, shutil
from tqdm import tqdm

# Вводим пути
path_jpg = input("Введите путь каталога с jpg: ")
path_raw = input("Введите путь каталога с raw: ")
new_path = input("Введите путь к папке куда будем копировать : ")

# Создаём список из имён файлов jpg и убираем у них расширения
file_list_jpg = os.listdir(path_jpg)
new_list_jpg = [item[:-4] for item in file_list_jpg]

# Создаём счётчики файлов
coped_cr2 = 0
coped_xmp = 0

# Цикл перебора файлов в списке и копирование (добавлен прогрессбар tqdm)
for i in tqdm(new_list_jpg):
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

# Выводим информацию о колличестве скопированных файлов
print(f"\nСкопировано {coped_cr2} .cr2 файлов и {coped_xmp} .xmp файлов")
print(f"Всего скопировано {coped_cr2 + coped_xmp} файла")