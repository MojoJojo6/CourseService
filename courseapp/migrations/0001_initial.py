# Generated by Django 2.0.2 on 2018-02-25 17:49

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('cid', models.BigAutoField(primary_key=True, serialize=False)),
                ('course_name', models.CharField(max_length=50)),
                ('course_description', models.CharField(max_length=200)),
                ('faculty_id', models.BigIntegerField()),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('date_modified', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
