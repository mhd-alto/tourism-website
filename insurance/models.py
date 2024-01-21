from django.db import models
from django.conf import settings
from django.urls import reverse



class Insurance(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    from_age = models.CharField(max_length=256)
    to_age = models.CharField(max_length=256)
    period = models.CharField(max_length=256)
    from_ageAr = models.CharField(max_length=256)
    to_ageAr = models.CharField(max_length=256)
    periodAr = models.CharField(max_length=256)
    price = models.DecimalField(max_digits=8,decimal_places=2)
    note = models.TextField(max_length=1000)
    noteAr = models.TextField(max_length=1000)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    isActive = models.BooleanField(default=True)

    def __str__(self):
        return "from__"+self.from_age+"__to___"+self.to_age


    def get_absolute_url(self):
        return reverse('editInsurance', args=[self.id,self])

    def itemDetails(self):
        return reverse('insuranceDetails',args=[self.id])
    
    def itemDetailsAr(self):
        return reverse('insuranceDetailsAr',args=[self.id])
