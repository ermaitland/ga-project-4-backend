# Generated by Django 4.1.5 on 2023-01-18 17:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0005_alter_products_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='products',
            name='category',
            field=models.CharField(max_length=3),
        ),
    ]
