# Generated by Django 5.0.7 on 2024-07-31 11:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0002_variations'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Variations',
            new_name='Variation',
        ),
    ]
