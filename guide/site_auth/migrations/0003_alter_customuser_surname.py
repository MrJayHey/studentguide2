# Generated by Django 4.2.5 on 2024-02-14 19:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('site_auth', '0002_remove_customuser_is_proforg_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='surname',
            field=models.CharField(blank=True, max_length=30),
        ),
    ]
