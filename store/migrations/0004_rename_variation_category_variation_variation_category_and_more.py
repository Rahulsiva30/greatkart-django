# Generated by Django 5.1.1 on 2024-10-04 04:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0003_rename_created_date_product_created_date_variation'),
    ]

    operations = [
        migrations.RenameField(
            model_name='variation',
            old_name='Variation_category',
            new_name='variation_category',
        ),
        migrations.RenameField(
            model_name='variation',
            old_name='Variation_value',
            new_name='variation_value',
        ),
    ]
