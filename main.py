import os
import sys
from phoneBook.phoneBook import PhoneBookCSV as Book


Menu = {
    "Меню": lambda: getMenu(),
    "Справочник": lambda: Book(input("Введите имя справочника: ")),
    "Добавить_запись": lambda: Book.setValue(),
    "Просмотр_справочника": lambda: Book.getBook(),
    "Поиск_строк_по_ключю": lambda: Book.getSearchRow(input("Введите ключевое слово поиска! :")),
    "Изменить_строку": lambda: Book.resetValue(),
    "Удалить_все_данные": lambda: Book.resetBook(),
    "Выход": "",

}


class InMenu(object):
    def __init__(self):
        
        keys = Menu.keys()
        self.getMenu = print(("{:-^25}" * len(keys)).format(*keys))
        answer = input("выберите пункт меню: ")
        if answer in list(keys) and answer != "Выход":            
            self.tiket = True
            self.menu = Menu[answer]
        else:
            self.tiket = False
            self.menu = Menu["Выход"]


def main():
    action = Menu[sys.argv[-1]]
    action()
    while True:
        try:
            action = getMenu.menu            
            if not getMenu.tiket:
                break
            action()
            print('{:"^30}'.format("Выполнено!"))            
            action = Menu["Меню"]
        except:
            action = Menu["Меню"]
            if not getMenu.tiket:
                break
            action()

    print("{:-^30}".format("Программа выполнена выход."))


if __name__ == "__main__":
    main()
