import os
from os import system, name
from atm import urls, open_json
os.environ['TERM'] = 'xterm'


def сlear():
    if name == 'nt':
        _ = system('cls')
    else:
        _ = system('clear')


# Поиск клиента и его счета. Если счета нет, то при первой авторизации добавляет в файл account.json
def input_pin():
    code_entry = 0
    while code_entry <= 0:
        try:
            code_entry = int(input("Введите пинкод: "))
            person = open_json.customer_search(code_entry)
            if person is not None and person['password'] is not None and person['password'] == code_entry:
                file = "account.json"
                if os.path.exists(file):
                    id_exists = any(account['id'] == person['id'] for account in open_json.open_account_json())
                    if not id_exists:
                        data = open_json.open_account_json()
                        data.extend(open_json.invoice_form(person))
                        open_json.record_account_json(data)
                else:
                    data = open_json.invoice_form(person)
                    open_json.record_account_json(data)

                account = open_json.customer_account_lookup(person)
                сlear()
                print(f"Добро пожаловать! {person['last_name']} {person['first_name']} " 
                f"{person['middle_name']} | пол: {person['gender']} | год рождения: {person['birth_year']} "
                f"| Баланс: {account['balance']}$ | Последняя операция: {account['data_time']}")
                return urls.menu(person)
            else:
                print('Клиент несуществует!')
        except ValueError:
            print("Ошибка ввода!")
