# Generated by Django 4.1.2 on 2022-12-06 10:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('basket', '0001_initial'),
        ('mainapp', '0003_rename_description_productcategories_descriptions_and_more'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Product',
            new_name='Exhibits',
        ),
        migrations.RenameModel(
            old_name='ProductCategories',
            new_name='ExhibitsCategories',
        ),
    ]
