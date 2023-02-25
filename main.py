from utils import utils

operation_sort = utils.sort_by_date()
try:
    for num in range(len(operation_sort), len(operation_sort) - 5, -1):
        print(utils.date_output(operation_sort,num - 1))
        try:
            print(utils.hidden_account_from(operation_sort, num - 1),end='-> ')
            print(utils.hidden_account_to(operation_sort, num - 1))
        except:
            print(utils.hidden_account_to(operation_sort, num - 1))
        print(utils.transfer_amount_currency(operation_sort, num - 1))
except:
    print('Неверная ссылка')