# Generated by Django 5.0.6 on 2024-06-12 07:00

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0002_category_productvariant_alter_product_image_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProductCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.CharField(max_length=255)),
            ],
        ),
        migrations.RemoveField(
            model_name='product',
            name='variant_name',
        ),
        migrations.RemoveField(
            model_name='productvarianttype',
            name='variant_name',
        ),
        migrations.AlterField(
            model_name='product',
            name='image',
            field=models.ImageField(blank=True, upload_to='static/blog'),
        ),
        migrations.AlterField(
            model_name='product',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='product.productcategory'),
        ),
        migrations.DeleteModel(
            name='ProductVariant',
        ),
        migrations.DeleteModel(
            name='ProductVariantType',
        ),
        migrations.DeleteModel(
            name='Category',
        ),
    ]