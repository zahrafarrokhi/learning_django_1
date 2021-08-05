from django.urls import path,re_path

from . import views

app_name ='app_first'
urlpatterns = [   
    path('home/',views.index,name = 'home'),
    path('view/', views.MyView.as_view(), name='view'),
    path('tem/', views.HomePageView.as_view(), name='template'),
    path('', views.TodoListView.as_view(), name='list'),
    # path('list/', views.TodoListView.as_view(), name='list'),
    path('create/', views.TodoCreate.as_view(), name='create_todo'),  
    path('create2/', views.TodoCreate2.as_view(), name='create_todo'),
    # persian_urls  you need repath ?
    # re_path(r'detail/(?P<slug>[-\w]+)/',views.TodoDetailView.as_view(), name='detail'),
    # re_path(r'detail<int:pk>/(?P<slug>[-\w]+)', views.TodoDetailView.as_view(), name='detail'), 
    path('<int:pk>/<str:slug>', views.TodoDetailView.as_view(), name='detail'),
    # path('detail<int:pk>/<str:slug>', views.TodoDetailView.as_view(), name='detail'),

    path('delete/<int:pk>/', views.DeleteTodo.as_view(), name='delete_todo'),
    path('update/<int:pk>/', views.UpdateTodo.as_view(), name='update_todo'),
   
    
]