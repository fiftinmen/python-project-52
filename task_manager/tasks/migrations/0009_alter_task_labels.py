# Generated by Django 5.0.6 on 2024-07-22 16:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("labels", "0001_initial"),
        ("tasks", "0008_alter_task_labels"),
    ]

    operations = [
        migrations.AlterField(
            model_name="task",
            name="labels",
            field=models.ManyToManyField(
                blank=True, through="tasks.TaskLabels", to="labels.label"
            ),
        ),
    ]
