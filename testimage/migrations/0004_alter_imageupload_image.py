# Generated by Django 3.2.6 on 2021-08-22 13:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('testimage', '0003_alter_imageupload_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='imageupload',
            name='image',
            field=models.ImageField(default='', upload_to='image/'),
        ),
    ]
