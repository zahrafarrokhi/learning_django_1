from django.shortcuts import render
from django.contrib.auth import views as auth_views
from django.urls import reverse_lazy
# Create your views here.

class UserLogin(auth_views.LoginView):
	template_name = 'user/login.html'

class UserPassReset(auth_views.PasswordResetView):
	template_name = 'user/password_reset_form.html'
	success_url = reverse_lazy('user:password_reset_done')
	email_template_name = 'user/password_reset_email.html'

class PasswordResetDone(auth_views.PasswordResetDoneView):
	template_name = 'user/reset_done.html'

class PasswordResetConfirm(auth_views.PasswordResetConfirmView):
	template_name = 'user/password_reset_confirm.html'
	success_url = reverse_lazy('user:password_reset_complete')

class PasswordResetComplete(auth_views.PasswordResetCompleteView):
	template_name = 'user/password_reset_complete.html'

