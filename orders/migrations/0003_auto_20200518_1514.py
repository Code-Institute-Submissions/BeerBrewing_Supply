# Generated by Django 3.0.6 on 2020-05-18 15:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0002_order_status'),
    ]

    operations = [
        migrations.RenameField(
            model_name='order',
            old_name='klarna_line_items',
            new_name='cart',
        ),
    ]
