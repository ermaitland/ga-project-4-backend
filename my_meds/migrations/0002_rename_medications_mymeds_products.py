# Generated by Django 4.1.5 on 2023-01-24 11:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('my_meds', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='mymeds',
            old_name='medications',
            new_name='products',
        ),
    ]