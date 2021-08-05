from django.urls import path

# test postman GET
# from . import views
# urlpatterns = [
#     path('', views.index, name='index'),
#     ]


from questions.views import login_page,register,whoami,add_question,question_list_view


urlpatterns = [
    path('login/', login_page ,name='login_page'),
    path('register/', register,name='register'),
    path('whoami/', whoami,name='whoami'),
    path('add/', add_question,name='add'),
    # path('exam-list/', exam_list, name='exam-list'),
    # path('question-list/<int:id>/', question-list),
    path('question-list', question_list_view, name='question-list')

    ]