# Generated by Django 4.1.4 on 2023-01-05 11:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='picture',
            field=models.ImageField(blank=True, upload_to='users_profile_pic/'),
        ),
    ]
