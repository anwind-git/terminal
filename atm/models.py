import re


class DataHandler:
    def __get__(self, instance, owner):
        return instance.__dict__[self.name]

    def __set__(self, instance, value):
        cleaned_value = re.sub(r'[^А-Яа-я]', '', value)
        instance.__dict__[self.name] = cleaned_value.title()

    def __set_name__(self, owner, name):
        self.name = name


class Person:
    last_name = DataHandler()
    first_name = DataHandler()
    middle_name = DataHandler()

    def __init__(self, id_client, last_name, first_name, middle_name, gender, birth_year, password):
        self.id_client = id_client
        self.last_name = last_name
        self.first_name = first_name
        self.middle_name = middle_name
        self.gender = gender
        self.birth_year = birth_year
        self.password = password


class Atm:
    def __init__(self, withdrawal_fee, wealth_tax, max_fee, min_fee, accruals, max_count):
        self.withdrawal_fee = withdrawal_fee
        self.wealth_tax = wealth_tax
        self.max_fee = max_fee
        self.min_fee = min_fee
        self.accruals = accruals
        self.max_count = max_count
