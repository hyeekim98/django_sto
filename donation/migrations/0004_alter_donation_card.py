# Generated by Django 3.2.5 on 2021-08-06 10:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('donation', '0003_auto_20210806_0946'),
    ]

    operations = [
        migrations.AlterField(
            model_name='donation',
            name='card',
            field=models.CharField(choices=[('hana', '하나'), ('woori', '우리'), ('kB', '국민'), ('shinhan', '신한')], max_length=10, verbose_name='카드사'),
        ),
    ]