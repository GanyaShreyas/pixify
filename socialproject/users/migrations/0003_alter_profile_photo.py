# Generated by Django 5.0.6 on 2024-07-08 17:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_alter_profile_photo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='photo',
            field=models.ImageField(default='media/users/2024/0706/default-profile-photo.jpg', upload_to='users/%Y/%m%d'),
        ),
    ]
