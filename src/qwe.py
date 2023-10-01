import json

with open('operations.json', encoding='utf-8') as file:
    data = json.load(file)
    print(data)

"""import json

try:
    with open('operations.json') as file:
        data = json.load(file)
        print(data)
except Exception as e:
    print("Произошла ошибка:", str(e))"""