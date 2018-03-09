# Generated by Django 2.0.2 on 2018-03-09 17:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courseapp', '0011_auto_20180306_1141'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='lesson',
            name='course',
        ),
        migrations.RemoveField(
            model_name='litem',
            name='lesson',
        ),
        migrations.AddField(
            model_name='course',
            name='lessons',
            field=models.ManyToManyField(to='courseapp.Lesson'),
        ),
        migrations.AddField(
            model_name='lesson',
            name='litems',
            field=models.ManyToManyField(to='courseapp.Litem'),
        ),
    ]