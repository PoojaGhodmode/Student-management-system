# Generated by Django 3.1.7 on 2021-05-02 19:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='subject',
            name='total_lec_alloted',
            field=models.IntegerField(default=1),
        ),
    ]
