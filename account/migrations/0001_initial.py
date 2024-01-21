# Generated by Django 4.1.4 on 2023-01-05 11:25

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import phonenumber_field.modelfields
import taggit.managers


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('taggit', '0005_auto_20220424_2025'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='FAQ',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question_one', models.CharField(max_length=500)),
                ('answer_one', models.CharField(max_length=750)),
                ('question_two', models.CharField(max_length=500)),
                ('answer_two', models.CharField(max_length=750)),
                ('question_three', models.CharField(max_length=500)),
                ('answer_three', models.CharField(max_length=750)),
                ('question_four', models.CharField(max_length=500)),
                ('answer_four', models.CharField(max_length=750)),
                ('question_five', models.CharField(max_length=500)),
                ('answer_five', models.CharField(max_length=750)),
            ],
        ),
        migrations.CreateModel(
            name='FAQAR',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question_one', models.CharField(max_length=500)),
                ('answer_one', models.CharField(max_length=750)),
                ('question_two', models.CharField(max_length=500)),
                ('answer_two', models.CharField(max_length=750)),
                ('question_three', models.CharField(max_length=500)),
                ('answer_three', models.CharField(max_length=750)),
                ('question_four', models.CharField(max_length=500)),
                ('answer_four', models.CharField(max_length=750)),
                ('question_five', models.CharField(max_length=500)),
                ('answer_five', models.CharField(max_length=750)),
            ],
        ),
        migrations.CreateModel(
            name='Slider',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=256)),
                ('description', models.TextField()),
                ('titleAr', models.CharField(max_length=256)),
                ('descriptionAr', models.TextField()),
                ('sliderimg', models.ImageField(default='static/index/assets/img/hero-bg.jpg', upload_to='slidermainimgs/')),
                ('url', models.URLField(blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='WhyUs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=256)),
                ('titleAr', models.CharField(max_length=256)),
                ('description', models.TextField()),
                ('descriptionAr', models.TextField()),
                ('img', models.ImageField(upload_to='whyUs/')),
                ('videoUrl', models.URLField()),
                ('question_one', models.CharField(max_length=500)),
                ('answer_one', models.CharField(max_length=750)),
                ('question_two', models.CharField(max_length=500)),
                ('answer_two', models.CharField(max_length=750)),
                ('question_three', models.CharField(max_length=500)),
                ('answer_three', models.CharField(max_length=750)),
                ('question_oneAr', models.CharField(max_length=500)),
                ('answer_oneAr', models.CharField(max_length=750)),
                ('question_twoAr', models.CharField(max_length=500)),
                ('answer_twoAr', models.CharField(max_length=750)),
                ('question_threeAr', models.CharField(max_length=500)),
                ('answer_threeAr', models.CharField(max_length=750)),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_of_birth', models.DateField()),
                ('picture', models.ImageField(blank=True, default='users_profile_pic/default_profile_pic.jpg', upload_to='users_profile_pic/')),
                ('phone_number', phonenumber_field.modelfields.PhoneNumberField(blank=True, max_length=128, region=None)),
                ('gender', models.CharField(blank=True, max_length=30)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=256)),
                ('titleAr', models.CharField(max_length=256)),
                ('photo', models.ImageField(upload_to='blog_image/')),
                ('slug', models.SlugField()),
                ('description', models.TextField(max_length=1000)),
                ('descriptionAr', models.TextField(max_length=1000)),
                ('is_active', models.BooleanField(default=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('tags', taggit.managers.TaggableManager(help_text='A comma-separated list of tags.', through='taggit.TaggedItem', to='taggit.Tag', verbose_name='Tags')),
            ],
        ),
    ]
