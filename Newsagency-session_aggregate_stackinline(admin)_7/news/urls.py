from django.urls import path

from .views import show_articles,article_list,article_detail


urlpatterns = [
    path('', show_articles),
    path('article/', article_list, name='article_list'),
    path('article/<str:slug>', article_detail, name='article_detail'),
   
]
