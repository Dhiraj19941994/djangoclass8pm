# Generated by Django 3.1.7 on 2021-03-16 14:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('teacher', '0003_studentattendence'),
    ]

    operations = [
        migrations.CreateModel(
            name='FoundItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('found_item_name', models.CharField(max_length=80)),
                ('found_item_detail', models.CharField(max_length=80)),
                ('found_item_image', models.CharField(max_length=80)),
            ],
        ),
    ]
