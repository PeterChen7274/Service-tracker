# Generated by Django 4.2.9 on 2024-01-12 03:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("taskapp", "0012_task_extended"),
    ]

    operations = [
        migrations.AlterField(
            model_name="task",
            name="name",
            field=models.CharField(max_length=255, unique=True),
        ),
    ]
