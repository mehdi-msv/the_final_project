# Generated by Django 4.2.13 on 2024-07-10 16:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='image',
            field=models.ImageField(default='blog/blog-img2.png', upload_to='blog/'),
        ),
    ]