# Generated by Django 3.2.9 on 2021-12-24 11:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('teacher', '0005_auto_20211216_1126'),
    ]

    operations = [
        migrations.AlterField(
            model_name='exam',
            name='year',
            field=models.CharField(default='FE', max_length=50),
        ),
    ]