from django.http.response import HttpResponse
from django.shortcuts import get_object_or_404, render

# Create your views here.
from .models import Todo
def hello(requset):
    return HttpResponse('hello')


def all_todos(requset):
    todos = Todo.objects.all()
    context ={'todos':todos}
    return render(requset,'todo/alltodo.html',context)


def detail_todo(request,id):
#     todo = Todo.objects.get(id=id)
    todo = get_object_or_404(Todo,id=id)
    return render(request,'todo/todo.html',{'todo':todo})







