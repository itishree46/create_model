# Generated by Django 4.1.4 on 2023-01-19 06:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_rename_nmae_access_records_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='access_records',
            name='date',
            field=models.DateField(),
        ),
    ]
