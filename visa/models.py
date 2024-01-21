from django.db import models
from django.urls import reverse
from django.conf import settings
from django.contrib.contenttypes.fields import GenericRelation
from cart.models import CartItem


class Visa(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    title = models.CharField(max_length=256)
    description = models.TextField(max_length=2000)
    titleAr = models.CharField(max_length=256)
    descriptionAr = models.TextField(max_length=2000)
    photo = models.ImageField(upload_to="visaPhoto/")
    cartItem = GenericRelation(CartItem) 
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)
  
    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('editVisa',args=[self.id,self.title])

    def delete_absolute_visa(self):
        return reverse('deleteVisa',args=[self.id])
    
    def itemDetails(self):
        return reverse('visaDetails',args=[self.id])
    
    def itemDetailsAr(self):
        return reverse('visaDetailsAr',args=[self.id])
    
   
