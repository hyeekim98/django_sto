# Generated by Django 3.2.5 on 2021-08-09 10:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('funding', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='funding',
            name='goal_price',
            field=models.IntegerField(default=0),
        ),
    ]