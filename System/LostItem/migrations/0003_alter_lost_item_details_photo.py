# Generated by Django 4.2.4 on 2023-08-30 12:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('LostItem', '0002_alter_lost_item_details_additional_comments'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lost_item_details',
            name='photo',
            field=models.FileField(default=None, max_length=250, null=True, upload_to='lost_items/'),
        ),
    ]
