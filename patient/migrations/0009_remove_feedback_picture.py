# Generated by Django 2.1.5 on 2021-07-14 05:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('patient', '0008_auto_20210714_1050'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='feedback',
            name='picture',
        ),
    ]
