from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

app_name ='user'
urlpatterns = [   
    path('login/',views.UserLogin.as_view(),name = 'login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),  
    # rest
    path('reset/', views.UserPassReset.as_view(), name='reset_pass'),
    path('reset/done/', views.PasswordResetDone.as_view(), name='password_reset_done'),
    path('confirm/<uidb64>/<token>/', views.PasswordResetConfirm.as_view(), name='password_reset_confirm'),
	path('confirm/done/', views.PasswordResetComplete.as_view(), name='password_reset_complete'),
    
    
]