from django.shortcuts import render, redirect
from django.http import HttpResponse

from .models import Todo


# Create your views here
# .

def home(request):

    todos = Todo.objects.all()

    return render(request, 'home.html', {'todos': todos})


def create(request):
    if request.method == 'GET':
        return render(request, 'create.html')

    elif request.method == 'POST':
        title = request.POST['title']
        description = request.POST['description']
        date = request.POST['date']
        completed = False
        print(date)
        todo = Todo.objects.create(
            title=title, description=description, completiondate=date, completed=completed)

        todo.save()

        todos = Todo.objects.all()

        return render(request, 'home.html', {'todos': todos})


def update_value(request):
    if request.method == 'POST':
        obj_id = request.POST.get("object_id")
        obj = Todo.objects.get(id=obj_id)
        obj.completed = True
        obj.save()

    todos = Todo.objects.all()
    return render(request, 'home.html', {'todos': todos})

    # return redirect(to='home')
