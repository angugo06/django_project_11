# Generated by Django 3.2.6 on 2021-08-24 23:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='files',
            field=models.FileField(default=None, upload_to='files'),
        ),
        migrations.AddField(
            model_name='post',
            name='img',
            field=models.ImageField(default=None, upload_to='img'),
        ),
    ]