# Generated by Django 4.1.4 on 2023-01-11 02:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Agents', '0002_alter_agent_phone_number'),
    ]

    operations = [
        migrations.AlterField(
            model_name='agent',
            name='phone_number',
            field=models.PositiveIntegerField(max_length=13, unique=True),
        ),
    ]
