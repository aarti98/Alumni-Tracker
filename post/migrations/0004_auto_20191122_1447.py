# Generated by Django 2.2.7 on 2019-11-22 14:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0003_auto_20191122_1445'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='post',
            field=models.TextField(null=True),
        ),
    ]
