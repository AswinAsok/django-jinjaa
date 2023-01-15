from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
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


def signup(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        password1 = request.POST['password']
        email = request.POST['email']

        if User.objects.filter(username=username).exists():
            print("Username Taken")
        elif User.objects.filter(email=email).exists():
            print("Email Registered")
        else:
            user = User.objects.create_user(
                username=username, password=password1, email=email, first_name=first_name, last_name=last_name)
            user.save()
            print("Havvu!!")

        return redirect('/home')
    else:
        return render(request, 'signup.html')
