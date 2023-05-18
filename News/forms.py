from django import forms
from .models import Post
# from django.core.exceptions import ValidationError


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        # fields = '__all__'
        fields = ['author',
                  'category',
                  'title',
                  'type',
                  'post',
                  'rating',
                  ]
