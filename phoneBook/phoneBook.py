import csv
import os
from prompt_toolkit import prompt


class PhoneBookCSV(object):
    """
    Инициализация справочника\n
    Args:
        bookName (str): имя_справочника

    Methods:
        getBook(): просмотр справочника\n
        setValue(self): создать новую запись\n
        getSearchRow(): поиск по значению\n
        resetValue(): обновить значение строки\n
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
        self.tiket = True  # флаг пустого справочника
        self.__csvReader(None)

    def __csvWriter(self):
        """
        Формирование csv файла
        """
        with open(
            repr(self.bookName) + ".csv",
            "a"
            if self.tiket
            else "w",  # открываем на добавление либо перезапись файла.
            encoding="utf8",
            newline="",
            errors="surrogateescape",
        ) as csvfile:
            writer = csv.DictWriter(
                csvfile,
                fieldnames=self.fields,
                restval="",
                extrasaction="raise",
                dialect="excel",
            )
            if not self.tiket:
                writer.writeheader()  # если файла нет записываем заголовок.
                self.tiket = True
            if self.row:
                writer.writerow(self.row)  # для записи новой строки
                self.row = None
            if self.rows:
                writer.writerows(self.rows)  # для редактирования записи
                self.rows = None
        print("{:-^30}".format("Запись сделана!"))

    def __csvReader(self, search: str | None):
        """
        Поиск по значению\n

        Args:
            bookName (str): название зправочника.\n
            search (str): поиск строк по справочнику.
        """
        print("{:-^30}".format(self.bookName))
        if os.path.isfile(repr(self.bookName) + ".csv"):
            with open(
                repr(self.bookName) + ".csv",
                "r",
                encoding="utf8",
                newline="",
                errors="surrogateescape",
            ) as csvfile:
                reader = csv.DictReader(csvfile, restval="None", dialect="excel")
                fieldName = reader.fieldnames
                Header = print(
                    ("{:-^30}" * len(fieldName)).format(*fieldName)
                )  # выводим заголовок таблицы.
                Header
                numLine = 0
                if search == None:
                    self.fields = fieldName
                    self.count = len(list(reader))
                if search == "all":
                    for d in reader:
                        value = list(d.values())
                        print(numLine, ("{:-^30}" * len(d)).format(*value))
                        if numLine % 10 == 0 and numLine != 0:
                            prompt("{:-^30}".format("Далее => нажмите Enter"))
                            Header
                        numLine += 1
                elif search:
                    for d in reader:
                        value = list(d.values())
                        if search in value:
                            print(numLine, ("{:-^30}" * len(d)).format(*value))
                            numLine += 1
        else:
            print("Файл не найден!")
            while True:
                answer = prompt("Создать новый? (да/нет): ")
                if answer == "да":
                    self.__csvWriter()
                    break
                elif answer == "нет":
                    break

    def __newRow(self):
        """
        Заполняем поля справочника
        """
        row = dict()
        for field in self.fields:
            value = prompt("Заполните поле:\n{!r:-^30}\n{:^15}".format(field, "=>"))
            row[field] = value
        return row

    def getBook(self):
        """
        Просмотреть справочник
        """
        self.__csvReader("all")

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
        self.row = self.__newRow()
        self.__csvWriter()

    def setValue(self):
        """
        Создать новую запись.
        """
        self.row = self.__newRow()
        self.__csvWriter()

    def resetValue(self):
        """
        Редактировать строку\n
        """
        self.getBook()
        while True:
            row = prompt("Выберите строку для редактирования : ")
            if row.isdigit():
                row = int(row)
                break
        print(self.count)
        if row >= 0 and row <= self.count:
            with open(
                repr(self.bookName) + ".csv",
                "r",
                encoding="utf8",
                errors="surrogateescape",
            ) as csvfile:
                read = csv.DictReader(csvfile, dialect="excel")
                self.rows = list(read)
                self.rows[row] = self.__newRow()
            self.tiket = False
            self.__csvWriter()

    def getSearchRow(self, search: str):
        self.__csvReader(search)
