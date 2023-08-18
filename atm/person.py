from atm import models, open_json


def add_person():
    open_json.person_form(models.Person(1, 'иванов', 'Иван', 'Иванович', 'М', 1995, 1111))
    open_json.person_form(models.Person(2, 'Петров1', 'Петр', 'Петрович', 'М', 1985, 2222))
    open_json.person_form(models.Person(3, 'Васильева', 'лариса4', 'Ивановна', 'Ж', 1977, 3333))
    open_json.person_form(models.Person(4, 'Игнатова', 'Татьяна', 'Николаевна', 'Ж', 1965, 4444))
