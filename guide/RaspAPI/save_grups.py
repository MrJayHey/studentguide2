import requests
import json
from bs4 import BeautifulSoup


def save_grups():

    response = requests.get("https://rasp.dmami.ru/")

    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')

        scripts = soup.find_all('script')

        for script in scripts:
            if 'globalListGroups' in script.text:
                # Извлекаем содержимое скрипта с переменной globalListGroups
                script_text = script.text
                start_pos = script_text.find('{')
                end_pos = script_text.rfind('}') + 1
                data = script_text[start_pos:end_pos]


                data = json.loads(data)

                with open('RaspAPI/data_grup.json', 'w', encoding='utf-8') as file:
                    json.dump(data, file, ensure_ascii=False, indent=4)
        return True
    else:
        return False

