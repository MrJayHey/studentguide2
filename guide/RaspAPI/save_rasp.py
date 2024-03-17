import requests
import json
def save_rasp():
    url = "https://rasp.dmami.ru/semester.json"

    response = requests.get(url)

    # Проверяем успешность запроса
    if response.status_code == 200:
        # Преобразуем JSON ответ в словарь
        data = response.json()

        # Сохраняем данные в файл
        with open('RaspAPI/data_rasp.json', 'w', encoding='utf-8') as file:
            json.dump(data, file, ensure_ascii=False, indent=4)

        return True
    else:
        return False