# Generated by Django 3.1.7 on 2021-04-12 20:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='payment_intent',
            field=models.CharField(blank=True, max_length=255),
        ),
    ]