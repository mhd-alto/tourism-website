from django import forms
from django.forms import ModelForm
from .models import Package,PackageImg
from django.forms import modelformset_factory

class PackageForm(forms.ModelForm):
    title = forms.CharField(
        label='',widget=forms.TextInput(attrs={'placeholder':'Title','class':'form-control form-control-user'}))
    titleAr = forms.CharField(
        label='',widget=forms.TextInput(attrs={'placeholder':'عنوان','class':'form-control form-control-user'}))
    country = forms.CharField(
        label='',widget=forms.TextInput(attrs={'placeholder':'Country','class':'mx-auto form-control form-control-user'}))
    countryAr = forms.CharField(
        label='',widget=forms.TextInput(attrs={'placeholder':'المنطقة','class':'mx-auto form-control form-control-user'}))
    packageProgram = forms.CharField(
        label='',widget=forms.Textarea(attrs={'placeholder':'packageProgram','class':'form-control'}))
    packageProgramAr = forms.CharField(
        label='',widget=forms.Textarea(attrs={'placeholder':'(الوصف)برنامج','class':'form-control'}))
    sdate = forms.DateTimeField(
        widget=forms.DateTimeInput(attrs={
            'class': 'form-control datetimepicker-input',
            'type':'datetime-local'
        })
    )
    edate = forms.DateTimeField(
        widget=forms.DateTimeInput(attrs={
            'class': 'form-control datetimepicker-input',
            'type':'datetime-local'
        })
    )
    
    class Meta:
        model = Package
        fields = ('title','packageType','country','titleAr','packageTypeAr','countryAr','photo','packageProgram',
        'packageProgramAr','sdate','edate','isActive')
   

   


class ImgForm(forms.ModelForm):
    class Meta:
        model = PackageImg
        fields = ('img',)

imgFormset = modelformset_factory(
    PackageImg,
    form=ImgForm,
    extra=1,
    can_delete=True,
    can_delete_extra=True,   
)


