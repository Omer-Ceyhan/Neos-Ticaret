# Generated by Django 5.0 on 2024-02-22 10:37

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0007_alter_product_content_alter_product_image'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name': 'Kategori', 'verbose_name_plural': 'Kategoriler'},
        ),
        migrations.AlterModelOptions(
            name='product',
            options={'verbose_name': 'ürün', 'verbose_name_plural': 'Ürünler'},
        ),
        migrations.AlterModelOptions(
            name='subcategory',
            options={'verbose_name': 'Alt Kategori', 'verbose_name_plural': 'Alt Kategoriler'},
        ),
        migrations.AddField(
            model_name='product',
            name='favorite',
            field=models.ManyToManyField(blank=True, related_name='favorites_user', to=settings.AUTH_USER_MODEL),
        ),
    ]