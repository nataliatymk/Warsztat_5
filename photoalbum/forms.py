from django import forms
from django.forms import ModelForm

from photoalbum.models import Photo


class AddPhotoForm(ModelForm):
    class Meta:
        model = Photo
        exclude = ("user",)


class LoginForm(forms.Form):
    email = forms.EmailField(label="email")
    password = forms.CharField(label="Haslo", widget=forms.PasswordInput)