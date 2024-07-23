# Generated by Django 5.0.6 on 2024-07-22 16:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("labels", "0001_initial"),
        ("tasks", "0007_tasklabels_task_labels"),
    ]

    operations = [
        migrations.AlterField(
            model_name="task",
            name="labels",
            field=models.ManyToManyField(
                blank=True, null="", through="tasks.TaskLabels", to="labels.label"
            ),
        ),
    ]