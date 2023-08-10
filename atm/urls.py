from atm import views, open_json


def menu(person):
    num = input("Выберете действие (пополнить - 1, снять - 2, операции - 3, выход - 4): ")
    if num == '1':
        views.TopUp.balance_top_up(None, person)
    elif num == '2':
        views.Cash.cash_withdrawal(None, person)
    elif num == '3':
        print("----------------------------------------")
        print("История операций:")
        print("----------------------------------------")
        open_json.operation_history(person)
        print("----------------------------------------")
    elif num == '4':
        print("Работа с банкоматом завершена")