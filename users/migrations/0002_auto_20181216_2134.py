# Generated by Django 2.1.2 on 2018-12-16 20:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='image',
            field=models.ImageField(default='pdefault.jpg', upload_to='profile_pics'),
        ),
    ]
