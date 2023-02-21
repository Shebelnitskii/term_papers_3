import json
import datetime

def load_json():
    ''' функция выгрузки json'''
    with open('operations.json', 'r', encoding='utf-8') as f:
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

# def output_trans_info():
# new = sort_by_date()
# try:
#     for i in range(len(new),len(new)-5,-1):
#         print(new[i - 1]['date'])
#         print(new[i-1]["description"],new[i-1]["to"])
#         print(new[i-1]['operationAmount']['amount'],new[i-1]['operationAmount']['currency']['name'])
# except:
#     print('Неверная ссылка')