from atm import views, open_json
from atm.journal_printin import logging


def menu(person):
    num = input("Выберете действие (пополнить - 1, снять - 2, операции - 3, выход - 4): ")
    if num == '1':
        views.BalanceTopUp.balance_top_up(None, person)
    elif num == '2':
        views.CashWithdrawal.cash_withdrawal(None, person)
    elif num == '3':
        print("----------------------------------------")
        print("История операций:")
        print("----------------------------------------")
        open_json.operation_history(person)
        print("----------------------------------------")
    elif num == '4':
        logging.info(f"id={person['id']} Работа с банкоматом завершена")