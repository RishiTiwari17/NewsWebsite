# Generated by Django 5.0.6 on 2024-12-23 13:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0002_usersubsdetails'),
    ]

    operations = [
        migrations.AddField(
            model_name='usersubsdetails',
            name='amount',
            field=models.IntegerField(default=0),
        ),
    ]
