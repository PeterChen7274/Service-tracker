# Generated by Django 4.2.9 on 2024-01-12 01:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("taskapp", "0006_rename_ding_task_ding"),
    ]

    operations = [
        migrations.AddField(
            model_name="task",
            name="period_days",
            field=models.IntegerField(default=0, verbose_name="Period (Days)"),
        ),
    ]