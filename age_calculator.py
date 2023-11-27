from datetime import datetime
from dateutil import relativedelta


class Person:
    def __init__(self, name, dob):
        self.name = name
        self.dob = dob

    def age(self):
        """abstract methode"""
        pass


class Student(Person):
    def __init__(self, name, dob):
        self.dob = dob
        super().__init__(name, dob)

    def age(self):
        today = str(datetime.today().date())
        # # print(type(today))
        # print(today)            #year-month-day
        date_of_birth = self.dob
        # # print(type(date_of_birth))
        # print(date_of_birth)
        start_date = datetime.strptime(date_of_birth, '%Y-%m-%d')
        end_date = datetime.strptime(today, "%Y-%m-%d")
        date_delta = relativedelta.relativedelta(end_date, start_date)
        print("your age :", date_delta.years, 'Years,', date_delta.months, 'months,', date_delta.days, 'days')


s1 = Student("ab", '2000-2-29')
s1.age()

# print(datetime.date.today())
