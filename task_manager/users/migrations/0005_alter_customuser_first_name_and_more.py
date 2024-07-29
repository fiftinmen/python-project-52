# Generated by Django 5.0.7 on 2024-07-28 13:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("users", "0004_alter_customuser_options_alter_customuser_managers_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="customuser",
            name="first_name",
            field=models.CharField(max_length=150, verbose_name="First name"),
        ),
        migrations.AlterField(
            model_name="customuser",
            name="last_name",
            field=models.CharField(max_length=150, verbose_name="Last name"),
        ),
        migrations.AlterField(
            model_name="customuser",
            name="username",
            field=models.CharField(
                help_text="Обязательное поле. Не более 150 символов. Только буквы, цифры и символы @/./+/-/_.",
                max_length=150,
                unique=True,
                verbose_name="Username",
            ),
        ),
    ]