import json


def rasp():

    with open('RaspAPI/data_grup.json', 'r', encoding='utf-8') as file:
        data = json.load(file)

    return data