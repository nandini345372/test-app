# Generated by Django 3.1.4 on 2020-12-16 06:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='blogmodel',
            name='image',
            field=models.ImageField(blank=True, upload_to='images'),
        ),
    ]