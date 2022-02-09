# -*- coding: utf-8 -*-

from django import forms
from core.models import Book, Author

# -----------------------------------------------------------------------------
# Project
# -----------------------------------------------------------------------------


class BookAddForm(forms.ModelForm):
 
    """Custom UserCreationForm."""

    class Meta():
        model = Book
        fields = "__all__"

    def __init__(self, *args, **kwargs):
        super(BookAddForm, self).__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs.update({'class' : 'form-control'})
        self.fields['description'].widget.attrs['rows'] = '4'

class AuthorAddForm(forms.ModelForm):
 
    """Custom AuthorAddForm."""

    class Meta():
        model = Author
        fields = "__all__"

    def __init__(self, *args, **kwargs):
        super(AuthorAddForm, self).__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs.update({'class' : 'form-control'})
            
