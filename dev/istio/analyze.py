import json

# Чтение файла JSON
file_path = 'listener_config.json'  # замените путь на ваш путь к listener_config.json
with open(file_path, 'r') as file:
    data = file.read()

# Парсинг JSON данных
try:
    parsed_json_data = json.loads(data)
except json.JSONDecodeError as error:
    print(f"Ошибка парсинга JSON данных: {error}")
    parsed_json_data = None

# Проверка структуры данных и вывод для отладки
if parsed_json_data:
    for listener in parsed_json_data:
        if 'filterChains' in listener:
            for filter_chain in listener['filterChains']:
                if 'filters' in filter_chain:
                    for filter in filter_chain['filters']:
                        print(f"Фильтр: {filter.get('name')}")
                        if 'typedConfig' in filter:
                            print(f"Тип конфигурации: {filter['typedConfig'].get('@type')}")
                        else:
                            print("Нет конфигурации typedConfig")

# Вывод отладочной информации
parsed_json_data

