# Модуль по копированию оригинальных cr2 файлов в новую директорию, если аналогичные файлы jpg есть в целевом каталоге
# С начала указывается путь где лежат jpg файлы
# Потом указывается путь где лежат cr2 файлы
# Потом указывается путь куда будут копироваться cr2 файлы (каталог должен быть создан)
import os.path
import shutil
from colorama import Back, Style, init
from tqdm import tqdm

init()

try:
    # Вводим пути и проверяем их наличие
    print("Для выхода из программы наберите exit!!!!!")
    path_jpg, path_raw, new_path = "null", "null", "null"
    while not os.path.exists(path_jpg):
        path_jpg = input("Введите путь каталога с jpg: ")
        if path_jpg.lower() == "exit":
            exit()
    while not os.path.exists(path_raw):
        path_raw = input("Введите путь каталога с raw: ")
        if path_raw.lower() == "exit":
            exit()
    while not os.path.exists(new_path):
        new_path = input("Введите путь к папке куда будем копировать : ")
        if new_path.lower() == "exit":
            exit()

    # Создаём список из имён файлов jpg и убираем у них расширения
    list_jpg = [item[:-4] for item in os.listdir(path_jpg)]

    # Создаём счётчики файлов
    coped_cr2, coped_xmp = 0, 0

    # Цикл перебора файлов в списке и копирование (добавлен прогресс бар tqdm)
    for i in tqdm(list_jpg):
        if os.path.isfile(f"{path_raw}\\{i}.cr2"):
            shutil.copy(f"{path_raw}\\{i}.cr2", f"{new_path}\\{i}.cr2")
            coped_cr2 += 1
        if os.path.isfile(f"{path_raw}\\{i}.xmp"):
            shutil.copy(f"{path_raw}\\{i}.xmp", f"{new_path}\\{i}.xmp")
            coped_xmp += 1

    # Выводим информацию о количестве скопированных файлов
    print(f"\nСкопировано {coped_cr2} .cr2 файлов и {coped_xmp} .xmp файлов")
    print(f"Всего скопировано {coped_cr2 + coped_xmp} файла")
except FileNotFoundError:
    print(Back.RED, Style.BRIGHT + 'Файла или каталога не существует! '.upper() + Style.RESET_ALL)
except KeyboardInterrupt:
    print("\n", Back.RED, Style.BRIGHT + 'Неизвестная ошибка! '.upper() + Style.RESET_ALL)

input('\nPress ENTER to exit')
