# Generated by Django 3.1.5 on 2021-05-25 21:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_bmi_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='bmi',
            name='age',
            field=models.CharField(default=None, max_length=255),
        ),
        migrations.AddField(
            model_name='bmi',
            name='height',
            field=models.CharField(default=None, max_length=255),
        ),
        migrations.AddField(
            model_name='bmi',
            name='waist',
            field=models.CharField(default=None, max_length=255),
        ),
        migrations.AddField(
            model_name='bmi',
            name='weight',
            field=models.CharField(default=None, max_length=255),
        ),
    ]
