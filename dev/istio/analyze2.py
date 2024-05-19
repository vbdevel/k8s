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

# Функция для рекурсивного поиска фильтров внутри HttpConnectionManager
def find_http_filters(config):
    if '@type' in config and config['@type'] == 'type.googleapis.com/envoy.extensions.filters.network.http_connection_manager.v3.HttpConnectionManager':
        return config.get('httpFilters', [])
    return []

# Проверка структуры данных и вывод для отладки
if parsed_json_data:
    filters = []
    for listener in parsed_json_data:
        if 'filterChains' in listener:
            for filter_chain in listener['filterChains']:
                if 'filters' in filter_chain:
                    for filter in filter_chain['filters']:
                        filter_info = {
                            "filter_name": filter.get("name", "No name provided"),
                            "filter_type": filter.get("typedConfig", {}).get("@type", "No type provided")
                        }
                        filters.append(filter_info)
                        
                        # Проверяем наличие http_filters внутри HttpConnectionManager
                        if filter_info['filter_name'] == 'envoy.filters.network.http_connection_manager':
                            http_filters = find_http_filters(filter.get('typedConfig', {}))
                            for http_filter in http_filters:
                                http_filter_info = {
                                    "filter_name": http_filter.get("name", "No name provided"),
                                    "filter_type": http_filter.get("typedConfig", {}).get("@type", "No type provided")
                                }
                                filters.append(http_filter_info)
                                print(http_filter_info)  # выводим информацию о каждом http фильтре для отладки

# Возвращаем собранные данные для дальнейшего анализа
filters

