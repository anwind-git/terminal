from atm import models, pin_code_entry
import os
from atm import open_json
os.environ['TERM'] = 'xterm'


class BaseClass():
    atm = models.Atm(0.015, 10, 600, 30, 0.03)


class TopUp(BaseClass):
    # пополнение баланса
    def balance_top_up(self, person):
        wealth_tax(person)
        account = open_json.customer_account_lookup(person)
        requested_amount = input_amount(person)
        if account['id'] == person['id']:
            account['balance'] += requested_amount
            account['number_operations'] += 1
            open_json.update_account_json(account)
            replenishment = f'Баланс пополнен на {requested_amount}$, на вашем счете: {account["balance"]}$'
            open_json.new_operations(account, replenishment)
            print(replenishment)
            accruals(account)


class Cash(BaseClass):
    # вывод средств
    def cash_withdrawal(self, person):
        wealth_tax(person)
        requested_amount = input_amount(person)
        percentages = max(min(requested_amount * BaseClass.atm.withdrawal_fee, BaseClass.atm.max_fee), BaseClass.atm.min_fee)
        account = open_json.customer_account_lookup(person)
        if account['id'] == person['id']:
            summa = requested_amount - percentages
            if summa + percentages <= account['balance']:
                account['balance'] -= summa + percentages
                account['number_operations'] += 1
                withdrawal = f"Выдано наличных {requested_amount - percentages}$, Остаток на балансе: {account['balance']}"
                open_json.new_operations(account, withdrawal)
                print(withdrawal)
                accruals(account)
                open_json.update_account_json(account)
            else:
                print('На счете недостаточно средств!')


def input_amount(person):
    requested_amount = 0
    while requested_amount <= 0:
        try:
            requested_amount = int(input("Введите сумму: "))
            if requested_amount % 50 == 0 and requested_amount > 0:
                return requested_amount
            else:
                requested_amount = 0
                print('Ошибка: сумма должна быть кратна 50 у.е.')
        except ValueError:
            print("Ошибка ввода")


# Вычет 10% от баланса, налога на богатство
def wealth_tax(person):
    balance = open_json.customer_account_lookup(person)
    if balance['balance'] > 5000000:
        if balance['number_operations'] == 1:
            balance['balance'] -= balance['balance'] * BaseClass.atm.wealth_tax / 100
            open_json.update_account_json(balance)
            deduction_10 = f"Налог на богатство 10%. Баланс: {balance['balance']}"
            open_json.new_operations(balance, deduction_10)
            print(deduction_10)


# начисление 3% за три операции
def accruals(account):
    if account['number_operations'] >= 3:
        account['balance'] += account['balance'] * BaseClass.atm.accruals
        account['number_operations'] = 0
        accrual_3 = f"За 3-ри выполненные операции, к балансу начислено 3% :-) Баланс: {account['balance']}$"
        open_json.new_operations(account, accrual_3)
        print(accrual_3)
        open_json.update_account_json(account)


