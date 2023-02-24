import json
import datetime

def load_json():
    ''' функция выгрузки json'''
    try:
        with open('C://Users/Шебельницкие/PycharmProjects/term_papers_3/operations.json', 'r', encoding='utf-8') as f:
            return json.load(f)
    except:
        return 'ошибка файла'

def transactions_executed():
    ''' функция перебора json и нахождение успешных операций игнорируя пустых записей в Json'''
    data = load_json()
    data_executed = []
    try:
        for i in range(len(data)): ### Проход по всему списку на поиск и добавление в новый список по статусу "Успешных операций"
            try:
                if data[i]['state'] == 'EXECUTED':
                    data_executed.append(data[i])
            except:
                continue
        return data_executed
    except:
        data_executed.append('Неверный формат файла')
        return data_executed

def sort_by_date():
    ''' Сортировка списка выполненых операций по дате'''
    data_executed = transactions_executed()
    sort_name = sorted(data_executed, key=lambda x: datetime.datetime.fromisoformat(x['date']))
    return sort_name

def hidden_account_from(operation_sort, number):
    ''' Вывод информации откуда был выполнен перевод и скрытие информации о номере в зависимости от типа счёта(Visa,MasterCard и т.д.) '''

    split_from = operation_sort[number]['from'].split() ### Разделение from по пробелу
    hidden_account = '' ### Пустая строка в которую после перебора добавятся нужные символы в зависимости от кол-ва символов в номере счёта

    if split_from[0].lower() == "maestro" or split_from[0].lower() == 'mastercard':
        ### проверка по первому значению списка после split

        for i in range(len(split_from[1])):
            if i in range(6, 12): ### Все символы с 6-го по 12 заменяются на *
                hidden_account += split_from[1][i].replace(split_from[1][i], '*')
            else:
                hidden_account += split_from[1][i]
        ### Вывод информации после переборки текста split_from[0] Это Maestro/MasterCard, hidden_account разделяется по 4-е символа
        hidden_output = split_from[0] + ' ' + hidden_account[:4] + ' ' + hidden_account[4:8] + ' ' + hidden_account[8:12] + ' ' + hidden_account[12:16] + ' ' + hidden_account[16:20]
        return hidden_output

    elif split_from[0].lower() == "visa":
        ### если в первом индекск после сплита стоит Visa то второй индекс будет Gold/platinum и тд, по этому перебор номера счёта идёт по индексу 2
        for i in range(len(split_from[2])):
            if i in range(6, 12):
                hidden_account += split_from[2][i].replace(split_from[2][i], '*')
            else:
                hidden_account += split_from[2][i]
        hidden_output = split_from[0] + ' ' + split_from[1] + ' ' + hidden_account[:4] + ' ' + hidden_account[4:8] + ' ' + hidden_account[8:12] + ' ' + hidden_account[12:16] + ' ' + hidden_account[16:20]
        return hidden_output

    else:
        ### в последнем случае это номер счёта, в котором 20 символов, и соответсветсвенно показываются последние 6 символов
        for i in range(len(split_from[1])):
            if i in range(0, 16):
                hidden_account += split_from[1][i].replace(split_from[1][i], '*')
            else:
                hidden_account += split_from[1][i]
        ### Вывод последних 6-ти символов, при этом первые 16 из 20 символов заменены на звёздочку
        hidden_output = split_from[0] + ' ' + hidden_account[-6:]
        return hidden_output

def hidden_account_to(operation_sort, number):
    ''' Вывод информации куда был выполнен перевод и скрытие информации о номере в зависимости от типа счёта(Visa,MasterCard и т.д.)'''
    split_to = operation_sort[number]['to'].split() ### Разделение to по пробелу
    hidden_account = ''  ### Пустая строка в которую после перебора добавятся нужные символы в зависимости от кол-ва символов в номере счёта

    if split_to[0].lower() == "maestro" or split_to[0].lower() == 'mastercard':
        ### проверка по первому значению списка после split

        for i in range(len(split_to[1])):
            if i in range(6, 12): ### Все символы с 6-го по 12 заменяются на *
                hidden_account += split_to[1][i].replace(split_to[1][i], '*')
            else:
                hidden_account += split_to[1][i]
        ### Вывод информации после переборки текста split_from[0] Это Maestro/MasterCard, hidden_account разделяется по 4-е символа
        return print(split_to[0], hidden_account[:4], hidden_account[4:8], hidden_account[8:12], hidden_account[12:16],hidden_account[16:20])

    elif split_to[0].lower() == "visa":
        ### если в первом индекск после сплита стоит Visa то второй индекс будет Gold/platinum и тд, по этому перебор номера счёта идёт по индексу 2
        for i in range(len(split_to[2])):
            if i in range(6, 12):
                hidden_account += split_to[2][i].replace(split_to[2][i], '*')
            else:
                hidden_account += split_to[2][i]
        return print(split_to[0], split_to[1], hidden_account[:4], hidden_account[4:8], hidden_account[8:12], hidden_account[12:16],
                     hidden_account[16:20])
    else:
        ### в последнем случае это номер счёта, в котором 20 символов, и соответсветсвенно показываются последние 6 символов
        for i in range(len(split_to[1])):
            if i in range(0, 16):
                hidden_account += split_to[1][i].replace(split_to[1][i], '*')
            else:
                hidden_account += split_to[1][i]
        ### Вывод последних 6-ти символов, при этом первые 16 из 20 символов заменены на звёздочку
        return print(split_to[0], hidden_account[-6:])

def date_output(operation_sort, number):
    ''' Вывод информации о дате операции в формате ДД.ММ.ГГГГ '''
    date = datetime.datetime.fromisoformat(operation_sort[number]['date']).date()
    return print(f"{date.day}.{date.month}.{date.year} {operation_sort[number]['description']}")

def transfer_amount_currency(operation_sort, number):
    ''' Вывод информации о сумме и валюте операции '''
    return print(f'{operation_sort[number]["operationAmount"]["amount"]} {operation_sort[number]["operationAmount"]["currency"]["name"]}\n')
