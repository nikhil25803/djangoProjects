# from pyexpat import model
from dataclasses import fields
from pyexpat import model
from django import forms

from .models import book_upload, request_book

class BookForm(forms.ModelForm):

    class Meta:
        model = book_upload
        fields = [
            'title', 'author', 'year', 'country', 'pages', 'languages', 'link',
        ]

        labels = {
            'title':'Name of the book',
            'author':'Author of the Book',
            'year':'Year of Publication',
            'country':'Country of Publication',
            'pages':'Number of Pages',
            'languages':'Language of the Book',
            'link':'Link of Wikipedia',
        }

        widgets = {
            'title':forms.TextInput(attrs={'class':'form-control m-1', 'style':'width:500px', 'placeholder':'Name of the Book'}),
            'author':forms.TextInput(attrs={'class':'form-control m-1', 'style':'width:500px', 'placeholder':'Name of the Author'}),
            'year':forms.NumberInput(attrs={'class':'form-control m-1', 'style':'width:500px', 'placeholder':'Year of Publication'}),
            'country':forms.TextInput(attrs={'class':'form-control m-1', 'style':'width:500px', 'placeholder':'Country Published in'}),
            'pages':forms.NumberInput(attrs={'class':'form-control m-1', 'style':'width:500px', 'placeholder':'Number of Pages'}),
            'languages':forms.TextInput(attrs={'class':'form-control m-1', 'style':'width:500px', 'placeholder':'Languages Used'}),
            'link':forms.TextInput(attrs={'class':'form-control m-1', 'style':'width:500px', 'placeholder':'Link to WikiPedia'}),
        }

class RequestForm(forms.ModelForm):

    class Meta:
        model = request_book

        fields = [
            'name','email','number','book','author', 'book_link',
        ]

        label = {
            'name':'Your Name',
            'email':'Email Address',
            'number':'Contact',
            'book':'Name of the Book',
            'author':'Name of the Author',
            'book_link':'Wikipedia Link to Book'
        }

        widgets = {
            'name':forms.TextInput(attrs={'class':'form-control m-1', 'style':'width:500px'}),
            'email':forms.EmailInput(attrs={'class':'form-control m-1', 'style':'width:500px'}),
            'number':forms.NumberInput(attrs={'class':'form-control m-1', 'style':'width:500px'}),
            'book':forms.TextInput(attrs={'class':'form-control m-1', 'style':'width:500px'}),
            'author':forms.TextInput(attrs={'class':'form-control m-1', 'style':'width:500px'}),
            'book_link':forms.TextInput(attrs={'class':'form-control m-1', 'style':'width:500px'}),
            
        }
