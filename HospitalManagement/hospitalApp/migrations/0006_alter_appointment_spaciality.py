# Generated by Django 5.0.1 on 2024-03-15 08:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hospitalApp', '0005_alter_appointment_spaciality'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appointment',
            name='spaciality',
            field=models.CharField(max_length=50),
        ),
    ]
