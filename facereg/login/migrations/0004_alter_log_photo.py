# Generated by Django 5.1.3 on 2024-12-08 14:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0003_log_profile'),
    ]

    operations = [
        migrations.AlterField(
            model_name='log',
            name='photo',
            field=models.ImageField(blank=True, upload_to='login'),
        ),
    ]
