# Generated by Django 5.0.6 on 2024-07-13 15:39

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("tasks", "0004_alter_task_description_alter_task_executor"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AlterField(
            model_name="task",
            name="author",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.PROTECT,
                related_name="task_author",
                to=settings.AUTH_USER_MODEL,
            ),
        ),
        migrations.AlterField(
            model_name="task",
            name="executor",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.PROTECT,
                related_name="task_executor",
                to=settings.AUTH_USER_MODEL,
            ),
        ),
    ]
