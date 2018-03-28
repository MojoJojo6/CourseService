# Generated by Django 2.0.2 on 2018-03-28 11:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('cat_id', models.BigAutoField(primary_key=True, serialize=False)),
                ('cat_name', models.CharField(max_length=50)),
                ('cat_desc', models.CharField(blank=True, max_length=200, null=True)),
                ('cat_icon_url', models.URLField(blank=True, null=True)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('date_modified', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Course',
            fields=[
                ('cid', models.BigAutoField(primary_key=True, serialize=False)),
                ('course_name', models.CharField(max_length=50)),
                ('course_description', models.CharField(max_length=200)),
                ('faculty', models.BigIntegerField(blank=True, null=True)),
                ('course_icon_url', models.URLField(blank=True, null=True)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('date_modified', models.DateTimeField(auto_now=True)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='courses', to='courseapp.Category')),
            ],
        ),
        migrations.CreateModel(
            name='Lesson',
            fields=[
                ('lid', models.BigAutoField(primary_key=True, serialize=False)),
                ('lesson_name', models.CharField(max_length=50)),
                ('lesson_seqnum', models.IntegerField(null=True)),
                ('lesson_desc', models.CharField(max_length=200)),
                ('lesson_icon_url', models.URLField(blank=True, null=True)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('date_modified', models.DateTimeField(auto_now=True)),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='lessons', to='courseapp.Course')),
            ],
        ),
        migrations.CreateModel(
            name='Litem',
            fields=[
                ('liid', models.BigAutoField(primary_key=True, serialize=False)),
                ('litem_name', models.CharField(max_length=50)),
                ('litem_seqnum', models.IntegerField(null=True)),
                ('litem_desc', models.CharField(max_length=200)),
                ('litem_icon_url', models.URLField(blank=True, null=True)),
                ('litem_asset_url', models.URLField(blank=True, null=True)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('date_modified', models.DateTimeField(auto_now=True)),
                ('lesson', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='litems', to='courseapp.Lesson')),
            ],
        ),
    ]
