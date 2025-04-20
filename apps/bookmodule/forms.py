from django import forms
from .models import Book

class Book_form(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['title', 'author', 'price', 'edition']
        
    title = forms.CharField(
        label='Title',
        max_length=200,
        widget=forms.TextInput(attrs={'placeholder': 'Enter book title'})
    )

    author = forms.CharField(
        label='Author',
        max_length=200,
        widget=forms.TextInput(attrs={'placeholder': 'Enter author name'})
    )

    price = forms.DecimalField(
        label='Price',
        max_digits=6,
        decimal_places=2,
        widget=forms.NumberInput(attrs={'min': 0})
    )

    edition = forms.IntegerField(
        label='Edition',
        widget=forms.NumberInput(attrs={'min': 1})
    )