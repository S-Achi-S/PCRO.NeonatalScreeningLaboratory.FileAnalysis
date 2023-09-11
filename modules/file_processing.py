#   Libraries
import os
from colorama import init
from colorama import Fore, Style

#   Inside modules
from data.configuration.file_extensions import correct_extensions

#   Some code =>
init()


def file_processing(application_object):
    file_path = application_object.file_path

    if file_path is not None:
        application_object.file_name = get_file_name(file_path)
        application_object.file_extension = get_file_extension(file_path)
        application_object.file_size = get_file_size(file_path)
        application_object.upload_file = True
        application_object.check_file_extension = check_file_extensions_bool(application_object)

        if application_object.upload_file:
            show_file_information(application_object)
        else:
            print(f"{Fore.RED}[ERROR]{Style.RESET_ALL} При чтении файла возикла ошибка!")

    else:
        print(f"{Fore.LIGHTBLUE_EX}[INFO]{Style.RESET_ALL} Пустая ссылка.\n"
              "Выберите другой файл или перезагрузите программу.")


def get_file_name(file_path):
    file_name = os.path.basename(file_path)
    file_name, _ = os.path.splitext(file_name)

    return file_name


def get_file_extension(file_path):
    file_extension = os.path.basename(file_path)
    _, file_extension = os.path.splitext(file_extension)

    return file_extension


def check_file_extensions_bool(application_object):
    extension = application_object.file_extension

    if extension in correct_extensions:
        return True
    else:
        return False


def get_file_size(file_path):
    file_size = os.path.getsize(file_path)
    file_size = file_size / 1024
    file_size = round(file_size)

    return file_size


def show_file_information(application_object):
    print(f"{Fore.LIGHTMAGENTA_EX}\n\tИнформация о файле:\n\n{Style.RESET_ALL}"
          f"\tПуть к файлу: {Fore.GREEN}{application_object.file_path}{Style.RESET_ALL}\n"
          f"\tИмя файла: {Fore.GREEN}{application_object.file_name}{Style.RESET_ALL}")
    if application_object.check_file_extension:
        print(f"\tРасширение файла: {Fore.GREEN}{application_object.file_extension}{Style.RESET_ALL}")
    else:
        print(f"\tРасширение файла: {Fore.RED}{application_object.file_extension}{Style.RESET_ALL}")
    print(f"\tРазмер файла: {Fore.GREEN}{application_object.file_size}{Style.RESET_ALL} кБайт\n"
          f"\t---\n"
          f"\tЧтение файла: {Fore.GREEN}{application_object.upload_file}{Style.RESET_ALL}")
    if application_object.check_file_extension:
        print(f"\tВозможность анализа: {Fore.GREEN}{application_object.check_file_extension}{Style.RESET_ALL}")
    else:
        print(f"\tВозможность анализа: {Fore.RED}{application_object.check_file_extension}{Style.RESET_ALL}")
