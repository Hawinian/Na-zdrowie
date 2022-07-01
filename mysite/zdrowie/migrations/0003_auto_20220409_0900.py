# Generated by Django 3.2.9 on 2022-04-09 09:00

from django.db import migrations, models
import zdrowie.models


class Migration(migrations.Migration):

    dependencies = [
        ('zdrowie', '0002_alter_book_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='description',
            field=models.TextField(default='None'),
        ),
        migrations.AlterField(
            model_name='book',
            name='image',
            field=models.FilePathField(path=zdrowie.models.images_path),
        ),
    ]