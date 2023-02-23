import json
import datetime

def load_json():
    ''' функция выгрузки json'''
    with open('../operations.json', 'r', encoding='utf-8') as f:
        return json.load(f)
    # transactions_json = requests.get('https://file.notion.so/f/s/d22c7143-d55e-4f1d-aa98-e9b15e5e5efc/operations.json?spaceId=0771f0bb-b4cb-4a14-bc05-94cbd33fc70d&table=block&id=f11058ed-10ad-42ea-a13d-aad1945e5421&expirationTimestamp=1676819826971&signature=mlzGk6m1mIPlyKTMcpobeiA43GEZtI3ON_5ACWPMEz4&downloadName=operations.json').json()
    # return transactions_json

def transactions_executed():
    ''' функция перебора json и нахождение успешных операций игнорируя пустых записей в Json'''
    data = load_json()
    data_executed = []
    try:
        for i in range(len(data)):
            try:
                if data[i]['state'] == 'EXECUTED':
                    data_executed.append(data[i])
            except:
                continue
        return data_executed
    except:
        data_executed.append('Неверная ссылка')
        return data_executed

def sort_by_date():
    ''' Сортировка списка выполненых операций по дате'''
    data_executed = transactions_executed()
    sort_name = sorted(data_executed, key=lambda x: datetime.datetime.fromisoformat(x['date']))
    return sort_name

def hidden_account_from(operation_sort, number):
    ''' Вывод информации откуда был выполнен перевод и скрытие информации о номере в зависимости от типа счёта(Visa,MasterCard и т.д.) '''
    check_from = operation_sort[number]['from']
    split_from = check_from.split()
    hidden_account = ''
    if split_from[0].lower() == "maestro" or split_from[0].lower() == 'mastercard':
        for i in range(len(split_from[1])):
            if i in range(6, 12):
                hidden_account += split_from[1][i].replace(split_from[1][i], '*')
            else:
                hidden_account += split_from[1][i]
        return print(split_from[0],hidden_account[:4],hidden_account[4:8],hidden_account[8:12],hidden_account[12:16],hidden_account[16:20],end = ' -> ')
    elif split_from[0].lower() == "visa":
        for i in range(len(split_from[2])):
            if i in range(6, 12):
                hidden_account += split_from[2][i].replace(split_from[2][i], '*')
            else:
                hidden_account += split_from[2][i]
        return print(split_from[0],split_from[1],hidden_account[:4],hidden_account[4:8],hidden_account[8:12],hidden_account[12:16],hidden_account[16:20],end = ' -> ')
    else:
        for i in range(len(split_from[1])):
            if i in range(0, 16):
                hidden_account += split_from[1][i].replace(split_from[1][i], '*')
            else:
                hidden_account += split_from[1][i]
        return print(split_from[0], hidden_account[-6:],end = ' -> ')

def hidden_account_to(operation_sort, number):
    ''' Вывод информации куда был выполнен перевод и скрытие информации о номере в зависимости от типа счёта(Visa,MasterCard и т.д.)'''
    check_to = operation_sort[number]['to']
    split_to = check_to.split()
    hidden_account = ''
    if split_to[0].lower() == "maestro" or split_to[0].lower() == 'mastercard':
        for i in range(len(split_to[1])):
            if i in range(6, 12):
                hidden_account += split_to[1][i].replace(split_to[1][i], '*')
            else:
                hidden_account += split_to[1][i]
        return print(split_to[0], hidden_account[:4], hidden_account[4:8], hidden_account[8:12], hidden_account[12:16],
                     hidden_account[16:20])
    elif split_to[0].lower() == "visa":
        for i in range(len(split_to[2])):
            if i in range(6, 12):
                hidden_account += split_to[2][i].replace(split_to[2][i], '*')
            else:
                hidden_account += split_to[2][i]
        return print(split_to[0], split_to[1], hidden_account[:4], hidden_account[4:8], hidden_account[8:12], hidden_account[12:16],
                     hidden_account[16:20])
    else:
        for i in range(len(split_to[1])):
            if i in range(0, 16):
                hidden_account += split_to[1][i].replace(split_to[1][i], '*')
            else:
                hidden_account += split_to[1][i]
        return print(split_to[0], hidden_account[-6:])

def date_output(operation_sort, number):
    ''' Вывод информации о дате операции в формате ДД.ММ.ГГГГ '''
    date = datetime.datetime.fromisoformat(operation_sort[number]['date']).date()
    return print(f"{date.day}.{date.month}.{date.year} {operation_sort[number]['description']}")

def transfer_amount_currency(operation_sort, number):
    ''' Вывод информации о сумме и валюте операции '''
    return print(f'{operation_sort[number]["operationAmount"]["amount"]} {operation_sort[number]["operationAmount"]["currency"]["name"]}\n')