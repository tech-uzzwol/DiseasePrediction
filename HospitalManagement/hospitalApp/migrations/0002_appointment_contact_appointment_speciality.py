# Generated by Django 5.0.1 on 2024-03-15 10:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hospitalApp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='appointment',
            name='contact',
            field=models.CharField(max_length=10, null=True),
        ),
        migrations.AddField(
            model_name='appointment',
            name='speciality',
            field=models.CharField(max_length=50, null=True),
        ),
    ]
