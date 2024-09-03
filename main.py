import requests

# URL для API
url = "https://playground.learnqa.ru/ajax/api/compare_query_type"

# 1. Делает http-запрос любого типа без параметра method
response = requests.get(url)  # Используем GET-запрос
print("1. Ответ на GET-запрос без параметра method:")
print(response.text)
print()

# 2. Делает http-запрос не из списка (например, HEAD)
response = requests.head(url)  # Используем HEAD-запрос
print("2. Ответ на HEAD-запрос:")
print(response.text)
print()

# 3. Делает запрос с правильным значением method (например, POST)
response = requests.post(url, data={"method": "POST"})  # Используем POST с параметром method
print("3. Ответ на POST-запрос с правильным значением method:")
print(response.text)
print()

# 4. Проверяем все возможные сочетания реальных типов запроса и значений параметра method
http_methods = ['GET', 'POST', 'PUT', 'DELETE']
method_values = ['GET', 'POST', 'PUT', 'DELETE']

# Проверяем все комбинации
for http_method in http_methods:
    for method_value in method_values:
        if http_method == 'GET':
            response = requests.get(url, params={"method": method_value})
        else:
            response = requests.request(http_method, url, data={"method": method_value})

        print(f"Запрос: {http_method}, method: {method_value} -> Ответ: {response.text}")