# Generated by Django 3.1.7 on 2021-03-04 18:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('phoneshop', '0002_remove_category_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='image',
            field=models.ImageField(blank=True, upload_to='category'),
        ),
    ]