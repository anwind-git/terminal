import os
from os import system, name
from atm import urls, open_json
os.environ['TERM'] = 'xterm'


def сlear():
    if name == 'nt':
        _ = system('cls')
    else:
        _ = system('clear')


# Поиск счета клиента.
def input_pin():
    while True:
        try:
            code_entry = int(input("Введите пинкод: "))
        except ValueError as e:
            print(f"Ошибка ввода: {e}")
            continue

        person = open_json.customer_search(code_entry)
        if person is not None and person['password'] is not None and person['password'] == code_entry:
            id_exists = any(account['id'] == person['id'] for account in open_json.open_account_json())
            if not id_exists:
                account = open_json.open_account_json()
                account.extend(open_json.invoice_form(person))
                open_json.record_account_json(account)
            сlear()
            account = open_json.customer_account_lookup(person)
            print(f"Добро пожаловать! {person['last_name']} {person['first_name']} " 
            f"{person['middle_name']} | пол: {person['gender']} | год рождения: {person['birth_year']} "
            f"| Баланс: {account['balance']}$ | Последняя операция: {account['data_time']}")
            return urls.menu(person)
        else:
            print('Клиент не существует!')

