from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.forms import ReadOnlyPasswordHashField
from django import forms
from .models import Profile, User
from django.core import validators
from django.contrib.auth import get_user_model
User = get_user_model()

from eshop_accounts.models import Customer


Gender_Choices = [('M', 'Male'), ('F', 'Female')]

class CustomUserCreationForm(UserCreationForm):
    phone = forms.CharField(label="شماره تلفن", required=True)

    class Meta:
        model = User
        fields = ['email',
                  'password1', 'password2', 'phone']
        labels = {
            "email": "ایمیل",
            "password1": "رمز عبور",
            "password2": "تکرار رمز عبور",

        }

        help_texts = {
            "email": "ایمیل خود را به درستی وارد کنید",
        }

    def save(self, commit=True):
        '''
        override user create form to create profile after register!
        '''
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        try:
            # if commit:
            user.save()
            Profile.objects.create(user=user, phone=self.cleaned_data["phone"])

        except Exception as e:
            user.delete()
            raise ValueError(f"cant create profile object! reason: {e}")

        return user


class CustomUserChangeForm(UserChangeForm):
    

    class Meta:
        model = User
        fields = ('email', 'first_name')


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        exclude = ['image']


