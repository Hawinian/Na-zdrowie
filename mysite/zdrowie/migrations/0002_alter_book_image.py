# Generated by Django 4.0.3 on 2022-04-05 08:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('zdrowie', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='image',
            field=models.ImageField(upload_to='images'),
        ),
    ]
