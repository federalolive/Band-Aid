# Generated by Django 3.1.5 on 2021-02-04 04:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0004_album_band'),
    ]

    operations = [
        migrations.AlterField(
            model_name='album',
            name='release_date',
            field=models.DateField(verbose_name='release date'),
        ),
    ]
