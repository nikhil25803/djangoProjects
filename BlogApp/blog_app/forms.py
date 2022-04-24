from django import forms
from . import models
from django.forms import TextInput, NumberInput



class PostForm(forms.ModelForm):

    class Meta:
        model = models.Post
        fields = [
            'name', 'title', 'text', 'twitter',
        ]

        labels = {
            'name':'Name of the author',
            'title':'Title of the Blog',
            'text':'Content',
            'twitter':'Your Twitter Id',
        }

        widgets = {
            'name':forms.TextInput(attrs={'class':'form-control m-1', 'style':'width:500px', 'placeholder':'Name of the Book'}),
            'title':forms.TextInput(attrs={'class':'form-control m-1', 'style':'width:500px', 'placeholder':'Name of the Author'}),
            'text':forms.TextInput(attrs={'class':'form-control m-1', 'style':'width:500px', 'placeholder':'Write your blog here'}),
            'twitter':forms.TextInput(attrs={'class':'form-control m-1', 'style':'width:500px', 'placeholder':'Your Twitter Id'}),
        }