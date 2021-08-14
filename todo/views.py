from django.shortcuts import redirect, render
from .models import Todo
# Create your views here.


def show_todos(request):
    todos=Todo.objects.all()
    return render(request,'home.html',{"todos":todos})

def add_todo(request):
    title=request.POST.get("title")
    data=Todo.objects.create(name=title)    
    data.save()
    return redirect(show_todos)
  

def delete_todo(request,choice):
    Todo.objects.filter(id=choice).delete()
    return redirect(show_todos)