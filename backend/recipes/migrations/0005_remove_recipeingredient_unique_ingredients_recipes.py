# Generated by Django 3.2.13 on 2022-08-17 22:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0004_alter_recipe_text'),
    ]

    operations = [
        migrations.RemoveConstraint(
            model_name='recipeingredient',
            name='unique_ingredients_recipes',
        ),
    ]
