import json
import os
from datetime import datetime
datetime_now = datetime.now()
formatted_date_time = datetime_now.strftime("%Y-%m-%d %H:%M")
client = []


# чтение файла client.json
def open_client_json():
    with open('client.json', 'r') as json_file:
        tree_data = json.load(json_file)
    return tree_data


# чтение файла account.json
def open_account_json():
    with open('account.json', 'r') as json_file:
        data = json.load(json_file)
    return data


# чтение файла operations.json по id клиента
def operation_history(person):
    with open('operations.json', 'r') as json_file:
        operations = json.load(json_file)
        for data in operations:
            if data['id'] == person['id']:
                print(f"Операция: {data['operations']} Дата: {data['data_time']}")


# новая запись в account.json
def record_account_json(account):
    with open('account.json', 'w') as file:
        json.dump(account, file, ensure_ascii=False)


# обновление файла account.json
def update_account_json(account):
    data = open_account_json()
    for existing_account in data:
        if existing_account['id'] == account['id']:
            existing_account.update(account)
            break
    with open('account.json', 'w') as file:
        json.dump(data, file, ensure_ascii=False)


# форма записи в account.json
def invoice_form(person):
    account = [{
        'id': person['id'],
        'balance': 0,
        'number_operations': 0,
        'data_time': str(formatted_date_time),
    }]
    return account


# форма записи в operations.json
def operation_form(person, operation):
    data = [{
        'id': person['id'],
        'operations': operation,
        'data_time': str(formatted_date_time),
    }]
    return data


# операции по всем клиентам
def open_operations_json():
    with open('operations.json', 'r') as json_file:
        operations = json.load(json_file)
    return operations


# добавление новой операции
def new_operations(person, data):
    file = "operations.json"
    if os.path.exists(file):
        operation = open_operations_json()
        operation.extend(operation_form(person, data))
        record_operations_json(operation)
    else:
        operation = operation_form(person, data)
        record_operations_json(operation)


# новая запись в operations.json
def record_operations_json(operation):
    with open('operations.json', 'w') as file:
        json.dump(operation, file, ensure_ascii=False)


# поиск счета клиента
def customer_account_lookup(person):
    data = open_account_json()
    for account in data:
        if account['id'] == person['id']:
            return account


# поиск клиента
def customer_search(code_entry):
    data = open_client_json()
    for client in data:
        if client['password'] == code_entry:
            return client


def person_form(Person):

    client.append({
        'id': Person.id_client,
        'last_name': Person.last_name,
        'first_name': Person.first_name,
        'middle_name': Person.middle_name,
        'gender': Person.gender,
        'birth_year': Person.birth_year,
        'password': Person.password
    })

    with open('client.json', 'w') as file:
        json.dump(client, file, ensure_ascii=False)