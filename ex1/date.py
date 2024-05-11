import datetime


class Date:
    def __init__(self, date_str):
        try:
            self.__date = datetime.datetime.strptime(date_str, '%d.%m.%Y').date()
        except ValueError:
            print('Ошибка')
            self.__date = None

    @property
    def date(self):
        month_names = ["янв", "фев", "мар", "апр", "май", "июн", "июл", "авг", "сен", "окт", "ноя", "дек"]
        if self.__date:
            return f'{self.__date.day} {month_names[self.__date.month - 1]} {self.__date.year} г.'
        return None

    @date.setter
    def date(self, value):
        try:
            self.__date = datetime.datetime.strptime(value, '%d.%m.%Y').date()
        except ValueError:
            print('Ошибка')
            self.__date = None

    def to_timestamp(self):
        if self.date:
            return int((self.__date - datetime.datetime(1970, 1, 1).date()).total_seconds())
        else:
            return None

    def __eq__(self, other):
        return self.__date == other.__date if self.__date and other.__date else False

    def __lt__(self, other):
        return self.__date < other.__date if self.__date and other.__date else False

    def __le__(self, other):
        return self.__date <= other.__date if self.__date and other.__date else False

    def __gt__(self, other):
        return self.__date > other.__date if self.__date and other.__date else False

    def __ge__(self, other):
        return self.__date >= other.__date if self.__date and other.__date else False

    def __repr__(self):
        return f'{self.__date}'


