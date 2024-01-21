from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from django.urls import reverse



class Message(models.Model):
    user_name = models.CharField(max_length=256)
    email = models.EmailField()
    phoneNumber = PhoneNumberField()
    subject = models.CharField(max_length=256)
    message = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.user_name

    def get_absolute_url(self):
        return reverse('messageDetails',args=[self.id] )
