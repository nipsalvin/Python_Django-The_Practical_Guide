# Generated by Django 4.2.11 on 2024-05-27 16:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book_outlet', '0003_book_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='rating',
            field=models.IntegerField(),
        ),
    ]
