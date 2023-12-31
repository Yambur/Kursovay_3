def filter_and_sorting(data: list):
    """
    Определяет операцию по State
    И выводит с самой ранней датой
    """
    items = [item for item in data if item.get('state') == "EXECUTED"]
    items.sort(key=lambda x: x.get('date'), reverse=True)
    return items


def get_date(date: str):
    """
    Переворачивает дату на нужную нам
    """
    date_num = date[0:10].split('-')
    return date_num[2] + '.' + date_num[1] + '.' + date_num[0]


def mask_prepare_message_number(message):
    """
    Будет определять карта или счет
    """
    # если в json не было ключей from и to
    if message is None:
        return 'Личный счет'

    message_split = message.split(' ')
    if message_split[0] == 'Счет':
        hidden_number = mask_account_number(message_split[-1])
    else:
        hidden_number = mask_card_number(message_split[-1])

    return ' '.join(message_split[:-1]) + ' ' + hidden_number


def mask_card_number(number: str):
    """
    Проверяет, правильно ли написан номер карты
    """
    if number.isdigit() and len(number) == 16:
        return number[:4] + ' ' + number[4:6] + '** **** ' + number[-4:]
    else:
        print('номер карты не подходит')


def mask_account_number(number: str):
    """
    Определяет, подходит ли номер счета
    """
    if number.isdigit() and len(number) >= 4:
        return "**" + number[-4:]
    else:
        print('номер счета не подходит')


def prepare_user_message(item: dict):
    date = get_date(item.get('date'))
    desc = item.get('description')
    from_ = mask_prepare_message_number(item.get('from'))
    to_ = mask_prepare_message_number(item.get('to'))
    amount = item.get('operationAmount').get('amount')
    curr = item.get('operationAmount').get('currency').get('name')

    return f'{date} {desc}\n{from_} -> {to_}\n{amount} {curr}\n'