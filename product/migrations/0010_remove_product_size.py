# Generated by Django 5.0.6 on 2024-06-17 05:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0009_alter_product_size'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='size',
        ),
    ]
