from django import forms
from django.db import models
from django.db.models import fields
from .models import Comment, Todo

class TodoCreateForm(forms.Form):
    title = forms.CharField(max_length=150)


class TodoCommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = {'name','body'}
