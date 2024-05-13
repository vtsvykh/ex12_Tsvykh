import datetime

class Meeting:
    lst_meeting = []

    def __init__(self, id, date, title):
        self.id = id
        self.date = date
        self.title = title
        self.employees = []

    @classmethod
    def count_meeting(cls, date):
        counter = 0
        for meet in Meeting.lst_meeting:
            if meet.date == date:
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
        date_str = self.date.strftime('%d %b %Y')
        res += f'Рабочая встреча {Meeting.lst_meeting.index(self) + 1}\n'
        res += f'{date_str} {self.title}\n'

        for employee in self.employees:
            employee_str = (f'ID: {employee.id} '
                            f'LOGIN: {employee.nick_name} '
                            f'NAME: {employee.first_name} {employee.middle_name} {employee.last_name} '
                            f'GENDER: {employee.gender}')
            employee_str = ' '.join(employee_str.split())
            employee_str += '\n'
            res += employee_str
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
            for line in [line.rstrip() for line in file_meeting.readlines()][1:]:
                id, date, title = line.split(';')[:-1]
                Meeting.lst_meeting.append(Meeting(int(id), Date(date), title))

        with open(file_person, 'r', encoding='UTF-8') as f:
            for line in [line.rstrip() for line in f.readlines()][1:]:
                id, nick_name, first_name, last_name, middle_name, gender = line.split(';')[:-1]
                User.users.append(User(int(id), nick_name, first_name, last_name, middle_name, gender))

        with open(file_meet_pers, 'r', encoding='UTF-8') as f:
            for line in [line.rstrip() for line in f.readlines()][1:]:
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

    def __init__(self, date):
        """
        Sets all the necessary attributes for the class Date
        :param date: string of data of the class Date
        """

        self.date = datetime.datetime.strptime(date, '%d.%m.%Y')

    def __repr__(self):
        """
        Method of representing data of class Date
        :return:
        """

        return self.date


class User:
    users = []
    """
    Class representing User
    """

    def __init__(
            self,
            id: int,
            nick_name: str,
            first_name: str,
            last_name: str,
            middle_name: str,
            gender: str,
    ):
        """
             Initializes a User object.

             :param id: The user's ID.
             :param nick_name: The user's nickname.
             :param first_name: The user's first name.
             :param last_name: The user's last name.
             :param middle_name: The user's middle name.
             :param gender: The user's gender.
             """
        self.id = id
        self.nick_name = nick_name
        self.first_name = first_name
        self.last_name = last_name
        self.middle_name = middle_name
        self.gender = gender
