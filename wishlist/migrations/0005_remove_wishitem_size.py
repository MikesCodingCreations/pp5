# Generated by Django 3.0.1 on 2024-05-14 15:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('wishlist', '0004_wishitem_quantity'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='wishitem',
            name='size',
        ),
    ]
