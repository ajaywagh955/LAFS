# Generated by Django 4.2.4 on 2023-09-04 12:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('LostItem', '0005_alter_lost_item_details_photo'),
    ]

    operations = [
        migrations.CreateModel(
            name='Names',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
            ],
        ),
    ]
