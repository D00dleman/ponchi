import os
from shutil import copy
from sys import platform


# Функиця копирования файлов из директрии с чистым проектом в текующуу
def create():
    directory_delimiter = "/" if platform != "win32" else "\\"
    module_dir = directory_delimiter.join(
        os.path.realpath(__file__).split(directory_delimiter)[:-1]
    )
    clear_app_dir = "{0}{1}clear_app{1}".format(module_dir, directory_delimiter)
    clear_app_files = ["cfg.py", "app.py"]
    for i in clear_app_files:
        full_path_file = "{0}{1}".format(clear_app_dir, i)
        print("Copying {0} to ./".format(full_path_file))
        copy(full_path_file, ".")
