from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from django.contrib.auth import authenticate, logout
from datetime import date as dated
from datetime import datetime

from django.http import HttpResponse

from .models import Todo


def home(request):
    if request.user.is_authenticated:

        pending = True
        expired = True
        completed = True

        todos = Todo.objects.filter(user=request.user)

        today = dated.today()

        incomplete_todos = []

        for todo in todos:
            if todo.completiondate < today and not todo.completed:
                incomplete_todos.append(todo)
                if expired:
                    expired = False
            if pending and not todo.completed:
                pending = False
            if completed and todo.completed:
                completed = False

        render_data = {
            'todos': todos, 'incomplete_todos':  incomplete_todos, 'pending': pending, 'expired': expired, 'completed': completed
        }

        return render(request, 'home.html', {'render_data': render_data})
    else:
        return redirect('/')


def create(request):
    if request.method == 'GET' and request.user.is_authenticated:
        return render(request, 'create.html')
    elif request.method == 'POST':
        title = request.POST['title']
        description = request.POST['description']
        date = request.POST['date']
        completed = False
        print(date)
        todo = Todo.objects.create(
            title=title, description=description, completiondate=date, completed=completed, user=request.user)

        todo.save()

        return redirect('/home')
    else:
        return redirect('/')


def update_value(request):
    if request.method == 'POST':
        obj_id = request.POST.get("object_id")
        obj = Todo.objects.get(id=obj_id)
        obj.completed = True
        obj.save()

    return redirect('/home')


def signup(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        password = request.POST['password']
        email = request.POST['email']

        if User.objects.filter(username=username).exists():
            return render(request, 'signup.html', {'error': "Username Taken, Try Another Username"})
        elif User.objects.filter(email=email).exists():
            return render(request, 'signup.html', {'error': "Email Already Registered"})
        else:
            user = User.objects.create_user(
                username=username, password=password, email=email, first_name=first_name, last_name=last_name)
            user.save()

        return redirect('/home')

    else:
        return render(request, 'signup.html')


def login(request):
    if request.method == 'POST':
        password = request.POST['password']
        username = request.POST['username']

        user = authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('/home')
        else:
            return render(request, 'login.html', {'error': "Invalid Credentials"})
    else:
        return render(request, 'login.html')


def userlogout(request):
    if request.user.is_authenticated:
        logout(request)

    return redirect('/')
