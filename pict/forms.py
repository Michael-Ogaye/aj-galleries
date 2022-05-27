
from django import forms
from django.forms import ModelForm
from .models import Image,Category,Location

class ImageForm(ModelForm):
    class Meta:
        model=Image
        fields='__all__'

class CategoryForm(ModelForm):
    class Meta:
        model=Category
        fields='__all__'

class LoctionForm(ModelForm):
    class Meta:
        model=Location
        fields='__all__'