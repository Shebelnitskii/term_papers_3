import requests
import datetime

def load_json():
    ''' функция выгрузки json'''
    transactions_json = requests.get('https://file.notion.so/f/s/d22c7143-d55e-4f1d-aa98-e9b15e5e5efc/operations.json?spaceId=0771f0bb-b4cb-4a14-bc05-94cbd33fc70d&table=block&id=f11058ed-10ad-42ea-a13d-aad1945e5421&expirationTimestamp=1676715784166&signature=8VqIM33J1Hasw50YJhM1bXPs9HfKgnhSwXhpOXxTUzg&downloadName=operations.json').json()
    return transactions_json

def transactions_executed():
    ''' функция перебора json и нахождение успешных операций игнорируя пустых записей в Json'''
    data = load_json()
    data_executed = []
    for i in range(len(data)):
        try:
            if data[i]['state'] == 'EXECUTED':
                data_executed.append(data[i])
        except:
            continue
    return data_executed

#'%y-%m-%dT%H:%M:%S.%f'

def sort_by_date():
    ''' Сортировка списка выполненых операций по дате'''
    data_executed = transactions_executed()
    sort_name = sorted(data_executed, key=lambda x: datetime.datetime.fromisoformat(x['date']))
    return sort_name