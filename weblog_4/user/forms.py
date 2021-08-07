from django import forms
from django.contrib.auth.models import User


class UserLogin(forms.Form):
    username = forms.CharField(max_length=30,widget=forms.TextInput(attrs={'class':'form-control','placeholder':'please enter your name'}))
    password = forms .CharField(max_length=30,widget=forms.PasswordInput(attrs={'class':'form-control','placeholder':'please enter your password'}))


messages = {
	'required':'این فیلد اجباری است',
	'invalid':'لطفا یک ایمیل معتبر وارد کنید',
	'max_length':'تعداد کاراکترها بیشتر از حد مجاز است'}

class UserRegister(forms.Form):
    username = forms.CharField(error_messages=messages,max_length=30,widget=forms.TextInput(attrs={'class':'form-control','placeholder':'enter your name'}))
    email = forms.EmailField(error_messages=messages,max_length=30,widget=forms.EmailInput(attrs={'class':'form-control','placeholder':'enter your email'}))
    password1 = forms.CharField(error_messages=messages,label='password',max_length=30,widget=forms.PasswordInput(attrs={'class':'form-control','placeholder':'enter your password'}))
    password2 = forms.CharField(error_messages=messages,label='confirmpassword',max_length=30,widget=forms.PasswordInput(attrs={'class':'form-control','placeholder':'enter your password'}))


    def clean_email(self):
        email = self.cleaned_data['email']
        user = User.objects.filter(email=email)
        if user.exists():
            raise forms.ValidationError('This email already exists')
        return email

    # def clean_password2(self):
    #     p1 = self.cleaned_data['password1']
    #     p2 = self.cleaned_data['password2']

    #     if p1 != p2:
    #         raise forms.ValidationError('passwords must match')
    #     return p1

    def clean(self):
        cleaned_data = super().clean()
        p1 = cleaned_data.get('password1')
        p2 = cleaned_data.get('password2')

        if p1 and p2:
            if p1 != p2:
               raise forms.ValidationError('passwords must match')
