# from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
# from django.contrib.auth.models import User

from django import forms
from .models import QRcode, JpgToPng, YouTubeDownload


class QRcodeForm(forms.ModelForm):
    class Meta:
        model = QRcode
        fields = [
            'username',
            'name',
            'link',
            'dimension',

        ]

        widgets = {
            'username': forms.TextInput(attrs={
                'placeholder': 'Enter your username',
                'class': 'form-control'
            }),

            'name': forms.TextInput(attrs={
                'placeholder': 'Enter name for your code',
                'class': 'form-control'
            }),

            'link': forms.TextInput(attrs={
                'placeholder': 'Enter a link',
                'class': 'form-control'
            }),

        }


class JpgToPngForm(forms.ModelForm):
    class Meta:
        model = JpgToPng

        fields = [
            'username',
            'images',
            'name',

        ]

        widgets = {
            'username': forms.TextInput(attrs={
                'placeholder': 'Enter your username',
                'class': 'form-control'
            }),

            'name': forms.TextInput(attrs={
                'placeholder': 'Enter name for your png file',
                'class': 'form-control'
            }),
        }


class YouTubeDownloadForm(forms.ModelForm):
    class Meta:
        model = YouTubeDownload
        fields = [
            'username',
            'link'

        ]

        widgets = {
            'username': forms.TextInput(attrs={
                'placeholder': 'Enter your username',
                'class': 'form-control'
            }),

            'link': forms.TextInput(attrs={
                'placeholder': 'Enter a link of your video',
                'class': 'form-control'
            }),

        }


class LinkShortenerForm(forms.Form):
    link = forms.CharField(widget=forms.TextInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'Enter a link'
        }
    ))
