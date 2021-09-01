# Generated by Django 3.2.7 on 2021-09-01 14:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0002_rename_heading_topic'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='image',
            name='image_file',
        ),
        migrations.AddField(
            model_name='image',
            name='image',
            field=models.ImageField(default='no_image.jpg', upload_to='products'),
        ),
    ]
