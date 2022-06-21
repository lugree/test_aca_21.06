class AgeError(Exception):
    def __init__(self, value):
        self.__value = value

    def get_info(self):
        return f"Invalid age - {self.__value}\n"


class GenderError(Exception):
    def __init__(self, value):
        self.__value = value

    def get_info(self):
        return f"Invalid gender - {self.__value}\n"


class Patient:
    gender_list = ['M', 'F']

    def __init__(self, name, surname, age, gender):

        self.__is_valid = False
        try:
            if age < 18 or age > 100:
                raise AgeError('The age must be 18 - 100')
        except AgeError as err:
            print(err.get_info())
        else:
            self.age = age
            self.__is_valid = True

        try:
            if gender not in self.gender_list:
                raise GenderError('Gender must be F or M')
        except GenderError as err:
            print(err.get_info())
        else:
            self.gender = gender
            self.__is_valid = True

        self.surname = surname
        self.name = name

    def __repr__(self):
        return f'{self.name} {self.surname} - {self.gender}, {self.age} years old.'


doctor1 = Patient('Artur', 'Mnoyan', 25, 'M')
print(doctor1)


class Doctor:
    def __init__(self, name, surname, schedule):
        self.schedule = schedule
        self.surname = surname
        self.name = name

    def __str__(self):
        return f'Doctor {self.name} {self.surname}\n ' \
               f'schedule {self.schedule}'

    def register_patient(self, patient, date_time):
        self.schedule = {}
        new_schedule = self.schedule{self.patient: self.date_time}



