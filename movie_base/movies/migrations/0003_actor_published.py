# Generated by Django 3.2 on 2022-06-01 15:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0002_auto_20220601_1817'),
    ]

    operations = [
        migrations.AddField(
            model_name='actor',
            name='published',
            field=models.BooleanField(default=False, verbose_name='Published'),
        ),
    ]
