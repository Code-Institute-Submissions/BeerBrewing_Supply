# Generated by Django 3.0.6 on 2020-05-18 15:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0003_auto_20200518_1514'),
    ]

    operations = [
        migrations.RenameField(
            model_name='order',
            old_name='cart',
            new_name='klarna_line_items',
        ),
    ]
