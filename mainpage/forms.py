from django import forms
from .models import Message
from phonenumber_field.formfields import PhoneNumberField



class MessageForm(forms.ModelForm):
    user_name = forms.CharField(label='',widget=forms.TextInput(attrs={'class':'form-control',
    'placeholder':'User Name'}))
    email = forms.EmailField(label='',widget=forms.EmailInput(attrs={'class':'form-control',
    'placeholder':'Email'}))
    phoneNumber = PhoneNumberField(
        # label='',widget=PhoneNumberPrefixWidget(country_choices=[

        #          ("syria", "+963"),

        #     ],

        # )
    )
    subject = forms.CharField(label='',widget=forms.TextInput(attrs={'class':'form-control',
    'placeholder':'Subject'}))
    message = forms.CharField(label='',widget=forms.Textarea(attrs={'class':'form-control',
    'placeholder':'Message'}))
    

    class Meta:
        model = Message
        fields = ('user_name','email',"phoneNumber",'subject','message')

class MessageFormAr(forms.ModelForm):
    user_name = forms.CharField(label='',widget=forms.TextInput(attrs={'class':'form-control',
    'placeholder':'الاسم'}))
    email = forms.EmailField(label='',widget=forms.EmailInput(attrs={'class':'form-control',
    'placeholder':'البريد الالكتروني'}))
    number = forms.EmailField(label='',widget=forms.EmailInput(attrs={'class':'form-control',
    'placeholder':"رقم الهاتف"}))
    subject = forms.CharField(label='',widget=forms.TextInput(attrs={'class':'form-control',
    'placeholder':'عنوان الرسالة'}))
    message = forms.CharField(label='',widget=forms.Textarea(attrs={'class':'form-control',
    'placeholder':'نص الرسالة'}))
    

    class Meta:
        model = Message
        fields = ('user_name','email','subject','message')