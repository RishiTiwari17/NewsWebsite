# Generated by Django 5.0.6 on 2024-12-23 13:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserSubsDetails',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=100)),
                ('contact', models.IntegerField()),
                ('city', models.CharField(max_length=100)),
                ('state', models.CharField(max_length=100)),
                ('country', models.CharField(max_length=100)),
                ('order_id', models.CharField(default='blank', max_length=100)),
                ('order_payment_id', models.CharField(default='blank', max_length=100)),
                ('order_signature_id', models.CharField(default='blank', max_length=100)),
            ],
        ),
    ]
