# Generated by Django 2.2.2 on 2019-06-18 17:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todolist', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todolist',
            name='created',
            field=models.DateField(default='2019-06-18'),
        ),
        migrations.AlterField(
            model_name='todolist',
            name='due_date',
            field=models.DateField(default='2019-06-18'),
        ),
    ]