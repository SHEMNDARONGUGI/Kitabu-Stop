from django import forms
from .models import Resource

class ResourceForm(forms.ModelForm):
    class Meta:
        model = Resource
        fields = ['title', 'document']

    # Customizing widgets to add Bootstrap classes and custom styling
    title = forms.CharField(
        widget=forms.TextInput(attrs={
            'class': 'form-control', 
            'placeholder': 'Enter Resource Title',
            'style': 'color: black;'  # Ensuring the title text is black
        })
    )
    document = forms.FileField(
        widget=forms.ClearableFileInput(attrs={
            'class': 'form-control-file', 
            'style': 'color: black;'  # Ensuring the document field text is black
        })
    )
