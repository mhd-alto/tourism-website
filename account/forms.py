from django import forms
from django.contrib.auth.models import User
from .models import FAQ, Blog,Slider,WhyUs,FAQAR
from django.forms.widgets import SelectDateWidget
from .models import Profile
from datetime import datetime
from phonenumber_field.formfields import PhoneNumberField
from phonenumber_field.widgets import PhoneNumberPrefixWidget
from django.core.exceptions import ValidationError


class UserRegistrationForm(forms.ModelForm):
    username = forms.CharField(
        label='',widget=forms.TextInput(attrs={'placeholder':'UserName','class':'form-control form-control-lg'}))
    email = forms.CharField(
        label='',widget=forms.EmailInput(attrs={'placeholder':'Email','class':'form-control form-control-lg'}))
    password = forms.CharField(
        label='',widget=forms.PasswordInput(attrs={'placeholder': 'Password','class':'form-control form-control-lg'}))
    confirm_password = forms.CharField(
        label='',widget=forms.PasswordInput(
            attrs={'placeholder': 'confirm password','class':'form-control form-control-lg'}))

    class Meta:
        model = User
        fields = ("username", "email")
        help_texts = {
            'username': None,
        }

    def clean_confirm_password(self):
        cd = self.cleaned_data
        if cd["password"] != cd["confirm_password"]:
            raise forms.ValidationError("Passwords don't match")
        return cd["confirm_password"]
    
    def clean(self):
       email = self.cleaned_data.get('email')
       if User.objects.filter(email=email).exists():
            raise ValidationError("Email exists")
       return self.cleaned_data

class ProfileEdit(forms.ModelForm):
    first_name = forms.CharField(
        label='',widget=forms.TextInput(attrs={'placeholder':'FirstName','class':'form-control w-50'}))
    last_name = forms.CharField(
        label='',widget=forms.TextInput(attrs={'placeholder':'LastName','class':'form-control w-50'}))
    class Meta:
        model = User
        fields = ("first_name","last_name")
        
        


class ProfileForm(forms.ModelForm):
    """A class that represents a registration form for the Profile model"""
    date_of_birth = forms.DateField(widget=SelectDateWidget(years=range(1970, datetime.today().year + 1, 1),
    attrs={'style':'background-color:white','class':' border border-white-50 border-1 rounded'}))
    phone_number = PhoneNumberField(
        # label='',widget=PhoneNumberPrefixWidget(country_choices=[

        #          ("syria  ", "+963"),

        #     ],

        # )
    )

    class Meta:
        model = Profile
        fields = ("date_of_birth","picture","gender","phone_number")
        

class BlogForm(forms.ModelForm):
    title = forms.CharField(
        label='',widget=forms.TextInput(attrs={'placeholder':'title','class':'form-control form-control-user'}))
    description = forms.CharField(
        label='',widget=forms.Textarea(attrs={'placeholder':'description','class':'form-control '}))
    
    titleAr = forms.CharField(
        label='',widget=forms.TextInput(attrs={'placeholder':'عنوان','class':'form-control form-control-user'}))
    descriptionAr = forms.CharField(
        label='',widget=forms.Textarea(attrs={'placeholder':'وصف','class':'form-control '}))
    
    class Meta:
        model = Blog
        fields = ('title','titleAr','photo','tags','description','descriptionAr','is_active')

class sliderForm(forms.ModelForm):
    title = forms.CharField(
        label='',widget=forms.TextInput(attrs={'placeholder':'title','class':'form-control'}))
    description = forms.CharField(
        label='',widget=forms.Textarea(attrs={'placeholder':'description','class':'form-control '}))
    titleAr = forms.CharField(
        label='',widget=forms.TextInput(attrs={'placeholder':'عنوان','class':'form-control'}))
    descriptionAr = forms.CharField(
        label='',widget=forms.Textarea(attrs={'placeholder':'وصف ','class':'form-control '}))

    class Meta:
        model = Slider
        fields = ('title','titleAr','sliderimg','description','descriptionAr','url')



