# Generated by Django 5.0.1 on 2024-03-15 08:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hospitalApp', '0002_appointment_contact'),
    ]

    operations = [
        migrations.AddField(
            model_name='appointment',
            name='spaciality',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='appointment',
            name='contact',
            field=models.CharField(max_length=10),
        ),
    ]
