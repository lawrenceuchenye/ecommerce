# Generated by Django 3.1.7 on 2021-04-09 19:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0007_auto_20210409_1808'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='slug',
            field=models.SlugField(default=2, max_length=255),
            preserve_default=False,
        ),
    ]
