# Generated by Django 2.2.7 on 2019-11-16 20:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0003_alumnidetail'),
    ]

    operations = [
        migrations.AddField(
            model_name='studentdetail',
            name='picture',
            field=models.ImageField(blank=True, null=True, upload_to='images/'),
        ),
    ]
