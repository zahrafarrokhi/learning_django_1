from django.urls import path, include
from . import views

urlpatterns = [
    
    path("", views.IndexGeneric.as_view(), name="index"),
    path("list/", views.TaskList.as_view(), name="list"),
    # detail(pk)
    path("detail/<int:pk>/", views.TaskDetail.as_view(), name="detail_pk"),
    # detail(slug) # your task should have slug 
    path("detail/<str:slug>/", views.TaskDetailSlug.as_view(), name="detail_slug"),
    # deatil(pk_slug)
    path("detail/<int:pk>/<str:slug>/", views.TodoDetailMix.as_view(), name="detail_pk_slug"),    
    path("update/<int:pk>/", views.UpdateTaskGenericView.as_view(), name="update_task"),
    path("delete/<int:pk>/", views.DeleteTaskView.as_view(), name="delete_task"), 
]