from django.shortcuts import render
from .models import Todo


# Create your views here
# .

def index(request):

    todos = Todo.objects.all()

    return render(request, 'index.html', {'todos': todos})


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

        return render(request, 'index.html', {'todos': todos})
