# Generated by Django 4.2.7 on 2023-11-04 07:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='record',
            name='application_date',
            field=models.DateField(),
        ),
    ]
