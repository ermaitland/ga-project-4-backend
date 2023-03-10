# Generated by Django 4.1.5 on 2023-01-19 08:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0008_alter_products_category'),
        ('requests', '0002_alter_requests_text'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='requests',
            name='item_name',
        ),
        migrations.AddField(
            model_name='requests',
            name='products',
            field=models.ForeignKey(default=7, on_delete=django.db.models.deletion.CASCADE, related_name='requests', to='products.products'),
            preserve_default=False,
        ),
    ]
