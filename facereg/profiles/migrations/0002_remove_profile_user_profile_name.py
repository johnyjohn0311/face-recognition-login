# Generated by Django 5.1.3 on 2024-12-07 22:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='user',
        ),
        migrations.AddField(
            model_name='profile',
            name='name',
            field=models.CharField(max_length=50, null=True),
        ),
    ]