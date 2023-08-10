class Person:
    def __init__(self, id_client, last_name, first_name, middle_name, gender, birth_year, password):
        self.id_client = id_client
        self.last_name = last_name
        self.first_name = first_name
        self.middle_name = middle_name
        self.gender = gender
        self.birth_year = birth_year
        self.password = password


class Atm:
    def __init__(self, withdrawal_fee, wealth_tax, max_fee, min_fee, accruals):
        self.withdrawal_fee = withdrawal_fee
        self.wealth_tax = wealth_tax
        self.max_fee = max_fee
        self.min_fee = min_fee
        self.accruals = accruals
