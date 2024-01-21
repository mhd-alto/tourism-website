from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from django.urls import reverse
from taggit.managers import TaggableManager
from django.conf import settings



GENDER = (("Male","Male"),("Female","Female"))

class Profile(models.Model):    
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    date_of_birth = models.DateField(blank=True)
    picture = models.ImageField(upload_to="users_profile_pic/", blank=True)
    phone_number = PhoneNumberField(blank=True)
    gender = models.CharField(max_length=30,choices=GENDER,blank=True)

    def __str__(self):
        return f"{self.user.username}'s Profile"



class Blog(models.Model):
    title = models.CharField(max_length=256)
    titleAr = models.CharField(max_length=256)
    photo = models.ImageField(upload_to='blog_image/')
    slug = models.SlugField()
    tags = TaggableManager()
    description = models.TextField(max_length=1000)
    descriptionAr = models.TextField(max_length=1000)
    is_active = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)


    def __str__(self):
        return self.title
    
    def get_absolute_url(self):  
        return reverse('editBlog',args=[self.id,self.slug])

    def delete_absolute_blog(self):
        return reverse('deleteBlog',args=[self.id])
    
    def details(self):
        return reverse('blogsDetails',args=[self.id,self.slug])

    def detailAr(self):
        return reverse('blogsDetailsAr',args=[self.id,self.titleAr])

class Slider(models.Model):
    title = models.CharField(max_length=256)
    description = models.TextField()
    titleAr = models.CharField(max_length=256)
    descriptionAr = models.TextField()
    sliderimg = models.ImageField(upload_to='slidermainimgs/',default='static/index/assets/img/hero-bg.jpg')
    url = models.URLField(blank=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('editSlide',args=[self.id,self.title])

    def deleteslide(self):
        return reverse('deleteSlider')

class WhyUs(models.Model):
    title = models.CharField(max_length=256)
    titleAr = models.CharField(max_length=256)
    description = models.TextField() 
    descriptionAr = models.TextField() 
    img = models.ImageField(upload_to='whyUs/')
    videoUrl = models.URLField()
    question_one = models.CharField(max_length=500)
    answer_one = models.CharField(max_length=750) 
    question_two = models.CharField(max_length=500)
    answer_two = models.CharField(max_length=750) 
    question_three = models.CharField(max_length=500)
    answer_three = models.CharField(max_length=750) 
    question_oneAr = models.CharField(max_length=500)
    answer_oneAr = models.CharField(max_length=750) 
    question_twoAr = models.CharField(max_length=500)
    answer_twoAr = models.CharField(max_length=750) 
    question_threeAr = models.CharField(max_length=500)
    answer_threeAr = models.CharField(max_length=750) 


class FAQ(models.Model):
    question_one = models.CharField(max_length=500)
    answer_one = models.CharField(max_length=750) 
    question_two = models.CharField(max_length=500)
    answer_two = models.CharField(max_length=750) 
    question_three = models.CharField(max_length=500)
    answer_three = models.CharField(max_length=750) 
    question_four = models.CharField(max_length=500)
    answer_four = models.CharField(max_length=750) 
    question_five = models.CharField(max_length=500)
    answer_five = models.CharField(max_length=750) 

class FAQAR(models.Model):
    question_one = models.CharField(max_length=500)
    answer_one = models.CharField(max_length=750) 
    question_two = models.CharField(max_length=500)
    answer_two = models.CharField(max_length=750) 
    question_three = models.CharField(max_length=500)
    answer_three = models.CharField(max_length=750) 
    question_four = models.CharField(max_length=500)
    answer_four = models.CharField(max_length=750) 
    question_five = models.CharField(max_length=500)
    answer_five = models.CharField(max_length=750) 


    