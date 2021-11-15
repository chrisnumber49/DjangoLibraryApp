from django.forms import ModelForm, TextInput, EmailInput, Textarea
from .models import Books
# DataFlair


class BookCreate(ModelForm):
    class Meta:
        model = Books
        # inherit the "Books" model in models.py
        fields = '__all__'
        # use widgets to add attributes of model fields
        widgets = {
            'title': TextInput(attrs={
                'class': 'form-control', 'placeholder': 'Book title'
            }),
            'author': TextInput(attrs={
                'class': 'form-control', 'placeholder': 'Author'
            }),
            'email': EmailInput(attrs={
                'class': 'form-control', 'placeholder': 'Email (optional)'
            }),
            'describe': Textarea(attrs={
                'class': 'form-control', 'placeholder': 'Description'
            })
        }
