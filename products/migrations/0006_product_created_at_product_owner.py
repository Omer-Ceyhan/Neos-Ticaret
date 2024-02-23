# Generated by Django 5.0 on 2024-02-20 10:44

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0005_subcategory_product_sub_category'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, null=True, verbose_name='Oluşturulma Tarihi'),
        ),
        migrations.AddField(
            model_name='product',
            name='owner',
            field=models.ForeignKey(editable=False, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Satıcı'),
        ),
    ]
