import json


def remove_keys(data):

    if isinstance(data, dict):
        for key in list(data.keys()):
            if key in ['week', 'align', 'e_link',"auditories","dts"]:
                del data[key]
            else:
                remove_keys(data[key])
    elif isinstance(data, list):
        for item in data:
            remove_keys(item)




def rasp_grup(grup:str):

    with open('RaspAPI/data_rasp.json', 'r', encoding='utf-8') as file:
        data = json.load(file)

    if grup in data["contents"] :
        rasp = data["contents"][grup]["grid"]
    else:
        return "Расписание группы не найдено"

    new_days = {
            "1": "monday",
            "2": "tuesday",
            "3": "wednesday",
            "4": "thursday",
            "5": "friday",
            "6": "saturday",
    }

    new_pairs = {
        "1": "first",
        "2": "second",
        "3": "third",
        "4": "fourth",
        "5": "fifth",
        "6": "sixth",
        "7": "seventh",
    }

    new_jsn = {}
    for weekday in rasp:
        new_jsn[new_days[weekday]] = rasp[weekday]

    for day_key in new_jsn:
        for old_pair_key in new_pairs:
            tmp = new_jsn[day_key][old_pair_key]
            new_jsn[day_key][new_pairs[old_pair_key]] = tmp
            new_jsn[day_key].pop(old_pair_key)

    remove_keys(new_jsn)

    return new_jsn






