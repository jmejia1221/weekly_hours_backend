# Generated by Django 2.1.4 on 2018-12-17 14:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('manageHours', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='requestinvitation',
            name='created',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
