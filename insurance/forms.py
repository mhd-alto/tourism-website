from django import forms
from .models import Insurance

class InsuranceForm(forms.ModelForm):
    from_age = forms.CharField(
        label='',widget=forms.TextInput(attrs={'placeholder':'From Age','class':'form-control form-control-user'}))
    to_age = forms.CharField(
        label='',widget=forms.TextInput(attrs={'placeholder':'To Age','class':'form-control form-control-user'}))
    period = forms.IntegerField(
        label='',widget=forms.TextInput(attrs={'placeholder':'Period','class':'form-control form-control-user'}))
    from_ageAr = forms.CharField(
        label='',widget=forms.TextInput(attrs={'placeholder':'من عُمر','class':'form-control form-control-user'}))
    to_ageAr = forms.CharField(
        label='',widget=forms.TextInput(attrs={'placeholder':' لعُمر','class':'form-control form-control-user'}))
    periodAr = forms.IntegerField(
        label='',widget=forms.TextInput(attrs={'placeholder':'المدة','class':'form-control form-control-user'}))
    price = forms.DecimalField(
        widget=forms.NumberInput(attrs={
            'placeholder':'Price','class':'form-control form-control-user'
        })
    )
    note = forms.CharField(
        widget=forms.Textarea(attrs={
            'placeholder':'Note','class':'form-control '
            
        })
    )
    noteAr = forms.CharField(
        widget=forms.Textarea(attrs={
            'placeholder':'ملاحظات','class':'form-control '
            
        })
    )
    
    class Meta:
        model = Insurance
        fields = ('from_age','to_age','period','from_ageAr','to_ageAr','periodAr','price',
        'note','noteAr','isActive')
   

