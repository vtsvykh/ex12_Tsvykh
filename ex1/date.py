import datetime


class Date:
    """
    Class of date.

    Args:
        date_str (str): string with date

    """
    def __init__(self, date_str):
        """
        :param date_str (str): string with date
        """
        try:
            self.__date = datetime.datetime.strptime(date_str, '%d.%m.%Y').date()
        except ValueError:
            print('Ошибка')
            self.__date = None

    @property
    def date(self):
        """
        Function for getting date.
        :return: date
        """
        month_names = ["янв", "фев", "мар", "апр", "май", "июн", "июл", "авг", "сен", "окт", "ноя", "дек"]
        if self.__date:
            return f'{self.__date.day} {month_names[self.__date.month - 1]} {self.__date.year} г.'
        return None

    @date.setter
    def date(self, value):
        """
        Function for setting date.
        :param value: value of new date
        :return: new_date
        """
        try:
            self.__date = datetime.datetime.strptime(value, '%d.%m.%Y').date()
        except ValueError:
            print('Ошибка')
            self.__date = None

    def to_timestamp(self):
        """
         Converts the date to a timestamp.

        :return: The number of seconds since 01.01.1970.
        """
        if self.date:
            return int((self.__date - datetime.datetime(1970, 1, 1).date()).total_seconds())
        else:
            return None

    def __eq__(self, other):
        """
        Checks if this date is equal to another date.

        :param other: The other date to compare to.
        :return: True if the dates are equal, False otherwise.
        """
        return self.__date == other.__date if self.__date and other.__date else False

    def __lt__(self, other):
        """
        Checks if this date is less than another date.

        :param other: The other date to compare to.
        :return: True if this date is less than the other date, False otherwise.
        """
        return self.__date < other.__date if self.__date and other.__date else False

    def __le__(self, other):
        """
        Checks if this date is less than or equal to another date.

        :param other: The other date to compare to.
        :return: True if this date is less than or equal to the other date, False otherwise.
        """
        return self.__date <= other.__date if self.__date and other.__date else False

    def __gt__(self, other):
        """
        Checks if this date is greater than another date.

        :param other: The other date to compare to.
        :return: True if this date is greater than the other date, False otherwise.
        """
        return self.__date > other.__date if self.__date and other.__date else False

    def __ge__(self, other):
        """
        Checks if this date is greater than or equal to another date.

        :param other: The other date to compare to.
        :return: True if this date is greater than or equal to the other date, False otherwise.
        """
        return self.__date >= other.__date if self.__date and other.__date else False

    def __repr__(self):
        """
        Returns a string representation of the date.

        :return: A string representing the date.
        """
        return f'{self.date}'


