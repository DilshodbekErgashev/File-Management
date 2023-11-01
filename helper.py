from pathlib import Path
from PIL import Image
import pathlib
import os
class FileManagement:
    def __init__(self, cwd):
        self.cwd = cwd

    def print_menu(self):
        print("========================================")
        print("1️⃣  ✦ Список файлов в текущем каталоге")
        print("2️⃣  ✦ Создание нового файла")
        print("3️⃣  ✦ Создание новой папки")
        print("4️⃣  ✦ Удаление файла")
        print("5️⃣  ✦ Удаление папки")
        print("6️⃣  ✦ Переименование файла или папки")
        print("7️⃣  ✦ Отображение изображения")
        print("8️⃣  ✦ Изменение текущей папки")
        print("0️⃣  ✦ Выход")
        print("========================================")

    def list_files(self):
        print(f"Listing files at {self.cwd}")
        files = os.listdir(self.cwd)
        for file in files:
            print(file)

    def create_file(self):
        file_name = input("Введите имя файла, который нужно создать: ")
        file_path = os.path.join(self.cwd, file_name)
        print(f"Создается файл: {file_path}")

        try:
            file = open(file_path, "w")
            file.close()
            print("Файл успешно создан.")
    
        except Exception as e:
            print(f"Ошибка при создании файла: {str(e)}")
        
    def create_folder(self):
        folder_name = input("Введите имя новой папки: ") 
        folder_path = Path(self.cwd) / folder_name 
        folder_path.mkdir()
        print(f"Создана новая папка: {folder_path}")
    
    def delete_file(self):
        file_name = input("Введите имя файла, который нужно удалить: ")
        file_path = os.path.join(self.cwd, file_name)
        try:
            os.remove(file_path)
            print(f"Удален файл: {file_path}")
        except Exception as e:
            print(f"Ошибка при удалении файла: {str(e)}")
            
    def delete_folder(self): 
        folder_name = input("Введите имя папки, которую нужно удалить: ") 
        folder_path = Path.cwd() / folder_name 
        print(f"Удаляется папка: {folder_path}") 
        try: 
            folder_path.rmdir()
            print("Папка успешно удалена.")
        except FileNotFoundError: 
            print("Папка не найдена.")

         
    def rename_file(self): 
        old_name = input("Введите имя файла или папки для переименования: ") 
        new_name = input("Введите новое имя файла или папки: ") 
        old_path = Path(self.cwd) / old_name 
        new_path = Path(self.cwd) / new_name 
        try: 
            old_path.rename(new_path) 
            print(f"Переименован: {old_path} -> {new_path}") 
        except Exception as e:
            print(f"Ошибка при переименовании: {str(e)}")
            
    def show_image(self):
        image_path = input("Введите путь к изображению: ")        
        try:
            image = Image.open(image_path)
            image.show()
            print(f"Отображается изображение: {image_path}")
        except FileNotFoundError:
            print("Файл не найден")
    
    def change_directory(self):
        new_directory = input("Введите новую директорию: ")     
        try:
            os.chdir(new_directory)
            self.cwd = os.getcwd()
            print(f"Текущая директория изменена на: {self.cwd}")
        except Exception as e:
            print(f"Ошибка при изменении текущей директории: {str(e)}")
    
    def run(self):
        while True:
            print(f"Текущий каталог: {self.cwd}")
            self.print_menu()
            number = input("Введите свой выбор: ")

            if number == "1":
                self.list_files()
            elif number == "2":
                self.create_file()
            elif number == "3":
                self.create_folder()
            elif number == "4":
                self.delete_file()
            elif number == "5":
                self.delete_folder()
            elif number == "6":
                self.rename_file()
            elif number == "7":
                self.show_image()
            elif number == "8":
                self.change_directory()
            elif number == "0":
                break
            else:
                print("Неверный выбор. Пожалуйста, попробуйте еще раз.")
