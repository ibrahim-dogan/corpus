# Generated by Django 2.2.2 on 2019-06-06 18:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('urlarchive', '0003_auto_20190606_1547'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='icon',
            field=models.CharField(default='fas fa-link', max_length=50),
            preserve_default=False,
        ),
    ]
