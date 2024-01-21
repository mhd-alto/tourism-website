from django import forms
from django.forms import ModelForm
from .models import Tour,TourImg
from django.forms import modelformset_factory

class TourForm(forms.ModelForm):
    title = forms.CharField(
        label='',widget=forms.TextInput(attrs={'placeholder':'Title','class':'form-control form-control-user'}))
    country = forms.CharField(
        label='',widget=forms.TextInput(attrs={'placeholder':'Country','class':'mx-auto form-control form-control-user'}))
    tourProgram = forms.CharField(
        label='',widget=forms.Textarea(attrs={'placeholder':'TourProgram','class':'form-control'}))
    titleAr = forms.CharField(
        label='',widget=forms.TextInput(attrs={'placeholder':'العنوان','class':'form-control form-control-user'}))
    countryAr = forms.CharField(
        label='',widget=forms.TextInput(attrs={'placeholder':'المنطقة','class':'mx-auto form-control form-control-user'}))
    tourProgramAr = forms.CharField(
        label='',widget=forms.Textarea(attrs={'placeholder':'برنامج الرحلة','class':'form-control'}))
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
        model = Tour
        fields = ('title','tourType','country','titleAr','tourTypeAr','countryAr','photo','tourProgram','tourProgramAr','sdate','edate','isActive')
   

   


class ImgTourForm(forms.ModelForm):
    class Meta:
        model = TourImg
        fields = ('img',)

imgTourFormset = modelformset_factory(
    TourImg,
    form=ImgTourForm,
    extra=1,
    can_delete=True,
    can_delete_extra=True,   
)


