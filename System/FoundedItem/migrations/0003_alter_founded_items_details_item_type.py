# Generated by Django 4.2.4 on 2023-09-02 13:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('FoundedItem', '0002_alter_founded_items_details_photo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='founded_items_details',
            name='item_type',
            field=models.CharField(max_length=200, null=True),
        ),
    ]
