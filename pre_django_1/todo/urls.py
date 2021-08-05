from django.urls import path
from django.urls.resolvers import URLPattern
# from .views import hello
from . import views

urlpatterns = [

    # path('',hello,name='hello')
    path('',views.hello,name='hello'),
    path('all',views.all_todos,name='all'),
    path('detail/<int:id>',views.detail_todo,name='detail')
]