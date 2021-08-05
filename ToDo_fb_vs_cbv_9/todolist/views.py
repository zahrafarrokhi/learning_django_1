from django.shortcuts import render, HttpResponse,redirect,get_object_or_404
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView
from .forms import TaskForm
from .models import Task
from django.views import View
from django.views.generic import ListView,DeleteView,UpdateView,DeleteView
from django.urls import reverse_lazy
from django.contrib import messages

# Create your views here.

# Retrieve/Display Task
def index(request):
    # return HttpResponse("Hello World!!")
    form = TaskForm()
    if request.method == "POST":
        # Get the posted form
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect("index")
    tasks = Task.objects.all() # add this
    return render(request, "todolist/index.html", {"task_form": form, "tasks": tasks})

class Index(View):
    def get(self,request):
        form = TaskForm()
        tasks = Task.objects.all() 
        return render(request, "todolist/index.html", {"task_form": form, "tasks": tasks})

    def post(self,requset):
        form = TaskForm(self.request.POST)
        if form.is_valid():
            form.save()
        return redirect("index")
        tasks = Task.objects.all() # add this
        return render(request, "todolist/index.html", {"task_form": form, "tasks": tasks})


class IndexGeneric(CreateView):
    form_class = TaskForm
    model = Task
    template_name = "todolist/index.html"
    success_url ="/"
    
    def get_context_data(self, **kwargs):
        context= super().get_context_data(**kwargs)
        tasks = Task.objects.all() 
        form = self.get_form_class()
        context.update({'task_form':form,'tasks':tasks})
        return context




# update
def update_task(request, pk):
    # task = Task.objects.get(id=pk)
    task = get_object_or_404(Task,id=pk)
    if request.method == 'GET':
        form = TaskForm(instance=task)
    if request.method == "POST":
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect("index")
    return render(request, "todolist/update_task.html", {"task_edit_form": form})

class UpdateTaskView(View):
    def get_object(self, pk):
        # task = Task.objects.get(id=pk)
        task = get_object_or_404(Task,id=pk)
        return task

    def get(self, request, pk):
        form = TaskForm(instance=self.get_object(pk))
        return render(request, "todolist/update_task.html", {"task_edit_form": form})

    def post(self,request, pk):
        form = TaskForm(request.POST, instance=self.get_object(pk))
        if form.is_valid():
            form.save()
            return redirect("index")
        return render(request, "todolist/update_task.html", {"task_edit_form": form})
        

class UpdateTaskGenericView(UpdateView):
    form_class = TaskForm
    template_name = "todolist/update_task.html"
    model = Task

    def get_success_url(self):
        # return '/'
        return reverse_lazy('index')

    def get_context_data(self, **kwargs):
        form = TaskForm(instance=self.get_object())
        context = {'task_edit_form': form}
        return context



# delete
def delete_task(request, pk):
    # task = Task.objects.get(id=pk)
    task = get_object_or_404(Task,id=pk)
    task.delete()
    return redirect("index")

class DeleteTaskView(View):
    def post(self,request,pk):
        task = get_object_or_404(Task,id=pk)
        task.delete()
        messages.success(self.request,"successfully delete")
        return redirect("index")

class DeleteTask(DeleteView):
    model = Task 
    # context_object_name = 'todo'
    # success_url ="/"
    success_url = reverse_lazy('index')


# list
def task_list(requset):
    # form = TaskForm()
    todos = Task.objects.all()
    # context ={"task_form": form, 'todos':todos}
    context ={'todos':todos} 
    return render(requset,'todolist/list.html',context)

class TaskList(ListView):
    template_name = 'todolist/list.html'
    model = Task
    # context_object_name = 'todos' #object_list
    ordering = ['-created']
    paginate_by = 4

    # def get_context_data(self,*args,**kwargs):
    #     context = super().get_context_data(*args,**kwargs)
    #     context['task_form'] = TaskForm()       
    #     return context

#detail
def detail_todo(request,pk):
    # todos = Task.objects.get(id=pk)
    todos = get_object_or_404(Task,id=pk)    
    return render(request,'todolist/detail.html',{'todos':todos})

class TaskDetail(DetailView):
    template_name = 'todolist/detail.html'
    model = Task
    context_object_name = 'todo'
    # pk_url_kwarg = 'pk'


# your task should have slug 
class TaskDetailSlug(DetailView):
    template_name = 'todolist/detail.html'
    model = Task
    context_object_name = 'todo'
    slug_field = 'slug' # model field
    slug_url_kwarg = 'slug' # slug name in your url

    # def get_queryset(self,**kwargs) :
    #     return Todo.objects.filter(slug=self.kwargs['slug'])

class TodoDetailMix(DetailView):
    template_name = 'todolist/detail.html'
    model = Task
    context_object_name = 'todo' #object
    query_pk_and_slug = True
    
    def get_object(self, queryset=None):
        queryset = self.get_queryset()
        
        pk = self.kwargs.get(self.pk_url_kwarg)
        slug = self.kwargs.get(self.slug_url_kwarg)

        if pk:
            pk_query_set = queryset.filter(pk=pk)
            print(pk_query_set)
            # Next, try looking up by slug.
        if slug:
            slug_field = self.get_slug_field()
            slug_query_set = queryset.filter(**{slug_field: slug})
            print(slug_query_set)
        print(pk_query_set.union(slug_query_set))
        try:
            queryset = pk_query_set.union(slug_query_set).get()
        except:
            queryset = pk_query_set.get()
        return queryset
        