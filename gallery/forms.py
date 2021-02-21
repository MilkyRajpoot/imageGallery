from django import forms  
from . models import *
import re
from django.contrib.auth.forms import UserCreationForm
from django.core.exceptions import ValidationError
from django.core.files.images import get_image_dimensions
from crispy_forms.helper import FormHelper

class SignUpForm(UserCreationForm):
    name = forms.CharField(max_length=30, required=True)
    mobile = forms.CharField(min_length=10,max_length=12,required=True)
    email = forms.EmailField(max_length=255,required=True)

    class Meta:
        model = Users
        fields = ('name', 'email','mobile','password1', 'password2')

    widgets = {
            'name': forms.TextInput(attrs={'placeholder': 'Enter Name','class':'form-control'}),
            'email': forms.TextInput(attrs={'placeholder': 'Enter Email-Id','class':'form-control'}),
            'password1': forms.TextInput(attrs={'placeholder': 'Enter Password','class':'form-control'}),
            'password2': forms.TextInput(attrs={'placeholder': 'Confirm Password','class':'form-control'}),
            'mobile': forms.Textarea(attrs={'cols':10,'rows':5,'placeholder': 'Enter Mobile Number','class':'form-control'}),
        }

class OTP_Verification(forms.ModelForm):
    otp = forms.CharField(max_length=6,required=True)

    class Meta:
        model = OTP_verification
        fields = ('otp',)

class ImagesForm(forms.ModelForm):

    class Meta:
        model = Images
        fields = '__all__'
