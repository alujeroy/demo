# Generated by Django 4.1.5 on 2023-02-13 07:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shopapp', '0003_rename_shop_category'),
        ('cartapp', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Cart_item',
            new_name='Cartitem',
        ),
        migrations.AlterModelTable(
            name='cartitem',
            table='Cartitem',
        ),
    ]
