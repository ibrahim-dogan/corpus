# Generated by Django 2.2.2 on 2019-06-06 12:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('urlarchive', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'ordering': ['title'], 'verbose_name': 'Category', 'verbose_name_plural': 'Categories'},
        ),
        migrations.RenameField(
            model_name='category',
            old_name='name',
            new_name='title',
        ),
    ]