# Generated by Django 3.2.6 on 2021-08-25 00:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_auto_20210824_1903'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='files',
            field=models.FileField(null=True, upload_to='files'),
        ),
        migrations.AlterField(
            model_name='post',
            name='img',
            field=models.ImageField(null=True, upload_to='img'),
        ),
    ]