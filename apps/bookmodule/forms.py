from django import forms
from .models import Book,Student1,Student2,Images,Address2

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
    
class Student1Form(forms.ModelForm):
    class Meta:
        model = Student1
        fields = ['name', 'address']
        
    name = forms.CharField(
        label='Student Name',
        max_length=100,
        widget=forms.TextInput(attrs={'placeholder': 'Enter student name'})
    )


class Student2Form(forms.ModelForm):
    name = forms.CharField(
        label='Student Name',
        max_length=100,
        widget=forms.TextInput(attrs={'placeholder': 'Enter student name', 'class': 'form-control'})
    )
    addresses = forms.ModelMultipleChoiceField(
        queryset=Address2.objects.all(),
        widget=forms.CheckboxSelectMultiple
    )
    class Meta:
        model = Student2
        fields = ['name', 'addresses']
        
class ImageForm(forms.ModelForm):
    class Meta:
        model = Images
        fields= [ 'name' , 'image']