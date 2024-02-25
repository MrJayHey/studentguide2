import json
import os
import asyncio
from rasp.models import Pair
from django.core.management.base import BaseCommand
from django.conf import settings
from playwright.async_api import async_playwright
from asgiref.sync import sync_to_async

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

async def save_to_database():
    # 2 paths that we need
    json_file_path = os.path.join(settings.BASE_DIR, 'rasp', 'data.json')
    groups_file_path = os.path.join(settings.BASE_DIR, 'rasp', 'groups.json')

    print('Started parsing process...')
    # Load groups data
    with open(groups_file_path, encoding='utf-8') as f:
        data = json.load(f)
    groups = list(data['groups'].keys())
    async with async_playwright() as playwright:
        chromium = playwright.chromium
        for group in groups:
            url = f"https://rasp.dmami.ru/json/?{group}"
            browser = await chromium.launch()
            page = await browser.new_page()

            async def handle_response(response):
                if "/group?" in response.url:
                    try:
                        data = await response.json()
                        grid = trash_from_json(data["grid"])
                        with open(json_file_path, 'w', encoding='utf-8') as f:
                            json.dump(grid, f, ensure_ascii=False)
                    except KeyError:
                        print(f"Skipping group {group} due to incorrect schedule")
                        return

            page.on("response", handle_response)
            await page.goto(url, wait_until="networkidle")

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
                        # Check if the pair already exists in the database
                        existing_pair = await sync_to_async(Pair.objects.filter(day=schedule.day, lesson_index=schedule.lesson_index, group=group).exists)()
                        if not existing_pair:
                            await sync_to_async(schedule.save)()
                            # print('Saved!')
                        else:
                            continue

            await page.close()
            await browser.close()

class Command(BaseCommand):
    help = 'Parse and save data to the database'

    def handle(self, *args, **options):
        asyncio.get_event_loop().run_until_complete(save_to_database())
