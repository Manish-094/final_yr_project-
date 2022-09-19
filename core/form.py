from django import forms
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm,UsernameField,PasswordChangeForm
from django.contrib.auth.models import User
from django.db.models.fields import AutoField

class SignUpForm(UserCreationForm):
    password1 = forms.CharField(label='Password',widget=forms.PasswordInput(attrs={'class':'form-control'}))
    password2 = forms.CharField(label='Password Again',widget=forms.PasswordInput(attrs={'class':'form-control'}))
    email = forms.CharField(required=True,widget=forms.EmailInput(attrs={'class':'form-control'}))
    class Meta:
        model = User
        fields = ('username','email')
        widgets = {'username':forms.TextInput(attrs={'class':'form-control'})}
        
class MyLoginForm(AuthenticationForm):
    username = UsernameField(widget=forms.TextInput(attrs={'autofocus':True,'class':'form-control'}))
    password = forms.CharField(
        label = 'password',
        strip=False,
        widget=forms.PasswordInput(attrs={'autofocus':'current-password','class':'form-control'}),
        )
    
    
class MyChangePasswordForm(PasswordChangeForm):
    old_password = forms.CharField(
        label="old_password",
        strip=False,
        widget=forms.PasswordInput(attrs={'autocomplete':'current-password','autofocus':True,'class':'form-control'}),
    )
    new_password1 = forms.CharField(
        label="New Password",
        strip=False,
        widget=forms.PasswordInput(attrs={'autocomplete':'current-password','class':'form-control'}),
    )
    new_password2 = forms.CharField(
        label="New Password Again",
        strip=False,
        widget=forms.PasswordInput(attrs={'autocomplete':'current-password','class':'form-control'}),
    )
    