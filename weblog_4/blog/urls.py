
from django.urls import path
from . import views


app_name = 'blog'
urlpatterns = [
   path('', views.all_articles, name='all_articles'),
	path('<int:id>', views.article_detail_id, name='article_detail_d'),
	path('<str:slug>', views.article_detail, name='article_detail'),
   # id & slug
   path('<int:id>/<str:slug>/', views.article_details, name='article_detail'),
]
