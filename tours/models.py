from django.db import models
from django.conf import settings
from django.urls import reverse

PACKAGE_TYPE = (('InBound','InBound'),('OutBound','OutBound'))
PACKAGE_TYPEAR = (('ضمن القطر','ضمن القطر'),('خارج القطر','خارج القطر'))

class Tour(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    title = models.CharField(max_length=256)
    tourType = models.CharField(max_length=30,choices=PACKAGE_TYPE,default='InBound')
    country = models.CharField(max_length=256,blank=True)
    titleAr = models.CharField(max_length=256)
    tourTypeAr = models.CharField(max_length=30,choices=PACKAGE_TYPEAR,default='ضمن القطر')
    countryAr = models.CharField(max_length=256,blank=True)
    photo = models.ImageField(upload_to='packages/')
    tourProgram = models.TextField(max_length=2000)
    tourProgramAr = models.TextField(max_length=2000)
    sdate = models.DateTimeField()
    edate = models.DateTimeField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    isActive = models.BooleanField(default=True)

    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse('editTour',args=[self.id,self.title])

    def delete_absolute_tour(self):
        return reverse('deleteTour',args=[self.id])

    def details(self):
        return reverse('TourDetails',args=[self.id,self.title])
    
    def detailsAr(self):
        return reverse('TourDetailsAr',args=[self.id,self.titleAr])
    
    def itemDetails(self):
        return reverse('tourItemCart',args=[self.id,self.title])
    
    def itemDetailsAr(self):
        return reverse('tourItemCartAr',args=[self.id,self.titleAr])


class TourImg(models.Model):
        tour = models.ForeignKey(Tour,on_delete=models.CASCADE)
        img = models.ImageField(upload_to='Tours/')
        
        def __str__(self):
            return str(self.tour)
        
        def delete_absolute_tour_img(self):
            return reverse('deletePackage',args=[self.id,self.tour,self.tour.title])

