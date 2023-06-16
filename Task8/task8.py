# Задача №49. Решение в группах
# Создать телефонный справочник с
# возможностью импорта и экспорта данных в
# формате .txt. Фамилия, имя, отчество, номер
# телефона - данные, которые должны находиться
# в файле.
# 1. Программа должна выводить данные
# 2. Программа должна сохранять данные в
# текстовом файле
# 3. Пользователь может ввести одну из
# характеристик для поиска определенной
# записи(Например имя или фамилию
# человека)
# 4. Использование функций. Ваша программа
# не должна быть линейной

# Задача 38: Дополнить телефонный справочник возможностью изменения и удаления данных.
# Пользователь также может ввести имя или фамилию, и Вы должны реализовать функционал
# для изменения и удаления данных.


file_path = "Task8/file.txt"


def show_all_records():
    with open(file_path, "r", encoding="utf8") as file:
        for line in file:
            print(*line.split(';'), end="")


def search_record(desired):
    flag = True
    with open(file_path, "r", encoding="utf8") as file:
        for line in file:
            if desired.lower() in line.lower().replace(";", " "):
                print(*line.split(';'), end="")
                flag = False
    if flag:
        print(f"По запросу '{desired}' ничего не найдено.")


def add_contact(fio, number):
    with open(file_path, "r", encoding="utf8") as file:
        sp = list(file.readlines())
        with open(file_path, "a", encoding="utf8") as file:
            file.write(f"\n{len(sp)+1};{fio.replace(' ', ';')};{number}")


def edit_contact(position):
    with open(file_path, "r", encoding="utf8") as file:
        sp = list(file.readlines())
        contact = sp[position - 1].split(";")
        change_selection = int(input("Выберите действие: \n1 - изменить ФИО; "
                                     "\n2 - изменить номер; "
                                     "\n3 - изменить всю информацию; "
                                     "\n4 - отмена.\n "))
        if change_selection == 1:
            sp[position -
                1] = f"{contact[0]};{input('Введите новое ФИО через пробел: ').replace(' ',';')};{contact[-1]}\n"
        elif change_selection == 2:
            contact[-1] = input("Введите новый номер: ")+"\n"
            sp[position - 1] = ";".join(contact)
        elif change_selection == 3:
            sp[position -
                1] = f"{contact[0]};{input('Введите новое ФИО и номер через пробел: ').replace(' ',';')}\n"
        elif change_selection == 4:
            return
        with open(file_path, "w", encoding="utf8") as file:
            for i in sp:
                file.writelines(i)


def del_contact(position):
    with open(file_path, "r", encoding="utf8") as file:
        sp = list(file.readlines())
        del sp[position-1]
        for i in range(len(sp)):
            sp[i] = f"{i+1};"+";".join([sp[i].split(";")[j]
                                       for j in range(1, len(sp[i].split(";")))])
        with open(file_path, "w", encoding="utf8") as file:
            for i in sp:
                file.writelines(i)


def main():
    print("Выберите действие: \n1 - показать справочник; "
          "\n2 - найти контакт; "
          "\n3 - добавить данные; "
          "\n4 - изменить данные существующего контакта; "
          "\n5 - удалить существующий контакт.")
    select = int(input())
    if select == 1:
        show_all_records()
    elif select == 2:
        find = input("Введите данные для поиска: ")
        search_record(find)
    elif select == 3:
        print("Введите данные нового контакта.")
        new_fio = input("Введите ФИО через пробел: ")
        new_number = input("Введите номер телефона: ")
        add_contact(new_fio, new_number)
    elif select == 4:
        show_all_records()
        change_number = int(
            input("\nВведите id контакта, для редактирования: "))
        edit_contact(change_number)
    elif select == 5:
        show_all_records()
        del_number = int(input("\nВведите id контакта, для удаления: "))
        del_contact(del_number)


main()
