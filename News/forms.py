from allauth.account.forms import SignupForm
from django import forms
from django.contrib.auth.models import Group
from django.core.mail import EmailMultiAlternatives

from .models import Post
# from django.core.exceptions import ValidationError


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        # fields = '__all__'
        fields = ['author',
                  'category',
                  'title',
                  'post',
                  'rating',
                  ]


class CustomSignupForm(SignupForm):
    def save(self, request):
        user = super().save(request)
        common_users = Group.objects.get(name="common_users")
        user.groups.add(common_users)

        subject = 'Wellcome to our News Portal!'
        text = f'{user.username}, your registration is completed successfully!'
        html = (
            f'<b>{user.username}</b>, your registration is completed successfully on'
            f'<a href="http://127.0.0.1:8000/news">The News Portal</a>!'
        )
        msg = EmailMultiAlternatives(
            subject=subject, body=text, from_email=None, to=[user.email]
        )
        msg.attach_alternative(html, "text/html")
        msg.send()

        return user