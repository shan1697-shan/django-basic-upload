# Generated by Django 3.2.6 on 2021-08-22 09:11

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Imageupload',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('caption', models.CharField(blank=True, max_length=100)),
                ('image', models.ImageField(upload_to='testimage/image')),
            ],
        ),
    ]