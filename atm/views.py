from os import environ
from atm.models import Atm
from atm.open_json import customer_account_lookup, date_time, new_operations, update_account_json
from atm.journal_printin import logging

environ['TERM'] = 'xterm'

atm = Atm(0.015, 10, 600, 30, 0.03, 3)


class BalanceTopUp:
    def balance_top_up(self, customer):
        wealth_tax(customer)
        requested_amount = input_amount(customer)
        account = customer_account_lookup(customer)
        if requested_amount > 0:
            account['balance'] += requested_amount
            account['number_operations'] += 1
            account['data_time'] = date_time()
            update_account_json(account)
            replenishment = f'Баланс пополнен на {requested_amount}$, на вашем счете: {account["balance"]}$'
            new_operations(account, replenishment)
            logging.info(
                f'id={customer["id"]} {replenishment}')
            accruals(account, requested_amount)


class CashWithdrawal:
    def cash_withdrawal(self, customer):
        wealth_tax(customer)
        requested_amount = input_amount(customer)
        account = customer_account_lookup(customer)
        if requested_amount > 0:
            percentages = max(min(requested_amount * atm.withdrawal_fee, atm.max_fee),
                              atm.min_fee)
            summa = requested_amount - percentages
            if summa + percentages <= account['balance']:
                account['balance'] -= summa + percentages
                account['number_operations'] += 1
                account['data_time'] = date_time()
                withdrawal = f"{account['id']} Выдано наличных {requested_amount - percentages}$, Остаток на балансе: {account['balance']}"
                new_operations(account, withdrawal)
                logging.info(withdrawal)

                accruals(account, requested_amount)
                update_account_json(account)
            else:
                logging.error(f"id={account['id']} На счете недостаточно средств!")


def input_amount(customer):
    while True:
        requested_amount = 0
        try:
            requested_amount = int(input("Введите сумму: "))
        except ValueError as e:
            logging.error(f"id={customer['id']} Ошибка ввода: {e}")
        if requested_amount % 50 == 0 and requested_amount > 0:
            return requested_amount
        else:
            logging.error(f'id={customer["id"]} Ошибка: сумма должна быть кратна 50 у.е.')


def wealth_tax(customer):
    balance = customer_account_lookup(customer)
    if balance['balance'] > 5000000:
        if balance['number_operations'] == 1:
            balance['balance'] -= balance['balance'] * atm.wealth_tax / 100
            balance['data_time'] = date_time()
            update_account_json(balance)
            deduction_10 = f"id={balance['id']} Налог на богатство 10%. Баланс: {balance['balance']}"
            new_operations(balance, deduction_10)
            logging.info(deduction_10)


def accruals(account, requested_amount):
    if account['number_operations'] >= 3:
        account['balance'] += requested_amount * atm.accruals
        account['number_operations'] = 0
        account['data_time'] = date_time()
        accrual_3 = f"id={account['id']} За 3-ри выполненные операции, начислено 3% к сумме последней операции. Баланс: {account['balance']}$"
        new_operations(account, accrual_3)
        logging.info(accrual_3)
        update_account_json(account)


