from utils import utils

operation_sort = utils.sort_by_date()
try:
    for num in range(len(operation_sort), len(operation_sort) - 5, -1):
        utils.date_output(operation_sort,num - 1)
        try:
            utils.hidden_account_from(operation_sort, num - 1)
            utils.hidden_account_to(operation_sort, num - 1)
        except:
            utils.hidden_account_to(operation_sort, num - 1)
        utils.transfer_amount_currency(operation_sort, num - 1)
except:
    print('Неверная ссылка')