class WhyUsForm(forms.ModelForm):
    title = forms.CharField(
        label='',widget=forms.TextInput(attrs={'placeholder':'title','class':'form-control'}))
    description = forms.CharField(
        label='',widget=forms.Textarea(attrs={'placeholder':'description','class':'form-control '}))
    
    titleAr = forms.CharField(
        label='',widget=forms.TextInput(attrs={'placeholder':'العنوان','class':'form-control'}))
    descriptionAr = forms.CharField(
        label='',widget=forms.Textarea(attrs={'placeholder':'الوصف','class':'form-control '}))
    
    question_one = forms.CharField(
        label='',widget=forms.TextInput(attrs={'placeholder':'question_one','class':'form-control'}))
    answer_one = forms.CharField(
        label='',widget=forms.Textarea(attrs={'placeholder':'answer_one','class':'form-control '}))
    
    question_two = forms.CharField(
        label='',widget=forms.TextInput(attrs={'placeholder':'question_two','class':'form-control'}))
    answer_two = forms.CharField(
        label='',widget=forms.Textarea(attrs={'placeholder':'answer_two','class':'form-control '}))
    
    question_three = forms.CharField(
        label='',widget=forms.TextInput(attrs={'placeholder':'question_three','class':'form-control'}))
    answer_three = forms.CharField(
        label='',widget=forms.Textarea(attrs={'placeholder':'answer_three','class':'form-control '}))
    
    question_oneAr = forms.CharField(
        label='',widget=forms.TextInput(attrs={'placeholder':'السؤال الاول','class':'form-control'}))
    answer_oneAr = forms.CharField(
        label='',widget=forms.Textarea(attrs={'placeholder':'الجواب','class':'form-control '}))
    
    question_twoAr = forms.CharField(
        label='',widget=forms.TextInput(attrs={'placeholder':'السؤال الثاني','class':'form-control'}))
    answer_twoAr = forms.CharField(
        label='',widget=forms.Textarea(attrs={'placeholder':'الجواب','class':'form-control '}))
    
    question_threeAr = forms.CharField(
        label='',widget=forms.TextInput(attrs={'placeholder':'السؤال الثالث','class':'form-control'}))
    answer_threeAr = forms.CharField(
        label='',widget=forms.Textarea(attrs={'placeholder':'الجواب','class':'form-control '}))
    

    class Meta:
        model = WhyUs
        fields = ('title','description','titleAr','descriptionAr','img','videoUrl',
        'question_one','answer_one','question_two','answer_two','question_three','answer_three',
        'question_oneAr','answer_oneAr','question_twoAr','answer_twoAr','question_threeAr','answer_threeAr',)



class FAQForm(forms.ModelForm):
    
    question_one = forms.CharField(
        label='',widget=forms.TextInput(attrs={'placeholder':'question_one','class':'form-control'}))
    answer_one = forms.CharField(
        label='',widget=forms.Textarea(attrs={'placeholder':'answer_one','class':'form-control '}))
    
    question_two = forms.CharField(
        label='',widget=forms.TextInput(attrs={'placeholder':'question_two','class':'form-control'}))
    answer_two = forms.CharField(
        label='',widget=forms.Textarea(attrs={'placeholder':'answer_two','class':'form-control '}))
    
    question_three = forms.CharField(
        label='',widget=forms.TextInput(attrs={'placeholder':'question_three','class':'form-control'}))
    answer_three = forms.CharField(
        label='',widget=forms.Textarea(attrs={'placeholder':'answer_three','class':'form-control '}))
    
    question_four = forms.CharField(
        label='',widget=forms.TextInput(attrs={'placeholder':'question_four','class':'form-control'}))
    answer_four = forms.CharField(
        label='',widget=forms.Textarea(attrs={'placeholder':'answer_four','class':'form-control '}))
    
    question_five = forms.CharField(
        label='',widget=forms.TextInput(attrs={'placeholder':'question_five','class':'form-control'}))
    answer_five = forms.CharField(
        label='',widget=forms.Textarea(attrs={'placeholder':'answer_five','class':'form-control '}))
    
    class Meta:
        model = FAQ
        fields = ('question_one','answer_one','question_two','answer_two','question_three','answer_three','question_four','answer_four','question_five','answer_five',)


class FAQARForm(forms.ModelForm):
    
    question_one = forms.CharField(
        label='',widget=forms.TextInput(attrs={'placeholder':'السؤال الاول','class':'form-control'}))
    answer_one = forms.CharField(
        label='',widget=forms.Textarea(attrs={'placeholder':'الجواب ','class':'form-control '}))
    
    question_two = forms.CharField(
        label='',widget=forms.TextInput(attrs={'placeholder':'السؤال الثاني','class':'form-control'}))
    answer_two = forms.CharField(
        label='',widget=forms.Textarea(attrs={'placeholder':'الجواب','class':'form-control '}))
    
    question_three = forms.CharField(
        label='',widget=forms.TextInput(attrs={'placeholder':'السؤال الثالث','class':'form-control'}))
    answer_three = forms.CharField(
        label='',widget=forms.Textarea(attrs={'placeholder':'الجواب','class':'form-control '}))
    
    question_four = forms.CharField(
        label='',widget=forms.TextInput(attrs={'placeholder':'السؤال الرابع','class':'form-control'}))
    answer_four = forms.CharField(
        label='',widget=forms.Textarea(attrs={'placeholder':'الجواب','class':'form-control '}))
    
    question_five = forms.CharField(
        label='',widget=forms.TextInput(attrs={'placeholder':'السؤال الخامس','class':'form-control'}))
    answer_five = forms.CharField(
        label='',widget=forms.Textarea(attrs={'placeholder':'الجواب','class':'form-control '}))
    
    class Meta:
        model = FAQAR
        fields = ('question_one','answer_one','question_two','answer_two','question_three','answer_three','question_four','answer_four','question_five','answer_five',)
