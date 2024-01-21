from django.db import models
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.urls import reverse
from django.conf import settings


class Cart(models.Model):
    added_by = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=False)


    def get_absolute_url(self):
        return reverse('CartDetails',args=[self.id])
    



class CartItem(models.Model):
    cart = models.ForeignKey(Cart,on_delete=models.CASCADE)
    title = models.CharField(max_length=750)
    titleAr = models.CharField(max_length=750)
    count = models.PositiveIntegerField(default=1)

    # Listed below are the mandatory fields for a generic relation
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey()


    def deleteCartItem(self):
        return reverse('deleteItem',args=[self.id,self.cart.id])        


