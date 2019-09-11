
# Задача
# Создать файл который, принимает параметры из консоли и в зависимости от них выполняет определенную функцию
# либо выводит справку по параметру help
# либо создает директорию по параметрам mkdir <dir_name>
# используя конструкции try except 



import os
import sys
print('sys.argv = ', sys.argv)
def print_help():

    """ Выводит справку """

    print("help - получение справки") 
    print("mkdir <dir_name> - создание директории")
    print("ping - тестовый ключ")

def make_dir():

    """ Создает директорию или выводит сообщение, что директория с таким именем существует """

    if not dir_name:
        print("Необходимо указать имя директории вторым параметром")
        return
    # записать путь к создаваемой директори в переменную dir_path
    dir_path = os.path.join(os.getcwd(),dir_name)
    
    # Проверка на наличие директории с таким имененем
    try:  
        # создать директорию dir_path 
        os.mkdir(dir_path)
        print('директория {} создана'.format(dir_name))
    # Если директория уже существет, вывести сообщение 'директория {} уже существует'
    except FileExistsError:
        print('директория {} уже существует'.format(dir_name))
def ping():

    """ Проверяет, что параметры передаются """
    print("pong")

# Словарь параметр ключ : функция

do = {
    "help": print_help,
    "mkdir": make_dir,
    "ping": ping
}

# Присваиваем dir_name 
try:
    dir_name = sys.argv[2]
except IndexError:
    dir_name = None

# Присваеваем key 
try:
    key = sys.argv[1]
except IndexError:
    key = None


if key:
    if do.get(key):
        do[key]()
    else:
        print("Задан неверный ключ")
        print("Укажите ключ help для получения справки")