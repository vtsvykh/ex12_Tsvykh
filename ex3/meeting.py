import datetime

class Meeting:
    """
    Class of meetings.
    """
    lst_meeting = []

    def __init__(self, id, date, title):
        """
        Initializes a Meeting object.

        :param id: the meeting's ID.
        :param date: the date of the meeting.
        :param title: the title of the meeting.
        """
        self.id = id
        self.date = date
        self.title = title
        self.employees = []

    @classmethod
    def count_meeting(cls, date):
        counter = 0
        for meet in Meeting.lst_meeting:
            if str(meet.date) == str(date):
                counter += 1
        return counter

    @classmethod
    def total(cls):
        counter = 0
        for meet in Meeting.lst_meeting:
            counter += len(meet.employees)
        return counter

    def add_person(self, person):
        self.employees.append(person)

    def count(self):
        return len(self.employees)

    def __repr__(self):
        res = ''
        res += f'Рабочая встреча {Meeting.lst_meeting.index(self) + 1}\n'
        res += f'{self.date} {self.title}\n'

        for employee in self.employees:
            employee_str = (f'ID: {employee.id} '
                            f'LOGIN: {employee.nick_name} '
                            f'NAME: {employee.first_name} {employee.middle_name} {employee.last_name} '
                            f'GENDER: {employee.gender}')
            employee_str = ' '.join(employee_str.split())
            res = res + employee_str + '\n'
        return res


class Load:

    @staticmethod
    def write(file_meeting, file_person, file_meet_pers):
        """
        Method of loading data from the file
        :param file_meeting: txt document with info about meetings
        :param file_person: txt document with info about employees
        :param file_meet_pers: txt document with info about members of meetings
        :return:
        """

        with open(file_meeting, 'r', encoding='utf_8') as file_meeting:
            lines = file_meeting.readlines()
            for line in lines[1:]:
                line = line.rstrip()
                id, date, title = line.split(';')[:-1]
                Meeting.lst_meeting.append(Meeting(int(id), Date(date), title))

        with open(file_person, 'r', encoding='UTF-8') as file_person:
            lines = file_person.readlines()
            for line in lines[1:]:
                line = line.rstrip()
                id, nick_name, first_name, last_name, middle_name, gender = line.split(';')[:-1]
                User.users.append(User(int(id), nick_name, first_name, last_name, middle_name, gender))

        with open(file_meet_pers, 'r', encoding='UTF-8') as file_meet_pers:
            lines = file_meet_pers.readlines()
            for line in lines[1:]:
                line = line.rstrip()
                id_meet, id_pers = line.split(';')[:-1]
                for meet in Meeting.lst_meeting:
                    if meet.id == int(id_meet):
                        for user in User.users:
                            if user.id == int(id_pers):
                                meet.employees.append(user)


class Date:
    """
    Class representing date
    """

    def __init__(self, date_str):
        """
        Class of date.

        :param date_str: A string representing a date in the format "dd.mm.yyyy".
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

    def __repr__(self):
        """
        Returns a string representation of the date.

        :return: A string representing the date.
        """

        return f'{self.date}'

class User:
    users = []
    """
    Class representing User
    """

    def __init__(self, id, nick_name, first_name, last_name, middle_name, gender):
        """
         Initializes a User object.

         :param id (int): the user's ID.
         :param nick_name (str): the user's nickname.
         :param first_name (str): the user's first name.
         :param last_name (str): the user's last name.
         :param middle_name (str): the user's middle name.
         :param gender (str): the user's gender.
         """
        self.id = id
        self.nick_name = nick_name
        self.first_name = first_name
        self.last_name = last_name
        self.middle_name = middle_name
        self.gender = gender
