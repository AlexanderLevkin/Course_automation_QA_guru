import os

os.path.abspath(__file__)  # Путь к файлу
os.path.dirname(os.path.abspath(__file__))  # Путь к директории в скобочках мы указываем файл

current_dir = os.path.dirname(os.path.abspath(__file__))

os.path.join(current_dir, '/tmp')  # JOIN Склеивает пути, например мы к current_dir в этом примере добавили папку /tmp
