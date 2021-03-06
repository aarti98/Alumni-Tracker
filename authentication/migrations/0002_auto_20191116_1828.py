# Generated by Django 2.2.7 on 2019-11-16 18:28

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='profile',
            field=models.CharField(choices=[('student', 'Student'), ('alumni', 'Alumni')], default='student', max_length=10),
        ),
        migrations.CreateModel(
            name='StudentDetail',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=20)),
                ('last_name', models.CharField(max_length=20)),
                ('contact_no', models.IntegerField()),
                ('birth_date', models.DateField()),
                ('course', models.CharField(max_length=50)),
                ('session_start', models.IntegerField()),
                ('session_end', models.IntegerField()),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
