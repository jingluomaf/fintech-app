# Generated by Django 2.2.3 on 2019-08-01 01:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('collect', '0004_auto_20190801_1301'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='historicaldata',
            options={'managed': True, 'ordering': ['-date']},
        ),
    ]