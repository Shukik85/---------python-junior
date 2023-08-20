import array
import csv
import os
from prompt_toolkit import prompt


class PhoneBookCSV(object):
    """
    Инициализация справочника\n
    Args:
        bookName (str): имя_справочника

    Methods:
        setNewRow(): добавление записи\n
        setNewValue(): обновить значение строки\n
        getBook(): просмотр справочника\n
        getRows(): поиск по значению\n
        resetBook(): замена полей с очисткой справочника
    """

    def __init__(self, bookName):
        self.fields = [
            "Фамилия",
            "Имя",
            "Отчество",
            "Название организации",
            "Телефон рабочий",
            "Мобильный",
        ]
        self.bookName = bookName
        self.row = None
        self.rows = None
        self.tiket = True  # флаг сброса справочника

    def __csvSet(self):
        """
        Формирование csv файла
        """
        with open(
            repr(self.bookName) + ".csv",
            "a" if self.tiket else "w",  # открываем на добавление в конец файла.
            encoding="utf8",
            newline="",
            errors="surrogateescape"
        ) as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=self.fields, dialect="excel")
            if not self.tiket:
                writer.writeheader()  # если файла нет записываем заголовок.
            if self.row:
                writer.writerow(self.row)  # для записи новой строки
                self.row = None
            if self.rows:
                writer.writerows(self.rows)  # для редактирования записи
                self.rows = None

    def __getRows(self, search):
        """
        Поиск по значению\n

        Args:
            bookName (str): название зправочника.\n
            search (str, optional): поиск строк по справочнику. Defaults to "all".
        """
        print(self.bookName)
        print(search, type(search))
        if os.path.isfile(repr(self.bookName) + ".csv"):
            with open(
                repr(self.bookName) + ".csv",
                "r",
                encoding="utf8",
                newline="",
                errors="surrogateescape"
            ) as csvfile:
                reader = csv.reader(csvfile, dialect="excel")
                if search == "all":
                    self.count = 0
                    for value in reader:
                        print(self.count, ("{:-^30}" * len(value)).format(*value))
                        self.count += 1
                else:
                    print(("{:-^30}" * len(self.fields)).format(*self.fields))
                    for value in reader:
                        if value.count(search) > 0:
                            print(("{:-^30}" * len(value)).format(*value))
        else:
            print("Файл не найден!")

    def getBook(self):
        self.__getRows("all")

    def resetBook(self):
        """
        Создание полей, удаление всех данных(не уверен, что нужно)
        """

        self.fields.clear()  # сброс полей по-умолчанию
        while True:
            input = prompt("Введите название поля (пустое поле для выхода): ")
            if input:
                self.fields.append(input)
            else:
                break
        self.tiket = False
        self.setNewRow()

    def setNewRow(self):
        """
        Заполняем поля справочника
        """
        self.row = dict()
        for field in self.fields:
            value = prompt("Заполните поле:\n{!r:-^30}\n{:^15}".format(field, "=>"))
            self.row[field] = value
        self.__csvSet()

    def setNewValue(self):
        """
        Редактировать справочник\n
        """
        self.getBook()
        row = int(prompt("Выберите строку для редактирования : ")) - 1
        if row >= 0 and row <= self.count:
            with open(repr(self.bookName) + ".csv", "r", encoding="utf8", errors="surrogateescape") as csvfile:
                read = csv.DictReader(csvfile, dialect="excel")
                self.rows = list(read)
                tmpRow = self.rows.pop(row)

            self.rows.insert(row - 1, tmpRow)
            self.tiket = False
            self.__csvSet()


# nameBook = prompt("Имя справочника\n{:-^30}\n".format("Ввод"))
# print(nameBook)
Book = PhoneBookCSV("Новая книга")
Book.getBook()
print("Ok")
