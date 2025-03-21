# Generated by Django 5.1.6 on 2025-03-03 08:48

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Applicant',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('country_code', models.CharField(default='+1', max_length=10)),
                ('phone_number', models.CharField(max_length=20)),
                ('password', models.CharField(max_length=100)),
                ('job_applied', models.CharField(max_length=255)),
                ('dob', models.DateField()),
                ('preferred_areas', models.TextField()),
                ('house_number', models.CharField(blank=True, max_length=50, null=True)),
                ('address', models.TextField()),
                ('nationality', models.CharField(max_length=100)),
                ('gender', models.CharField(choices=[('Male', 'Male'), ('Female', 'Female'), ('Other', 'Other')], max_length=10)),
                ('image', models.ImageField(blank=True, null=True, upload_to='applicants/images/')),
                ('certificate', models.FileField(blank=True, null=True, upload_to='applicants/certificates/')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
