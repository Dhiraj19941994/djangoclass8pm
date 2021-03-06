# Generated by Django 3.1.7 on 2021-03-25 15:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0002_auto_20210313_2123'),
        ('teacher', '0009_delete_detail'),
    ]

    operations = [
        migrations.CreateModel(
            name='TeacherPP',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pp', models.ImageField(upload_to='')),
                ('admin', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='teacher_profile_picture', to='user.teacherprofile')),
            ],
        ),
    ]
