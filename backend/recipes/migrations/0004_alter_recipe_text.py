# Generated by Django 3.2.13 on 2022-08-17 21:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0003_auto_20220817_1734'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recipe',
            name='text',
            field=models.TextField(help_text='Введите описание рецепта', max_length=2048, verbose_name='Описание рецепта'),
        ),
    ]
