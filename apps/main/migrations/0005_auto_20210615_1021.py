# Generated by Django 3.1.5 on 2021-06-15 17:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_auto_20210611_1109'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='bmi',
            options={'ordering': ['-created_at']},
        ),
    ]
