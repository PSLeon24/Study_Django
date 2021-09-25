from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from .models import*

# Create your views here.


def index(request):
    todos = Todo.objects.all()
    content = {'todos': todos}
    return render(request, 'my_to_do_app/index.html', content)


def createTodo(request):
    user_input_str = request.POST['todoContent']
    new_todo = Todo(content=user_input_str)
    new_todo.save()
    return HttpResponseRedirect(reverse('index'))
    # testing to load data
    # return HttpResponse("Created! Todo! => " + user_input_str)


def activeTodo(request):
    done_todo_id = request.GET['todoNum']
    todo = Todo.objects.get(id=done_todo_id)
    if request.method == 'GET' and 'success' in request.GET:
        todo.isDone = True
        todo.save()
    elif request.method == 'GET' and 'delete' in request.GET:
        todo.delete()
    elif request.method == 'GET' and 'reset' in request.GET:
        todo.isDone = False
        todo.save()
    return HttpResponseRedirect(reverse('index'))
