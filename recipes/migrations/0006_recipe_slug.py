# Generated by Django 4.1.4 on 2023-01-03 18:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0005_alter_recipeingredient_recipe'),
    ]

    operations = [
        migrations.AddField(
            model_name='recipe',
            name='slug',
            field=models.SlugField(null=True, unique=True),
        ),
    ]
