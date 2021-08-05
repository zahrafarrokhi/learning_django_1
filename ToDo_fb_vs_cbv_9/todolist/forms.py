from django import forms
from django.forms import ModelForm, widgets
from .models import Task


# class TaskForm(forms.ModelForm):
#     class Meta:
#         model = Task
#         fields = "__all__"  # include all fields in form
#         # fields=('title','completed') # include particular fileds of model in form


# with style
class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = "__all__" 
        widgets = {'title': forms.TextInput(attrs={
                "class": "form-control form-control-lg",
                "placeholder": "Enter task...",}),         
                'completed':forms.CheckboxInput(attrs={"class": "form-check-input"}),
                }
        

    