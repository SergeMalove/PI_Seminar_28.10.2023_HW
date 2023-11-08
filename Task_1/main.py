import os

def print_data():
    with open('phonebook.txt', 'r', encoding = 'UTF-8') as file:
        phonebook_str = file.read()
    print(phonebook_str)
    print()


def input_name():
    return input('Введите имя контакта: ').title()

def input_surname():
    return input('Введите фамилию контакта: ').title()

def input_patronymic():
    return input('Введите отчество контакта: ').title()

def input_phone():
    return input('Введите номер телефона контакта: ')

def input_address():
    return input('Введите адрес контакта: ').title()

def input_data():
    sur_name = input_surname()
    name = input_name()
    patronymic = input_patronymic()
    phone = input_phone()
    address = input_address()
    my_sep = ' '
    return f'{sur_name}{my_sep}{name}{my_sep}{patronymic}{my_sep}{phone}\n{address}\n\n'


def add_contact():
    new_contact_str = input_data()
    with open('phonebook.txt', 'a', encoding = 'UTF-8') as file:
        file.write(new_contact_str)

def search_contact():
    print('Варианты поиска:\n'
        '1. По фамилии\n'
        '2. По имени\n'
        '3. По отчеству\n'
        '4. По телефону\n'
        '5. По адресу\n')
    
    command = input('Выберете вариант поиска: ')

    while command not in ('1', '2', '3', '4', '5'):
        print('Некорректный ввод пункта меню. Повторите ввод.')
        command = input('Выберете вариант поиска: ')

    i_search = int(command) - 1

    search = input('Введит данные для поиска: ').lower()
    print()

    with open('phonebook.txt', 'r', encoding = 'UTF-8') as file:
        contacts_list = file.read().rstrip().split('\n\n')
    print(contacts_list)

    check_cont = False

    for contact_str in contacts_list:
        lst_contact = contact_str.lower().replace('\n', ' ').split()
        if search in lst_contact[i_search]:
            print(contact_str)
            print()
            check_cont = True
    if not check_cont:
        print('Такого контакта нет')

def change_contact():
    print('Варианты поиска для изменения:\n'
        '1. По фамилии\n'
        '2. По имени\n'
        '3. По отчеству\n'
        '4. По телефону\n'
        '5. По адресу\n')
    
    command = input('Выберете вариант поиска: ')

    while command not in ('1', '2', '3', '4', '5'):
        print('Некорректный ввод пункта меню. Повторите ввод.')
        command = input('Выберете вариант поиска: ')

    i_search = int(command) - 1

    search = input('Введите данные для поиска: ').lower()
    print()

    with open('phonebook.txt', 'r', encoding = 'UTF-8') as file:
        contacts_list = file.read().rstrip().split('\n\n')

    check_cont = False
    contact_id = 0

    for contact_str in contacts_list:
        lst_contact = contact_str.lower().replace('\n', ' ').split()
        contact_id += 1
        if search in lst_contact[i_search]:
            print(f'{contact_id}. {contact_str}')
            print()
            check_cont = True
    if not check_cont:
        print('Такого контакта нет')
    else:
        contact_id = int(input('Введите номер контакта для изменения: '))
        print()
        print('Введите измененные данные контакта: ')
        new_contact = input_data()
        contacts_list[contact_id - 1] = new_contact.replace('\n\n', '')

        with open('phonebook.txt', 'w', encoding = 'UTF-8') as file:
            for contact_str in contacts_list:
                file.write(f'{contact_str}\n\n')
    
def delete_contact():
    print('Варианты поиска для удаления:\n'
        '1. По фамилии\n'
        '2. По имени\n'
        '3. По отчеству\n'
        '4. По телефону\n'
        '5. По адресу\n')
    
    command = input('Выберете вариант поиска: ')

    while command not in ('1', '2', '3', '4', '5'):
        print('Некорректный ввод пункта меню. Повторите ввод.')
        command = input('Выберете вариант поиска: ')

    i_search = int(command) - 1

    search = input('Введите данные для поиска: ').lower()
    print()

    with open('phonebook.txt', 'r', encoding = 'UTF-8') as file:
        contacts_list = file.read().rstrip().split('\n\n')

    check_cont = False
    contact_id = 0

    for contact_str in contacts_list:
        lst_contact = contact_str.lower().replace('\n', ' ').split()
        contact_id += 1
        if search in lst_contact[i_search]:
            print(f'{contact_id}. {contact_str}')
            print()
            check_cont = True
    if not check_cont:
        print('Такого контакта нет')
    else:
        contact_id = int(input('Введите номер контакта для удаления: '))
        print()
        contacts_list.pop(contact_id - 1)

        with open('phonebook.txt', 'w', encoding = 'UTF-8') as file:
            for contact_str in contacts_list:
                file.write(f'{contact_str}\n\n')

def copy_contact():
    print('Варианты поиска для копирования:\n'
        '1. По фамилии\n'
        '2. По имени\n'
        '3. По отчеству\n'
        '4. По телефону\n'
        '5. По адресу\n')
    
    command = input('Выберете вариант поиска: ')

    while command not in ('1', '2', '3', '4', '5'):
        print('Некорректный ввод пункта меню. Повторите ввод.')
        command = input('Выберете вариант поиска: ')

    i_search = int(command) - 1

    search = input('Введите данные для поиска: ').lower()
    print()

    with open('phonebook.txt', 'r', encoding = 'UTF-8') as file:
        contacts_list = file.read().rstrip().split('\n\n')

    check_cont = False
    contact_id = 0

    for contact_str in contacts_list:
        lst_contact = contact_str.lower().replace('\n', ' ').split()
        contact_id += 1
        if search in lst_contact[i_search]:
            print(f'{contact_id}. {contact_str}')
            print()
            check_cont = True
    if not check_cont:
        print('Такого контакта нет')
    else:
        contact_id = int(input('Введите номер контакта для копирования: '))
        print()

        with open('phonebook_copy.txt', 'a', encoding = 'UTF-8') as file:
            file.write(f'{contacts_list[contact_id - 1]}\n\n')

def interface():
    with open('phonebook.txt', 'a', encoding = 'UTF-8'):
        pass
    command = 0 
    os.system("cls")
    while command != '7':
        print('Меню пользователя:\n'
            '1. Вывод данных на экран\n'
            '2. Добавить контакт\n'
            '3. Поиск контакта\n'
            '4. Изменение контакта\n'
            '5. Удаление контакта\n'
            '6. Перенос контакта\n'
            '7. Выход\n')
        
        command = input('Выберете пункт меню: ')
        while command not in ('1', '2', '3', '4', '5', '6', '7'):
            print('Некорректный ввод пункта меню. Повторите ввод.')
            command = input('Выберете пункт меню: ')

        match command:
            case '1':
                print_data()
            case '2':
                add_contact()
            case '3':
                search_contact()
            case '4':
                change_contact()
            case '5':
                delete_contact()
            case '6':
                copy_contact()
            case '7':
                print('Завершение программы')
        print()

if __name__ == '__main__':
    interface()
