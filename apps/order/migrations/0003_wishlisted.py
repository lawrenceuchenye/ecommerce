# Generated by Django 3.1.7 on 2021-04-20 13:43

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('store', '0012_product_quantity'),
        ('order', '0002_auto_20210418_2145'),
    ]

    operations = [
        migrations.CreateModel(
            name='WishListed',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.IntegerField(default=1)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='wishlisted_items', to='store.product')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='wishlisted', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
