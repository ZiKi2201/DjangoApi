# Generated by Django 2.2.5 on 2019-09-28 14:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0004_auto_20190928_1718'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='end_time',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='article',
            name='start_time',
            field=models.DateField(),
        ),
    ]
