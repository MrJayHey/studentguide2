import json
import os
from .models import Pair
from django.conf import settings
from playwright.sync_api import sync_playwright
from asgiref.sync import async_to_sync

def trash_from_json(jsn):
    # Remove trash from JSON
    for day in jsn.values():
        for pairs in day.values():
            for pair in pairs:
                pair.pop("dts")
                pair.pop("auditories")
                pair.pop("week")
                pair.pop("align")
                pair.pop("e_link")
    return jsn

def save_to_database():
    # 2 paths that we need
    json_file_path = os.path.join(settings.BASE_DIR, 'rasp', 'data.json')
    groups_file_path = os.path.join(settings.BASE_DIR, 'rasp', 'groups.json')

    # Load groups data
    with open(groups_file_path, 'r', encoding='utf-8') as f:
        groups_data = json.load(f)

    groups = list(groups_data['groups'].keys())

    playwright = sync_playwright().start()
    chromium = playwright.chromium

    def handle_response(response):
        if "/group?" in response.url:
            with open(json_file_path, 'w', encoding='utf-8') as f:
                json.dump(trash_from_json(response.json()["grid"]), f, ensure_ascii=False)

    for group in groups:
        url = f"https://rasp.dmami.ru/json/?{group}"
        browser = chromium.launch()
        page = browser.new_page()
        page.on("response", handle_response)
        page.goto(url, wait_until="networkidle")

        with open(json_file_path, encoding='utf-8') as f:
            parsed_data = json.load(f)

        for day_index, day_data in parsed_data.items():
            for lesson_index, lesson_list in day_data.items():
                for lesson in lesson_list:
                    schedule = Pair(
                        day=int(day_index),
                        lesson_index=int(lesson_index),
                        sbj=lesson.get('sbj', ''),
                        teacher=lesson.get('teacher', ''),
                        df=lesson.get('df', ''),
                        dt=lesson.get('dt', ''),
                        shortRooms=lesson.get('shortRooms', []),
                        location=lesson.get('location', ''),
                        type=lesson.get('type', ''),
                        group=group
                    )
                    schedule.save()

        page.context.close()
        browser.close()

    playwright.stop()

# Convert async code to sync
async_to_sync(save_to_database)()
