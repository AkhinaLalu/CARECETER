# Generated by Django 5.1.6 on 2025-03-04 09:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('careapp', '0005_otpmodel'),
    ]

    operations = [
        migrations.AlterField(
            model_name='staffdetails',
            name='certificate',
            field=models.JSONField(default=list),
        ),
    ]
