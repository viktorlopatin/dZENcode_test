from django import forms
from django.core.exceptions import ValidationError

from .models import *
from captcha.fields import CaptchaField


class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        fields = ['text', 'file']
        widgets = {
            'text': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
            'file': forms.FileInput(attrs={'class': 'form-control-file'})
        }

    name = forms.CharField(max_length=200, widget=forms.TextInput(attrs={'class': 'form-control'}))
    email = forms.CharField(max_length=200, widget=forms.TextInput(attrs={'class': 'form-control'}))
    captcha = CaptchaField()

