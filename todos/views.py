from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Todo
from django.contrib.auth.decorators import login_required
from .forms import CreateTodo

# Create your views here.
# To display all lists of todos
@login_required(login_url='/accounts/login/')
def todos_list(request):
    todos = Todo.objects.all().filter(creater = request.user).order_by('date')
    return render(request,'todos/todos_list.html',{'todos':todos})


# To create new todo
@login_required(login_url='/accounts/login/')
def todos_create(request):
    if request.method == 'POST':
        todos = CreateTodo(request.POST,request.FILES)
        if todos.is_valid():
            #save article to db 
            instance = todos.save(commit=False)
            instance.creater = request.user
            instance.save()
            return redirect('todos:list')
    else:
        todos = CreateTodo()
    return render(request,'todos/todos_create.html',{'todos':todos})

# To display details of todo
@login_required(login_url='/accounts/login/')
def todos_detail(request,id):
    todos = Todo.objects.get(id=id)
    return render(request,'todos/todos_detail.html',{'todos':todos})

def todos_about(request):
    return render(request,'todos/about.html')

#To Update existing todo
@login_required(login_url='/accounts/login/')
def todos_update(request,id):
   # print(t)
    todos = Todo.objects.get(id=id)
    form = CreateTodo(request.POST,request.FILES,instance=todos)
    if form.is_valid():
        form.save()
        return redirect('todos:list')

    return render(request,'todos/todos_update.html',{'form':form, 'todos':todos})

# To Delete existing todos
def todos_delete(request,id):
    todos = Todo.objects.get(id=id)
    if request.method == 'POST':
        todos.delete()    
        return redirect('todos:list')

    return render(request,'todos/todos_delete.html',{'todos':todos})

