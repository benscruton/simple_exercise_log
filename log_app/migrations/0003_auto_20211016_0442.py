# Generated by Django 2.2.4 on 2021-10-16 04:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('log_app', '0002_auto_20211015_2238'),
    ]

    operations = [
        migrations.AlterField(
            model_name='workout',
            name='date',
            field=models.DateField(blank=True, null=True),
        ),
    ]
