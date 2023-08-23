from PhoneBook.phoneBook import PhoneBookCSV

Book = PhoneBookCSV(input("Введите имя справочника: "))

MENU = {
    "справочник": lambda: print(Book.bookName),
    "новая-запись": lambda: Book.setValue(),
    "просмотр": lambda: Book.getBook(),
    "поиск": lambda: Book.getSearchRow(input("Введите ключевое слово поиска!: ")),
    "изменить": lambda: Book.resetValue(),
    "удалить-справочник": lambda: Book.resetBook(),
    "выход": lambda: print("{:-^30}".format("Закрытие программы.")),
}


class Menu(object):
    tiket = True

    def __init__(self):
        self.keys = MENU.keys()

    def getMenu(self, insert: str):
        self.answer = insert
        if self.answer == "выход":
            self.tiket = False
        if self.answer in list(self.keys):
            self.menu = MENU[self.answer]
            self.menu()
            self.answer = print('{:"^30}'.format("Выполнено!"))
            return
        print(("{:-^25}" * len(MENU.keys())).format(*MENU.keys())),
        recurse = input("выберите пункт меню: ")
        self.getMenu(recurse)
