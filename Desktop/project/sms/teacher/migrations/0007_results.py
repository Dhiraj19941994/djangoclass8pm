# Generated by Django 3.1.7 on 2021-03-24 14:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0002_auto_20210313_2123'),
        ('teacher', '0006_auto_20210316_2045'),
    ]

    operations = [
        migrations.CreateModel(
            name='results',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('microprocessor', models.IntegerField()),
                ('digital_logic', models.IntegerField()),
                ('maths', models.IntegerField()),
                ('english', models.IntegerField()),
                ('database', models.IntegerField()),
                ('coa', models.IntegerField()),
                ('admin', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user.studentprofile')),
            ],
        ),
    ]
