from django.db import models
from django.conf import settings
from django.urls import reverse

PACKAGE_TYPE = (('InBound','InBound'),('OutBound','OutBound'))
PACKAGE_TYPEAR = (('ضمن القطر','ضمن القطر'),('خارج القطر','خارج القطر'))

class Package(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    title = models.CharField(max_length=256)
    titleAr = models.CharField(max_length=256)
    packageType = models.CharField(max_length=30,choices=PACKAGE_TYPE,default='InBound')
    packageTypeAr = models.CharField(max_length=30,choices=PACKAGE_TYPEAR,default='ضمن القطر')
    country = models.CharField(max_length=256,blank=True)
    countryAr = models.CharField(max_length=256,blank=True)
    photo = models.ImageField(upload_to='packages/')
    packageProgram = models.TextField(max_length=2000)
    packageProgramAr = models.TextField(max_length=2000)
    sdate = models.DateTimeField()
    edate = models.DateTimeField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    isActive = models.BooleanField(default=True)

    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse('editPackage',args=[self.id,self.title])

    def delete_absolute_package(self):
        return reverse('deletePackage',args=[self.id])

    def details(self):
        return reverse('packageDetails',args=[self.id,self.title])
   
    def detailsAr(self):
        return reverse('packageDetailsAr',args=[self.id,self.titleAr])
    
    def itemDetails(self):
        return reverse('packageItemCart',args=[self.id,self.title])

    def itemDetailsAr(self):
        return reverse('packageItemCartAr',args=[self.id,self.titleAr])


class PackageImg(models.Model):
        Package = models.ForeignKey(Package,on_delete=models.CASCADE)
        img = models.ImageField(upload_to='packages/')
        
        def __str__(self):
            return str(self.Package)
        
        def delete_absolute_package_img(self):
            return reverse('deletePackage',args=[self.id,self.Package,self.Package.title])

