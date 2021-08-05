from django.urls.base import reverse
from .models import Comment, Todo
from .forms import TodoCreateForm,TodoCommentForm
# 
from django.core.checks import messages
from django.db.models.base import Model
from django.shortcuts import render
from django.http import HttpResponse
# baseview
from django.views import View
from django.views.generic.base import TemplateView
# generic
# from django.views.generic.list import ListView
# from django.views.generic.detail import DetailView
# from django.views.generic.edit import FormView,CreateView,DeleteView,UpdateView
from django.views.generic import ListView,DetailView,FormView,CreateView,DeleteView,UpdateView

# formmixin
from django.views.generic.edit import FormMixin

# 
from django.urls import reverse_lazy
from django.utils.text import slugify
from django.contrib import messages


# Create your views here.
# function
def index(request):
    return HttpResponse("hello <function>")
# class base view-View
class MyView(View):
    def get(self, request, *args, **kwargs):
        return HttpResponse('Hello, World!')

# TemplateView
class HomePageView(TemplateView):
    template_name = "app_first/home.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['todos'] = Todo.objects.all()[:5]
        return context
# ListView
class TodoListView(ListView):   
    # template_name = "app_first/home.html" =>app_first/todo_list.html
    # queryset = Todo.objects.all() #object_list
    model = Todo
    # context_object_name = 'todos'
    # ordering = [-created]
    
    # def get_queryset(self):
    #     return super().get_queryset()


# DetailView with pk and slug
# class TodoDetailView (DetailView):
#     # template_name = "app_first/home.html" =>app_first/todo_detail.html
#     # queryset = Todo.objects.filter(puplished=True) #object
#     model = Todo
#     pk_url_kwarg = 'pk'
#     slug_field = 'slug'
#     slug_url_kwarg = 'slug'


class TodoDetailView(FormMixin,DetailView):
    model = Todo
    form_class = TodoCommentForm
    pk_url_kwarg = 'pk'
    slug_field = 'slug'
    slug_url_kwarg = 'slug'

    def post(self,request,*args,**kwargs):
        self.object = self.get_object()
        form = self.get_form()
        if form.is_valid():
            comment = Comment(todo=self.object,name=form.cleaned_data['name'],body=form.cleaned_data['body'])
            comment.save()
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('app_first:detail',kwargs={'pk':self.object.pk,'slug':self.object.slug})    


# FormView
class TodoCreate(FormView):
    template_name = 'app_first/todo_create.html'
    form_class = TodoCreateForm
    success_url = reverse_lazy('app_first:list')

    def form_valid(self, form):        
        self.create_todo(form.cleaned_data)
        return super().form_valid(form)
    
    def create_todo(self,data):
        todo = Todo(title =data['title'],slug=slugify(data['title']))
        todo.save()
        messages.success(self.request,'your todo added! ' ,'success')

#CreateView
class TodoCreate2(CreateView):
    model = Todo
    fields = ['title']
    template_name ='app_first/todo_create.html'
    success_url = reverse_lazy('app_first:list')

    def form_valid(self,form):
        todo = form.save(commit=False)
        todo.slug = slugify(form.cleaned_data['title'])
        todo.save()
        messages.success(self.request,'task added!','success')
        return super().form_valid(form)

# DeleteView
class DeleteTodo(DeleteView):
	model = Todo
	template_name = 'app_first/todo_delete.html'
	success_url = reverse_lazy('app_first:list')

# UpdateView
class UpdateTodo(UpdateView):
	model = Todo
	fields = ('title',)
	template_name = 'app_first/todo_update.html'
	success_url = reverse_lazy('app_first:list')

