from django.db import models
from django.contrib.postgres.fields import ArrayField

class Pair(models.Model):
    sbj = models.CharField(max_length=512)
    teacher = models.CharField(max_length=256)
    df = models.DateField()
    dt = models.DateField()
    shortRooms = ArrayField(models.CharField(max_length=50), blank=True, default=list)
    location = models.CharField(max_length=512)
    type = models.CharField(max_length=50)
    day = models.CharField(max_length=2)
    lesson_index = models.IntegerField()
    group = models.CharField(max_length=64)
    
    days = {
        "1": "Понедельник",
        "2": "Вторник",
        "3": "Среда",
        "4": "Четверг",
        "5": "Пятница",
        "6": "Суббота",
    }
    
    time = {
        '1': '9:00 10:30',
        '2': '10:40 12:10',
        '3': '12:20 13:50',
        '4': '14:30 16:00',
        '5': '16:10 17:40',
        '6': '17:50 19:20',
        '7': '19:30 21:00',
        
    }
    
    def get_lesson_time(self):
        return self.time[str(self.lesson_index)]
    
    def __str__(self):
        return f"Группа {self.group} пара в день недели - {self.days.get(self.day)}. Пара - {self.sbj}"
    