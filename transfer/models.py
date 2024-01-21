from django.db import models
from django.conf import settings
from django.urls import reverse
from cart.models import CartItem
from django.contrib.contenttypes.fields import GenericRelation


class Car(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    ride_from = models.CharField(max_length=256)
    drop_off_to = models.CharField(max_length=256)
    ride_fromAr = models.CharField(max_length=256)
    drop_off_toAr = models.CharField(max_length=256)
    photo = models.ImageField(upload_to='cars/')
    Persons_number = models.IntegerField()
    bags_number = models.IntegerField()
    price = models.DecimalField(max_digits=8,decimal_places=2)
    is_active = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    cartItem = GenericRelation(CartItem) 


    def __str__(self):
        return str(self.ride_from+"_____"+self.drop_off_to)


    def get_absolute_url(self):
        return reverse('editCar',args=[self.id,self.ride_from])

    def delete_absolute_car(self):
        return reverse('deleteCar',args=[self.id])
    
    
    def itemDetailsAr(self):
        return reverse('carDetailsAr',args=[self.id])

    def itemDetails(self):
        return reverse('carDetails',args=[self.id])