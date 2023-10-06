def get_date(date: str):
    date_num = date[0:10].split('-')
    return date_num[2] + '.' + date_num[1] + '.' + date_num[0]


print(get_date("2019-08-26T10:50:58.294041"))