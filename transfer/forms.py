from django import forms
from .models import Car

class TransferForm(forms.ModelForm):
    ride_from = forms.CharField(
        label='',widget=forms.TextInput(attrs={'placeholder':'Ride From','class':'form-control form-control-user'}))
    drop_off_to = forms.CharField(
        label='',widget=forms.TextInput(attrs={'placeholder':'Drop Off To','class':'form-control form-control-user'}))
    ride_fromAr = forms.CharField(
        label='',widget=forms.TextInput(attrs={'placeholder':'من','class':'form-control form-control-user'}))
    drop_off_toAr = forms.CharField(
        label='',widget=forms.TextInput(attrs={'placeholder':'إلى','class':'form-control form-control-user'}))
    Persons_number = forms.IntegerField(
        label='',widget=forms.NumberInput(attrs={'placeholder':'Persons Number','class':'form-control form-control-user'}))
    bags_number = forms.IntegerField(
        widget=forms.NumberInput(attrs={
            'placeholder':'Bags Number','class':'form-control form-control-user'
        })
    )
    price = forms.DecimalField(
        widget=forms.NumberInput(attrs={
            'placeholder':'Price','class':'form-control form-control-user'
            
        })
    )
    
    class Meta:
        model = Car
        fields = ('ride_from','drop_off_to','ride_fromAr','drop_off_toAr','photo','Persons_number','bags_number','price','is_active')
   

