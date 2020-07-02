from django import forms

from blog.models import BlogModel


class BlogAddForm(forms.ModelForm):
    class Meta:
        model=BlogModel
        # fields=['']
        exclude=['image']