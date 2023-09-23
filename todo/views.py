from django.shortcuts import render,redirect
from .models import Todo
from .forms import TodoForm
# Create your views here.

def listTodo(request):
    
    form = TodoForm()

    if request.method == 'POST':
        new_todo = request.POST.get('new_todo')
        if new_todo:
            Todo.objects.create(todo=new_todo)

    
    todos = Todo.objects.all()
    context = {
        'todos':todos
    }
    return render(request,'todo/index.html',context)

def deleteTodo(request,pk):
    Todo.objects.filter(id=pk).delete()
    return redirect('home')


    