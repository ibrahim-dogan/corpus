# Generated by Django 2.2.1 on 2019-05-11 13:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_auto_20190511_1601'),
    ]

    operations = [
        migrations.AlterField(
            model_name='file',
            name='uuid',
            field=models.CharField(default='old', max_length=50),
        ),
    ]