from django import forms
from .models import Visa

class VisaForm(forms.ModelForm):
    title = forms.CharField(
        label='',widget=forms.TextInput(attrs={'placeholder':'Title','class':'form-control form-control-user'}))
    description = forms.CharField(
        label='',widget=forms.Textarea(attrs={'placeholder':'description','class':'mx-auto form-control'}))
    titleAr = forms.CharField(
        label='',widget=forms.TextInput(attrs={'placeholder':'عنوان','class':'form-control form-control-user'}))
    descriptionAr = forms.CharField(
        label='',widget=forms.Textarea(attrs={'placeholder':'وصف','class':'mx-auto form-control'}))
    
    class Meta:
        model = Visa
        fields = ('title','description','photo',"titleAr","descriptionAr")
