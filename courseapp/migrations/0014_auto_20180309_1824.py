# Generated by Django 2.0.2 on 2018-03-09 18:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courseapp', '0013_auto_20180309_1433'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lesson',
            name='lesson_desc',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
