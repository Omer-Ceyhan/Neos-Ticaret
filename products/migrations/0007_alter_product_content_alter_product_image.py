# Generated by Django 5.0 on 2024-02-20 12:28

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0006_product_created_at_product_owner'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='content',
            field=ckeditor.fields.RichTextField(verbose_name='Ürün Açıklaması'),
        ),
        migrations.AlterField(
            model_name='product',
            name='image',
            field=models.FileField(default='', null=True, upload_to='products/'),
        ),
    ]
