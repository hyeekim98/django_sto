# Generated by Django 3.2.5 on 2021-08-09 17:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('donation', '0023_alter_donation_card'),
    ]

    operations = [
        migrations.AlterField(
            model_name='donation',
            name='card',
            field=models.CharField(choices=[('woori', '우리'), ('hana', '하나'), ('shinhan', '신한'), ('kB', '국민')], max_length=10, verbose_name='카드사'),
        ),
    ]
