# Generated by Django 2.2.7 on 2019-11-19 08:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='post',
            field=models.TextField(blank=True, null=True),
        ),
    ]
