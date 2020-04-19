# Generated by Django 3.0.5 on 2020-04-18 00:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('p_library', '0013_auto_20200418_0010'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='book',
            name='picture',
        ),
        migrations.AddField(
            model_name='book',
            name='book_cover',
            field=models.ImageField(blank=True, upload_to='images'),
        ),
    ]
