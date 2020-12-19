from django import forms
from .models import *


class Blogform(forms.ModelForm):
    class Meta:
        model = BlogModel
        fields = [ "title", "description","image"]