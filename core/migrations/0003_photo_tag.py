# Generated by Django 2.0.5 on 2018-06-14 01:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_clientcontact'),
    ]

    operations = [
        migrations.AddField(
            model_name='photo',
            name='tag',
            field=models.CharField(default='test', max_length=20),
            preserve_default=False,
        ),
    ]
