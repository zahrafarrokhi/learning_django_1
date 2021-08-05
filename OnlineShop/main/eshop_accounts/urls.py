from django.urls import path
from . import views



app_name = 'eshop_accounts'
urlpatterns = [
	path('login/', views.user_login, name='login'),
]