# Generated by Django 4.2.4 on 2023-09-02 13:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('FoundedItem', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='founded_items_details',
            name='photo',
            field=models.ImageField(blank=True, null=True, upload_to='founded_items/'),
        ),
    ]