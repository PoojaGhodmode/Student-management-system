# Generated by Django 3.1.7 on 2021-05-14 15:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('management', '0002_teacherattendance'),
    ]

    operations = [
        migrations.AddField(
            model_name='studentattendance',
            name='subject',
            field=models.CharField(max_length=10, null=True),
        ),
    ]
